#!usr/bin/env python

import psycopg2


def query1():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from popular_articles limit 3")
    result = c.fetchall()
    print("\nMost popular three articles of all time")
    for i in range(len(result)):
        article_name = result[i][0]
        views = result[i][1]
        print(article_name+"-"+str(views)+" views")
    db.close()


def query2():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from popular_article_authors")
    result1 = c.fetchall()
    print("\nMost popular article authors of all time")
    for i in range(len(result1)):
        author_name = result1[i][0]
        views1 = result1[i][1]
        print(author_name+"-"+str(views1)+" views")
    db.close()


def query3():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select time,error_per from error_percentage where error_per>1")
    result1 = c.fetchall()
    print("\nDays that lead to error requests more than 1 percent")
    for i in range(len(result1)):
        date = result1[i][0]
        error_p = result1[i][1]
        print(str(date)+" - "+str(error_p)+"%")
    db.close()


query1()
query2()
query3()
