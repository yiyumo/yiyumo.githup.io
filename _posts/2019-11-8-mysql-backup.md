

####将数据库zkbc 的数据做备份，导出到服务器磁盘/root/temp/上，以 zkbc20190121.sql 作为存储文件。

数据量太大可以不看日志什么的，直接备份，去掉--opt 还有 --extend--insert=false 【没有指定 --quick 或 --opt 选项，则会将整个结果集放在内存中。如果导出大数据库的话可能会出现问题。我们这里去掉了–opt,但加上了-q,该项在导出大表时很有用，它强制 mysqldump 从服务器查询取得记录直接输出而不是取得所有记录后将它们缓存到内存中。

```commandline
mysqldump -u root -p --default-character-set=utf8   --triggers -R --hex-blob --single-transaction -q  zkbc > /root/temp/zkbc20190121_1.sql;
```

----

#### 将/root/temp/zkbc190121.sql; 路径下的数据库文件导入 zkbc_new数据库，导入的两种方式①②如下
方法1

```commandline
mysql -u root -p 密码
```

在mysql连接的当前会话里，输入如下命令

```mysql
set session sql_log_bin=0;
use zkbc_new
source /root/temp/zkbc190221.sql
```

方法2
直接执行脚本即可，不用连接mysql数据库直接在服务器创建两个文件，
import_db.sh
import_Sql_file
.sh用来在linux环境执行的脚本，内容：

```commandline
#!/bin/bash
/usr/bin/mysql -u root -p 'msds007'  < /root/temp/import_sql_file.txt
```

第二个文件import_sql_file是.txt文件，只是.sh文件用来加载的，文件内容为要执行的导入指令：

```mysql
set session sql_log_bin=0;
use zkbc_new;
source /root/temp/zkbc190121.sql
```

想导入的话，直接执行脚本 ./import_db.sh 即可.

---

### 使用 mysqldump 命令对单个库进行完全备份

```commandline
mysqldump  -u  用户名   -p  [密码]   --databases   [数据库名]  >   /备份路径 /备份文件名
```

###数据恢复\
```commandline
mysql -uroot -p root
```

```mysql
drop database [数据库名];
source  /备份路径 /备份文件名
```



