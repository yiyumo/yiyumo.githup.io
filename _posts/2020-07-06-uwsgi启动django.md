# uWSGI 启动django项目

 
uWSGI 模块

   uWSGI 以客户端-服务端模式运行。Web 服务器（例如 nginx，Apache）与一个 django-uwsgi "worker" 进程交互，提供动态内容。
   
1. uwsgi 安装

        pip install uwsgi 

2. 配置并启动用于 Django 的 uWSGI 服务器
    
      创建uwsgi配置文件  例如：zzz_uwsgi.ini
       
      文件类容如下：
       
        [uwsgi]
        ; 监听的端口
        http = 0.0.0.0:8000  
        ; 项目所在目录，和manage.py同级
        chdir = /home/zzz_lc_server/zzz
        
        ; 虚拟环境所在目录  virtualenv 和 home 等同
        virtualenv = /root/miniconda3/envs/zzz_lc
        ;home = /root/miniconda3/envs/zzz_lc
        # 指定python
        pythonhome = /root/miniconda3/envs/zzz_lc/bin/python3
        
        ; 主应用中的wsgi文件
        wsgi-file = zzz/wsgi.py
        
        ; 使用路由代理静态资源，但失败了
        ; static-safe=/home/kzzf/project/OfferHelp/static/
        ; route = /static/(.*) static:/home/kzzf/project/OfferHelp/static/$1
        
        ; 代理静态资源：路径映射
        ;static-map = /static=/home/zzz_lc_server/zzz/static
        
        ; 启动一个master进程，来管理其余的子进程
        master=True
        processes = 4
        threads = 2
        
        ; 保存主进程的pid，用来控制uwsgi服务
        pidfile=/home/zzz_lc_server/zzz/uwsgi.pid
        ; 启动项目  uwsgi uwsgi.ini
        ; uwsgi --stop/reload xxx.pid  停止/重启uwsgi
        
        ; 设置后台运行，保存日志
        daemonize=/home/zzz_lc_server/zzz/uwsgi.log
        ; deamonize=1  ; 用来配置background运行
        
        ; 设置每个工作进程处理请求的上限，达到上限时，将回收（重启）该进程。可以预防内存泄漏
        max-requests=5000
        
        # 服务停止时自动移除unix Socket和pid文件
        vacuum=true
        py-autoreload = 1
        root@gdbuaruqurhas0tp-0322386:/home/zzz_lc_server/zzz#
     
     用uwsgi启动django
     
        uwsgi --ini zzz_uwsgi.ini
        
        # uwsgi --stop uwsgi.pid    停止uwsgi    
        # uwsgi --reload uwsgi.pid  重启uwsgi
        # pkill uwsgi -9  杀死uwsgi进程