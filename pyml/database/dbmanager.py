import psycopg2
from pyml.database.configmanager import config

class DbManager:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            params = config()
            self.connection = psycopg2.connect(**params)
            print("Connected to the PostgreSQL db.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        try:
            if self.connection is not None:
                self.connection.close()
                print("Disconnected from db.")
            else:
                print("Connection to db already closed.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def version(self):
        if self.connection is None:
            print("Connection to db is not open.")
            return None
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT version()")
            db_version = cursor.fetchone()
            return db_version
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cursor.close()

    def insert_author(self, author_name):
        if self.connection is None:
            print("Connection to db is not open.")
            return None
        sql = "INSERT INTO authors(name) VALUES(%s) RETURNING authorid;"
        authorid = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (author_name,))
            authorid = cursor.fetchone()[0]
            self.connection.commit()
            print("Inserted one row into authors table with value: " + author_name)
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return authorid

    def insert_author_list(self, author_list):
        if self.connection is None:
            print("Connection to db is not open.")
            return None
        sql = "INSERT INTO authors(name) VALUES(%s);"
        try:
            cursor = self.connection.cursor()
            cursor.executemany(sql, author_list)
            self.connection.commit()
            print("Inserted multiple rows into authors table.")
            cursor.close()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False

    def delete_author(self, author_id):
        if self.connection is None:
            print("Connection to db is not open.")
            return None
        sql = "DELETE FROM authors WHERE AuthorId = %s;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (author_id,))
            self.connection.commit()
            print("Deleted one row from authors table with id: " + str(author_id))
            cursor.close()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
