# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request
import sqlite3

def books_byBookId_putHandler(bookId):
    connection = sqlite3.connect("BookStore")
    cursor=connection.cursor()
    inputs = request.get_json()
    cursor.execute("CREATE TABLE IF NOT EXISTS BookStore (BookId INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,subTitle TEXT,authors TEXT)")
    cursor.execute("UPDATE BookStore SET title = ?, subTitle = ?, authors = ? WHERE BookId = ?", (inputs["title"],inputs["subTitle"],inputs["authors"],bookId))
    row=cursor.rowcount
    if row==0:
        connection.commit()
        connection.close()
        return jsonify("Unable to update book check Book ID."),404
    connection.commit()
    connection.close()
    return jsonify("successfully")
