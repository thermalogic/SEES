# -*- coding: utf-8 -*-

import redis
from datetime import *

conn = redis.Redis('localhost')

def TagDefToRedisHashKey(tagdeflist):
    pipe = conn.pipeline()
    for element in tagdeflist:
        pipe.hmset(
            element['id'], {'desc': element['desc'], 'value': "-10000", 'ts': ""})
    pipe.execute()


def TagDefFromRedisHash(tagdeflist):
    taglist = []
    for element in tagdeflist:
        htag = conn.hgetall(element['id'])
        taglist.append(htag)
    return taglist


def SendToRedisHash(tagvaluelist):
    pipe = conn.pipeline()

    curtime = datetime.now()

    for element in tagvaluelist:
        pipe.hmset(element['id'], {'value': element['value'], 'ts': curtime})
    pipe.execute()

def tagvalue_redis(taglist):
        #        for i in range(self.tagcount):
        #            self.taglist[i]['value']= conn.hget(self.taglist[i]['name'],'value').decode()
        tagcount=len(taglist)
        pipe = conn.pipeline()
        for i in range(tagcount):
            pipe.hmget(taglist[i]['id'], 'value', 'ts')
        tagvaluelist = pipe.execute()

        for i in range(tagcount):
            taglist[i]['value'] = tagvaluelist[i][0].decode()
            taglist[i]['ts'] = tagvaluelist[i][1].decode()



