# README

此为我使用Django框架开发的一个项目，也是我的第一个项目，目前我的博客就是使用该项目：[我的博客](https://www.redmango.top/)

## 简述

项目采用python的web框架中的老大哥——Django，前端采用bootstrap4以及一些自写的jquery；文章的修改、提交等都依赖于django的后端，因为该项目的上一个版本就是编写了前端页面但发现写markdown还是习惯先在本地写好然后再提交上去，若有需求可以使用Editor.md作为前端的md编写，具有实时预览以及各种功能。

博客具备文章markdown渲染，文章标签，归档，搜索，以及基于session的访客量统计，sitemap自动编写，日志记录等功能。

## 使用

clone完项目后在项目目录下使用`pip install -r requirements.txt`，之后在需要先建立好数据库并修改settings.py内对应的数据库配置，python3环境下依次运行命令：

`python manage.py makemigrations`

`python manage.py migrate`

迁移完数据后运行项目：

`python manage.py runserver`

