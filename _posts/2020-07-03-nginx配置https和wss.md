# nginx django 配置 https 和wss


### 1. nginx部署django服务基本配置

创建xxx.conf 配置表 (文件路径/etc/nginx/sites-enabled/xxx.conf)
配置完 使用 sudo /etc/init.d/nginx  restart

```editorconfig
server {
    listen 80;
    server_nmae  localhost;
    charset     utf-8;
    client_max_body_size 75M;   # adjust to taste
        
    #django location
    location /media {
        alias /home/projectroot/media;
        }

    location /django-static{
        alias /home/projectroot/public;
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
    # Vue location
    root         /home/projectroot/dist;
    location / {
        try_files $uri $uri/ @router;
        index index.html;
      }
    index login.html;
    location @router {
        rewrite ^.*$ /index.html last;
       }

}
```


### 2. 添加证书 证书为域名证书, https wss 均可使用

```editorconfig
server {
    listen 80;
    server_nmae  localhost;
    charset     utf-8;
    client_max_body_size 75M;   # adjust to taste

    # https 添加证书
    ssl on;
    listen 443 ssl;
    ssl_certificate /etc/nginx/ca/3988686_www.xxxx.top.pem;
    ssl_certificate_key /etc/nginx/ca/3988686_www.xxxx.top.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
        
    #django location
    location /media {
        alias /home/projectroot/media;
        }

    location /django-static{
        alias /home/projectroot/public;
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
    # Vue location
    root         /home/projectroot/dist;
    location / {
        try_files $uri $uri/ @router;
        index index.html;
      }
    index login.html;
    location @router {
        rewrite ^.*$ /index.html last;
       }

}
```
### 3. emqx ws转成wss
把8083转成443
```editorconfig
    # xxx.conf文件中加上如下配置
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
```


#  http https ws wss 均可使用-完整的配置文件
```editorconfig

# ComRonent nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001;  # for a web port socket (we'll use this first)
}

# configuration of the mainserver server
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
        alias /home/projectroot/media;
        }

    location /django-static{
        alias /home/projectroot/public;
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
    root         /home/projectroot/dist;
    location / {
        try_files $uri $uri/ @router;
        index index.html;
      }
    index login.html;
    location @router {
        rewrite ^.*$ /index.html last;
       }
}

```
