#
##1.1 查看Mysql的默认提交模式,Mysql默认是autocommit
```
show variables like 'autocommit';
```

##1.2 关闭Mysql默认的自动提交模式
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

#2 Mysql存储引擎
##2.1 查看mysql库中user表中的默认存储引擎
show table status like 'user' \G

##2.2 Mysql默认存储引擎-MyISAM
默认存储引擎是MyISAM，
*`优点`*：全文索引（Full-Text Indexing），压缩，空间函数（GIS）
*`不足`*：不事务，行级锁
MyISAM将每张表存储成两个文件，数据文件和索引文件，扩展名为.MYD和.MYI

##手动修复表
```
check table table_name
repair table table_name
```

##2.3 MyISAM Merge引擎
MyISAM Merge是一个整体，是MyISAM的一个变种。
合并表(Merge Table)是指将几个相同的MyISAM表合并为一个虚表(Virtual Table)，对于Mysql记录日志或数据仓库应用特别有用

##2.4 InnoDB引擎
InnoDB专为事务处理设计的一个存储引擎，特别是大量短期(Short Lived)事务，短期事务是指一般能正常完成，不需要回滚操作o
InnodDB仍然是一种最广泛应用的事务性存储引擎，它的性能和崩溃自动恢复特性，也让它在非事务性存储应用中非常流行
###特性
*表空间，将所有的数据共同存储在一个或者是多个数据文件中，为种数据就称为表空间
*MVCC
*InnoDB是基于聚簇索引建立的
*外键约束

##2.5 Memory引擎
###什么时候需要使用Memory引擎
用户想获得快速的访问性能和速度，并且相关数据是不变的，或者说重启后并不需要保存数据
###什么是内存表
之前称为HEAP table，即“堆表”，访问速度快，重启只保存表结构，不保存数据，比MyISAM快一个量级，因为都是放在内存中的，无需I／O等待
###内存表的几个特性
** 用于“查找”或“映射”表
** 用于缓存周期性聚合数据(Periodically Aggerageted Data)的结果
** 用于在数据分析中产生中间结果
