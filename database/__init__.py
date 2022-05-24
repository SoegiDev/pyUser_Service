"""module"""
import uuid
import datetime
import os
import psycopg2
from psycopg2.extensions import STATUS_BEGIN, STATUS_READY,STATUS_ASYNC,STATUS_SETUP,STATUS_PREPARED,STATUS_SYNC
class db:
    host = None
    database = None
    user = None
    password =None
    port = None
    conn = None
    cursor = None
    status = None
    message = None
    closed = 1
    def __init__(self, app):
        env = app.config.get('ENV_VALUE')
        print(env)
        self.host = app.config.get('HOST')
        self.database = app.config.get('DB')
        self.user = app.config.get('USER')
        self.password = app.config.get('PWD')
        self.port = app.config.get('PORT')
    def ConnectionToDB(self):
        try:
            conn = psycopg2.connect(host=self.host,
                                    database=self.database,
                                    user=self.user,
                                    password=self.password,
                                    port = self.port)
            cursor = conn.cursor()
            self.status = 1
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
        """DocString"""
        return self.conn,self.cursor,self.closed,self.status,self.message
    def closeConnection(self):
        self.conn.close()
        self.closed = self.conn.closed
        return self.conn,self.closed
        