# -*- coding: utf-8 -*-

import psycopg2


def sjk(abc):
    conn = psycopg2.connect(database="lyy_prod", user="lyy_test", password="lyytest", host="192.168.0.202", port="5432")
    cur = conn.cursor()
    sql = "select COUNT(versionno) from lyy_equipment where versionno in ({})".format(abc)
    print(sql)
    cur.execute(sql)

    data = cur.fetchall()
    print(data)

    # 关闭数据库连接
    conn.close()
    return data

ab = []
for i in range(4900,5000):
    ab.append("'{}'".format(i))

ab1 = ','.join(ab)

sjk(ab1)


###4600~ 4699
###4900 ~ 4999
