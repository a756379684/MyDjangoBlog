from django.shortcuts import render
import markdown
from django.core.paginator import Paginator
from django.utils.html import strip_tags
from django.shortcuts import reverse,redirect
# Create your views here.
from django.http import HttpResponse
from .models import Article,TaggitTag,Mydynamic
from django.shortcuts import get_object_or_404
from django.db.models import Q


def index(request):
    tags = {}
    dynamic = Mydynamic.objects.all().order_by('-date')[:1]
    articles = Article.objects.all()
    for article in articles:
        for tag in article.tags.all():
            if tag not in tags:
                tags[tag] = 1
            else:
                tags[tag] = tags[tag] + 1
    search = request.GET.get('search')
    if search:
        articles = Article.objects.filter(Q(title__icontains=search)|
                                          Q(text__icontains=search)
                                          ).order_by('-create')
    else:
        search = False
        articles = Article.objects.order_by('-create')
    paginator = Paginator(articles,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #获取每个标签被使用的数量，以其数量作为标签在前端显示的字体大小
    for article in page_obj:
        article.text = strip_tags(markdown.markdown(article.text))
    context = {'articles':page_obj,'tags':tags,'dynamic':dynamic,'search':search}
    return render(request,"articles/index.html",context)

#通过标签获取相关标签的文章
def filter_by_tag(request,tag_name):
    tags = {}
    dynamic = Mydynamic.objects.all().order_by('-date')[:1]
    search = request.GET.get('search')
    if search:
        return redirect(reverse('articles:index')+'?search='+search)
    articles = Article.objects.order_by('-create')
    for article in articles:
        for tag in article.tags.all():
            if tag not in tags:
                tags[tag] = 1
            else:
                tags[tag] = tags[tag] + 1
    #获取每个标签被使用的数量，以其数量作为标签在前端显示的字体大小
    articles = Article.objects.filter(tags__name__in=[tag_name]).order_by('-create')
    paginator = Paginator(articles,13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for article in page_obj:
        article.text = strip_tags(markdown.markdown(article.text))
    context = {'articles':page_obj,'tags':tags,'dynamic':dynamic,'tag_name':tag_name}
    return  render(request,'articles/filter_by_tag.html',context)

def article_detail(request,article_id):
    tags = {}
    request.session.setdefault('article_view', [])
    dynamic = Mydynamic.objects.all().order_by('-date')[:1]
    articles = Article.objects.order_by('-create')
    search = request.GET.get('search')
    if search:
        return redirect(reverse('articles:index')+'?search='+search)
    #获取每个标签被使用的数量，以其数量作为标签在前端显示的字体大小
    for article in articles:
        for tag in article.tags.all():
            if tag not in tags:
                tags[tag] = 1
            else:
                tags[tag] = tags[tag] + 1
    extensions = ['markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.toc']
    article = get_object_or_404(Article,id=article_id)
    md = markdown.Markdown(extensions=extensions)
    article.text = md.convert(article.text)
    if article.title not in request.session['article_view']:
        request.session['article_view'].append(article.title)
        article.views += 1
        article.save(update_fields=['views'])

    context = {"article":article,'toc':md.toc,'tags':tags,'dynamic':dynamic}
    return render(request,"articles/article.html",context)

def sortByDate(request):
    tags = {}
    dynamic = Mydynamic.objects.all().order_by('-date')[:1]
    search = request.GET.get('search')
    if search:
        return redirect(reverse('articles:index')+'?search='+search)
    articles = Article.objects.all()
    for article in articles:
        for tag in article.tags.all():
            if tag not in tags:
                tags[tag] = 1
            else:
                tags[tag] = tags[tag] + 1
    dates = Article.objects.dates('create', 'month').order_by("-create")
    articles = {}
    for i in dates:
        articles[i] = Article.objects.filter(create__year=i.year,create__month=i.month)
    context = {'tags':tags,'dynamic':dynamic,'articles':articles}
    return render(request,"articles/sort_by_date.html",context)

def myself(request):
    search = request.GET.get('search')
    if search:
        return redirect(reverse('articles:index')+'?search='+search)
    return render(request,"articles/myself.html")