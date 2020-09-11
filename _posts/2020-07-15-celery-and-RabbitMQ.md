#    Django Celery and RabbitMQ

一.Celery
1. 安装 Celery

        pip install Celery

2. django中使用celery
    2.1 将CELERY_BROKER_URL配置添加到settings.py文件中
            
            CELERY_BROKER_URL='amqp://localhost'
    2.2 创建一个名为celery.py:

        import  os
        from  celery import Celery 
        os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
        app=Celery('mysite')app.config_from_object('django.conf:settings',namespace='CELERY')
        app.autodiscover_tasks()
    2.3 编辑项目根目录下的__init__.py文件:
        
        from.celeryimportappascelery_app__all__=['celery_app']
    
    2.4 创建一个Celery任务:
    
        


二. RabbitMQ
1. linux 安装RabbitMQ

        apt-get install -y erlang
        完成后在控制台输入命令：
        erl
        可以查看erlang安装版本情况
        自动安装rabbitmq
        apt-get install rabbitmq-server
        查看运行状态
        service rabbitmq-server status
        保存配置后重启服务：
        service rabbitmq-server stop
        service rabbitmq-server start
        # 启用并启动RabbitMQ服务：
        #systemctlenable rabbitmq-serversystemctl start rabbitmq-server
        #检查状态以确保一切运行平稳：
        # systemctl status rabbitmq-server
        通过运行启用RabbitMQ Web管理控制台(下面这行命令是必须的，否则无法正常打开RabbitMQ)
        rabbitmq-plugins enable rabbitmq_management
        个人设置操作(创建用户，给以用户administrator权限)
        rabbitmqctl add_user adminyuan aq2017
        rabbitmqctl set_user_tags adminyuan administrator
        
2. config.py 
   连接rabbitmq 
   BROKER_URL ='amqp://guest:guest@localhost:5672//'

3. 配置django setting.py
    2.1 添加djcelery
            
            INSTALLED_APPS = [
                'djcelery'
            ]
    
    2.2 配置setting 使得在django 数据库后台，添加时间队列任务
        
        CELERY_QUEUES = (
            Queue(
                'flash_sale_change_state', 
                Exchange('flash_sale_change_state'),
                routing_key='flash_sale_change_state'
            ),
        )

    2.3 添加退了路由
    
        CELERY_ROUTES = (
            'flashsale.tasks.flash_sale_change_state': {'queue':'flash_sale_change_state',
            'routing_key':'flash_sale_change_state'},
        )
    
    2.4 编辑时间
  
        CELERYBEAT_SCHEDULE = {
            'flash_sale_change_state': {
            "task":"flashsale.tasks.flash_sale_change_state",
            "schedule": crontab(minute='*/1'),
            "args": (),
            },
        }

