##查看Mysql的默认提交模式,Mysql默认是autocommit
```
show variables like 'autocommit';
```

##关闭Mysql默认的自动提交模式
```
mysql> set autocommit = 0;
Query OK, 0 rows affected (0.02 sec)

mysql> show variables like 'autocommit';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | OFF   |
+---------------+-------+
1 row in set (0.00 sec)
```

##查看mysql库中user表中的默认存储引擎
show table status like 'user' \G

##Mysql默认存储引擎
默认存储引擎是MyISAM，
`*优点*`：全文索引（Full-Text Indexing），压缩，空间函数（GIS）
`*不足*`：不事务，行级锁
MyISAM将每张表存储成两个文件，数据文件和索引文件，扩展名为.MYD和.MYI
