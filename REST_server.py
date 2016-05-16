#!/usr/bin/env python2
# Found on http://www.dreamsyssoft.com/python-scripting-tutorial/create-simple-rest-web-service-with-python.php
import web
import json
import psycopg2

urls = (
    '/tables', 'list_tables',
    '/tables/(.*)', 'get_table',
)

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
        web.header('Content-Type', 'application/json')
        return json.dumps(tables)

class get_table:
    def GET(self, table):
        c=psycopg2.connect("host='localhost' dbname='sabes'")
        cur=c.cursor()
        cur.execute('select * from '+table)
        table=[]
        for r in cur:
            table.append(r)
        web.header('Content-Type', 'application/json')
        return json.dumps(table)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
