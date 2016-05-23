#!/usr/bin/env python2
# Found on http://www.dreamsyssoft.com/python-scripting-tutorial/create-simple-rest-web-service-with-python.php
import web
import json
import psycopg2
import uuid

urls = (
    '/db/(.*)', 'REST_db',
)

class REST_db:

    sessions = {}

    def GET(self, sub):
        sub=sub.split('/')
        i=web.input()
        if sub[0] == 'session':
            if sub[1] == 'open':
                s = db_session(i)
                self.sessions[s.ID] = s
                ret = s.ID
            elif sub[1] == 'close':
                del self.sessions[i.sid]
                ret = i.sid
        else:
            try:
                s = self.sessions[i.gid]
                methodToCall = getattr(s, sub[0])
                ret=methodToCall(sub[1:], i)
            except Exception as e:
                print(e)
                raise web.notfound()
                return ""
        web.header('Content-Type', 'application/json')
        return json.dumps(ret)

    def POST(self, sub):
        web.header('Content-Type', 'application/json')
        return json.dumps(tables)

class db_session():

    def __init__(self, i):
        self.cn = psycopg2.connect("host='localhost' dbname='{0}'".format(i.db))
        self.transactions = []
        self.ID = str(uuid.uuid4())
        self.gid = i.gid

    def __del__(self):
        self.cn.rollback()
        self.cn.close()

    def tables(self, sub, i):
        cur=self.cn.cursor()
        tables=[]
        cur.execute('select schemaname, tablename from pg_tables')
        for r in cur:
            t={}
            t['schema'] = r[0]
            t['table'] = r[1]
            tables.append(t)
        return tables

    def transaction(self, sub, i):
        if sub[0] == 'begin':
            mySessionID = i.sid
            mytransID = str(uuid.uuid4())
            mySession = mySessions[i.session]
            mySession[transactions] += mytransID
        elif sub[0] == 'commit':
            mytransID = i.tid
        return mytransID

    def query_execute(self, sub, i):
        if sub[0] == 'execute':
            ret={}
            ret['sid'] = 3
            ret['tid'] = 2
        elif sub[0] == 'get':
            cur=self.cn.cursor()
            cur.execute('select * from '+table)
            ret=[]
            for r in cur:
                ret.append(r)
        elif sub[0] == 'num':
            ret={}
            ret['sid'] = 3
            ret['tid'] = 2
        return ret

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
