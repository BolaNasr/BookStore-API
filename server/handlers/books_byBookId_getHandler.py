# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request
import sqlite3

def books_byBookId_getHandler(bookId):
    connection = sqlite3.connect("BookStore")
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS BookStore (BookId INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,subTitle TEXT,authors TEXT)")
    cursor.execute("SELECT * FROM BookStore WHERE BookId = ?",(bookId))
    data=cursor.fetchall()
    if len(data)==0:
        connection.commit()
        connection.close()
        return jsonify("Unable to find book check Book ID."),404
    item=[]
    for row in data:
        item.append({'BookId':row[0],'title':row[1],'subTitle':row[2],'authors':row[3]})
    connection.commit()
    connection.close()
    return jsonify(item)
