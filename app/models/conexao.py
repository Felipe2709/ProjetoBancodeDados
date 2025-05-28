import sqlite3
import os


def criar_conexao():
    conn = sqlite3.connect('academia.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn