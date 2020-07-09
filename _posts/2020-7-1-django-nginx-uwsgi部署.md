uwsgi.ini 文件

```ini
[uwsgi]
; 监听的端口
http = 0.0.0.0:8889
#the local unix socket file than commnuincate to Nginx
; socket = 127.0.0.1:8001
; socket = /home/kzzf/project/OfferHelp/OfferHelp.sock
# the base directory (full path)
; 项目所在目录，和manage.py同级
chdir = /home/zzz_lc_server/zzz
; 虚拟环境所在目录
;virtualenv = /root/miniconda3/envs/zzz_lc
home = /root/miniconda3/envs/zzz_lc
# 指定python
pythonhome = /root/miniconda3/envs/zzz_lc/bin/python3
# Django's wsgi file
; 主应用中的wsgi文件
wsgi-file = zzz/wsgi.py
; 启动一个master进程，来管理其余的子进程
master=True
# maximum number of worker processes
processes = 4
#thread numbers startched in each worker process
threads = 2
daemonize=uwsgi.log
#monitor uwsgi status
stats = 127.0.0.1:9191
# clear environment on exit
vacuum          = true
; 保存主进程的pid，用来控制uwsgi服务
pidfile=/home/zzz_lc_server/zzz/uwsgi.pid
; 设置后台运行，保存日志
daemonize=/home/zzz_lc_server/zzz/uwsgi.log
; 设置每个工作进程处理请求的上限，达到上限时，将回收（重启）该进程。可以预防内存泄漏
max-requests=5000
# 服务停止时自动移除unix Socket和pid文件
vacuum=true
py-autoreload = 1
```

nginx 配置
```editorconfig
server {

    # the port your site will be served on
    listen      80;
    # 添加ssl config
    listen 443 ssl;
    ssl on;
    # the domain name it will serve for
    server_name www.xxxx.top;   # substitute your machine's IP address or FQDN

    ssl_certificate /etc/nginx/ca/3988686_www.xxxx.top.pem;
    ssl_certificate_key /etc/nginx/ca/3988686_www.xxxx.top.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    charset     utf-8;
    # max upload size
    client_max_body_size 75M;   # adjust to taste


    #django location
    location /media {
        alias /home/zzz_lc_server/zzz/media;
        }

    location /static{
        alias /home/zzz_lc_xerver/zzz/static;
        }

    location ^~ /api/ {
        rewrite ^/api/(.*)$ /$1 break;
        uwsgi_pass django;
        include /etc/nginx/uwsgi_params;
        }

    location /admin {
        uwsgi_pass django;
        include /etc/nginx/uwsgi_params;
        }
    location ^~/baidu/ {
        proxy_pass http://api.map.baidu.com/;
        }
    # mqtt ws 转 wss  
    location /mqtt {
        proxy_pass  http://127.0.0.1:8083/mqtt;
        proxy_read_timeout 60s;
        proxy_set_header Host $host;
        proxy_set_header X-Real_IP $remote_addr;
        proxy_set_header X-Forwarded-for $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        }
    # Vue location
    
    location / {
        root /home/zzz_lc_server/dist;
        index index.html;
        #确保刷新不出现404
        try_files $uri $uri/ @router;
      }
    index login.html;
    location @router {
        rewrite ^.*$ /index.html last;
    }
}
```


启动项目脚本：

```shell script
echo "Begin deploying the mainserver web service"
echo "Temporary backup database"
mysqldump -u用户名 -p密码 数据库名 > /home/zzz_lc_server/mysql_bak_data/temporary/mainserver_$(date +%Y%m%d%H%M%S).sql #执行备份命令
cd /home/zzz_lc_server/
git pull
echo "Execute the migration file"
cd /root/miniconda3/envs/zzz_lc/bin/python3 manage.py migrate
cd /home/zzz_lc_server/zzz
echo "restart uwsgi"
uwsgi --reload uwsgi.pid
#rm uwsgi.log
#/home/pullin/.virtualenvs/projectroot/bin/uwsgi uwsgi.ini
sleep 3
ps -ef|grep uwsgi
echo "Deployment is complete"
```




nginx 指令

    $ /etc/init.d/nginx start  #启动
    $ /etc/init.d/nginx stop  #关闭
    $ /etc/init.d/nginx restart  #重启
    
    # 在部署完成之后一旦我们修改nginx的配置之后，使用reload会使我们的网址不会停止接收数据
    $ /etc/init.d/nginx reload 
    
    $ nginx -t  # 查看配置是否有