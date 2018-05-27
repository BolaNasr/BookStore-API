# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request
import sqlite3

def books_byBookId_deleteHandler(bookId):
    connection = sqlite3.connect("BookStore")
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS BookStore (BookId INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,subTitle TEXT,authors TEXT)")
    cursor.execute("DELETE FROM BookStore WHERE BookId = ?", (bookId))
    row=cursor.rowcount
    if row==0:
        connection.commit()
        connection.close()
        return jsonify("Unable to delete book check Book ID."),404
    connection.commit()
    connection.close()
    return jsonify("successfully")
