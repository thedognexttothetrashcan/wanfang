http://www.wanfangdata.com.cn/perio/toIndex.do
期刊导航,中国学术期刊数据库（China Science Periodical Database，CSPD）
共有期刊8571种
Content-Type: application/x-www-form-urlencoded; charset=UTF-8

{"pageNum":1,"pageSize":10,"totalRow":7923,"pageTotal":793}


a b c d e f g
70+181+294+445+9+167+535

h i j k l m n 
647+1+624+193+265+111+279

o p q r s t
0+16+181+90+869+216

u v w x y z 
0+0+199+616+373+1479

大类有用信息list:

[{'id': 'B', 'name': '哲学政法', 'count': 461}, {'id': 'C', 'name': '社会科学', 'count': 730}, {'id': 'F', 'name': '经济财政', 'count': 784}, {'id': 'G', 'name': '教科文艺', 'count': 1655}, {'id': 'N', 'name': '基础科学', 'count': 902}, {'id': 'R', 'name': '医药卫生', 'count': 1238}, {'id': 'S', 'name': '农业科学', 'count': 579}, {'id': 'T', 'name': '工业技术', 'count': 2225}]

mysql> desc periodical_list_new;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int(11)      | NO   | PRI | NULL    | auto_increment |
| perio_id      | varchar(50)  | YES  |     | NULL    |                |
| perio_title   | varchar(500) | YES  | UNI | NULL    |                |
| hostunit_name | varchar(500) | YES  |     |         |                |
| language      | varchar(255) | YES  |     | NULL    |                |
| issn          | varchar(255) | YES  |     | NULL    |                |
| cn            | varchar(255) | YES  |     | NULL    |                |
| cn_short      | varchar(255) | YES  |     | NULL    |                |
| release_cycle | varchar(255) | YES  |     | NULL    |                |
| affectoi      | float        | YES  |     | NULL    |                |
| article_num   | int(11)      | YES  |     | NULL    |                |
| funded_num    | int(11)      | YES  |     | NULL    |                |
| cite_num      | int(11)      | YES  |     | NULL    |                |
| download_num  | int(11)      | YES  |     | NULL    |                |
| core_perio    | varchar(255) | YES  |     | NULL    |                |
| trans_title   | varchar(255) | YES  |     | NULL    |                |
| crawl_time    | datetime     | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
17 rows in set (0.00 sec)
