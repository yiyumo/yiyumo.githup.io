---
title: Another Sample Page
published: true
---

Text can be **bold**, _italic_, ~~strikethrough~~ or `keyword`.

[Link to another page](another-page).

# [](#Header-1)Django环境搭建及创建项目 1
1. 安装django.

    (sudo) pip install Django
    
2. 创建一个django项目

    django-admin.py startproject project_name
3. 进入项目创建项目app

    cd project_name
    python manage.py startapp app_name 或 django-admin.py startapp app_name

4. 创建数据库表 或 更改数据库表或字段

    ##### 1. 创建更改的文件
    python manage.py makemigrations
    #####  2. 将生成的py文件应用到数据库
    python manage.py migrate

5. 使用开发服务器

    python mange.py runserver 0.0.0.0:8000
6.  清空数据库

    python manage.py flush
    
7.  创建超级管理员

    python manage.py createsuperuser
    ###### 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
    ###### 修改 用户密码可以用：
    python manage.py changepassword username
    
8.  导出数据 导入数据

    python manage.py dumpdata appname > appname.json
    python manage.py loaddata appname.json
    
9.  Django 项目环境终端

    python manage.py shell

10.  数据库命令行

    python manage.py dbshell

11.  更多命令
 终端上输入 python manage.py 可以看到详细的列表，在忘记子名称的时候特别有用。

