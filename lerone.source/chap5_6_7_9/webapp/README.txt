database is vsearchlogDB
user: vsearch
pword: vsearchpasswd

example of result from changing the log method to save to the DB:
mysql> select * from log
    -> ;
+----+---------------------+------------------------------------+---------+-----------+--------------+----------------------+
| id | ts                  | phrase                             | letters | ip        | browser_info | results              |
+----+---------------------+------------------------------------+---------+-----------+--------------+----------------------+
|  1 | 2017-08-02 08:07:56 | Hitch-hiker                        | aeiou   | 127.0.0.1 | firefox      | {'e', 'i'}           |
|  2 | 2017-08-02 08:08:09 | life, the universe, and everything | aeiou   | 127.0.0.1 | firefox      | {'e', 'u', 'a', 'i'} |
+----+---------------------+------------------------------------+---------+-----------+--------------+----------------------+
