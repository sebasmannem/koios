#!/usr/bin/env python2
# Found on http://www.dreamsyssoft.com/python-scripting-tutorial/create-simple-rest-web-service-with-python.php
import web
import json
import psycopg2
import uuid

urls = (
    '/db/(.*)', 'REST_db',
)

mySessions = {}

class REST_db:
    def GET(self, sub):
        sub=sub.split('/')
        try:
            methodToCall = getattr(self, sub[0])
            ret=methodToCall(sub[1:])
        except Exception as e:
            print(e)
            raise web.notfound()
            return ""
        web.header('Content-Type', 'application/json')
        return json.dumps(ret)
    def POST(self, sub):
        web.header('Content-Type', 'application/json')
        return json.dumps(tables)
    def tables(self, sub):
        c=psycopg2.connect("host='localhost' dbname='sabes'")
        cur=c.cursor()
        tables=[]
        cur.execute('select schemaname, tablename from pg_tables')
        for r in cur:
            t={}
            t['schema'] = r[0]
            t['table'] = r[1]
            tables.append(t)
        return tables
    def session(self, sub):
        i=web.input()
        if sub[0] == 'open':
            mySessionID = str(uuid.uuid4())
            self.globalID = i.gid
            mySessions[mySessionID] = self
        elif sub[0] == 'close':
            mySessionID = i.UUID
            del mySessions[mySessionID]
        else:
            raise KeyError("Invalid REST call")
        return mySessionID

    def transaction(self, sub):
        i=web.input()
        if sub[0] == 'begin':
            mySessionID = i.sid
            mytransID = str(uuid.uuid4())
            mySession = mySessions[i.session]
            mySession[transactions] += mytransID
        elif sub[0] == 'commit':
            mytransID = i.tid
        return mytransID

    def query_execute(self, sub):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return ret

    def query_get(self, sub):
        c=psycopg2.connect("host='localhost' dbname='sabes'")
        cur=c.cursor()
        cur.execute('select * from '+table)
        table=[]
        for r in cur:
            table.append(r)
        web.header('Content-Type', 'application/json')
        return table

    def query_num(self, sub):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return ret


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
