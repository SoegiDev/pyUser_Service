import uuid
import datetime
import os
import psycopg2
from psycopg2.extensions import STATUS_BEGIN, STATUS_READY,STATUS_ASYNC,STATUS_SETUP,STATUS_PREPARED,STATUS_SYNC
class db():
    HOST = None
    DATABASE = None
    USER = None
    PASSWORD =None
    PORT = None
    conn = None
    cursor = None
    status = None
    message = None
    closed = 1
    def __init__(self, app):
        env = app.config.get('ENV_VALUE')
        print(env)
        self.HOST = app.config.get('HOST')
        self.DATABASE = app.config.get('DB')
        self.USER = app.config.get('USER')
        self.PASSWORD = app.config.get('PWD')
        self.PORT = app.config.get('PORT')
    def ConnectionToDB(self):
        try:
            conn = psycopg2.connect(host=self.HOST,
                                    database=self.DATABASE,
                                    user=self.USER,
                                    password=self.PASSWORD,
                                    port = self.PORT)
            cursor = conn.cursor()
            status = 1
            # print({"Hasil":True,"conn":conn,"cursor":cursor}) 
            if conn.status == STATUS_SETUP:
                print({"status":STATUS_SETUP,"message":"A connection Setup"})
                self.status = STATUS_SETUP
                self.message = "A connection Setup"
            elif conn.status == STATUS_READY:
                print({"status":STATUS_READY,"message":"A connection Ready"})
                self.status = STATUS_READY
                self.message = "A connection Ready"
            elif conn.status == STATUS_BEGIN:
                print({"status":STATUS_BEGIN,"message":"A connection BEGIN"})
                self.status = STATUS_BEGIN
                self.message = "A connection Begin"
            elif conn.status == STATUS_SYNC:
                print({"status":STATUS_SYNC,"message":"A connection SYNC"})
                self.status = STATUS_SYNC
                self.message = "A connection Sync"
            elif conn.status == STATUS_ASYNC:
                print({"status":STATUS_ASYNC,"message":"A connection ASYNC"})
                self.status = STATUS_ASYNC
                self.message = "A connection Async"
            elif conn.status == STATUS_PREPARED:
                print({"status":STATUS_PREPARED,"message":"A connection PREPARED"})
                self.status = STATUS_PREPARED
                self.message = "A connection Prepared"
            self.conn = conn
            self.cursor = cursor
            self.closed = conn.closed
            return self.status,self.closed,self.message
        except (Exception, psycopg2.DatabaseError) as error:
            self.status = -1
            self.closed = 1
            self.message = error
            return self.status,self.closed,self.message
            
    def connect(self):
        return self.conn,self.cursor,self.closed,self.status,self.message
    
    def closeConnection(self):
        self.conn.close()
        self.closed = self.conn.closed
        return self.conn,self.closed