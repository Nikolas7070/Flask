import mysql.connector
import sqlite3


class MYSQL:
    def __init__(self):
        self.__connect = mysql.connector.connect(host="localhost", user="root", password="0000")
        self.__cursor = self.__connect.cursor()

    def get_all_skills(self):
        self.__cursor.execute("SELECT * FROM TheNikolas.skills_emp")
        return self.__cursor.fetchall()

    """
    This realisation was rejected because of platform realisation
    """


class SQLite:
    def __init__(self):
        self.__connect = sqlite3.connect("../refactor v1/data_base.db")
        self.__cursor = self.__connect.cursor()
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS cv(f_name,s_name,position,address,phone,mail)""")
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS skills(skill,points)""")
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS skills_emp(skill_id,skil_name)""")

    def get_all_skills_emp(self):
        self.__cursor.execute("SELECT * FROM skills_emp")
        return self.__cursor.fetchall()

    def get_all_cv(self):
        self.__cursor.execute("SELECT * FROM cv")
        return self.__cursor.fetchall()

    def get_all_skills(self):
        self.__cursor.execute("SELECT * FROM skills")
        return self.__cursor.fetchall()


class Interface:
    info_w = SQLite().get_all_cv()
    skills = SQLite().get_all_skills()
    data = SQLite().get_all_skills_emp()

    @staticmethod
    def skills_func(number):
        return "●" * number + "○" * (5 - number)

    @staticmethod
    def add_void(text):
        return " " * (40 - text.__len__())





