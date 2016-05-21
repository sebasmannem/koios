#!/usr/bin/env python2
# Found on http://www.dreamsyssoft.com/python-scripting-tutorial/create-simple-rest-web-service-with-python.php
import web
import json
import psycopg2

urls = (
    '/tables', 'list_tables',

    '/session/start', 'session_start',
    '/transaction/begin', 'transaction_begin',

    '/query/execute', 'query_execute',
    '/query/getone', 'query_get_one_record',
    '/query/getall', 'query_get_all_records',
    '/query/rowcount', 'query_numrecords',

    '/transaction/commit', 'transaction_commit',
    '/transaction/rollback', 'transaction_rollback',
    '/session/close', 'session_close',
)

def return_json(myDict):
    web.header('Content-Type', 'application/json')
    return json.dumps(myDict)

class list_tables:
    def GET(self):
        c=psycopg2.connect("host='localhost' dbname='sabes'")
        cur=c.cursor()
        tables=[]
        cur.execute('select schemaname, tablename from pg_tables')
        for r in cur:
            t={}
            t['schema'] = r[0]
            t['table'] = r[1]
            tables.append(t)
        return return_json(tables)

class session_start:
    def GET(self):
        i=web.input()
        print(i.globalsession)
        ret={}
        ret['sid'] = 1
        return return_json(ret)

class transaction_begin:
    def GET(self):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return return_json(ret)

class query_execute:
    def GET(self):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return return_json(ret)

class query_get_one_record:
    def GET(self):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return return_json(ret)

class query_get_all_records:
    def GET(self, table):
        c=psycopg2.connect("host='localhost' dbname='sabes'")
        cur=c.cursor()
        cur.execute('select * from '+table)
        table=[]
        for r in cur:
            table.append(r)
        web.header('Content-Type', 'application/json')
        return return_json(table)

class query_numrecords:
    def GET(self):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return return_json(ret)

class transaction_commit:
    def GET(self):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return return_json(ret)

class session_close:
    def GET(self):
        ret={}
        ret['sid'] = 3
        ret['tid'] = 2
        return return_json(ret)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
