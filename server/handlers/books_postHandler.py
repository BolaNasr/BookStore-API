# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request
import sqlite3


def books_postHandler():
    connection = sqlite3.connect("BookStore")
    cursor=connection.cursor()
    inputs = request.get_json()
    cursor.execute("CREATE TABLE IF NOT EXISTS BookStore (BookId INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,subTitle TEXT,authors TEXT)")
    cursor.execute("INSERT INTO BookStore VALUES(NULL,?,?,?)", (inputs["title"],inputs["subTitle"],inputs["authors"]))
    connection.commit()
    connection.close()
    return jsonify("successfully")
