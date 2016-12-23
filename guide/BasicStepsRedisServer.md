
## Introduction to Redis

Redis is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker. 

The data model is **key-value**, but many different kind of values are support。

It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries. 

Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, 

and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.

http://redis.io/

https://github.com/antirez/redis

https://github.com/redis


## Installation On Windows

https://github.com/MSOpenTech/redis

You can download the latest unsigned binaries and the unsigned MSI installer from the release page.

https://github.com/MSOpenTech/redis/releases

**redis 3.0.501**

https://github.com/MSOpenTech/redis/releases/download/win-3.0.501/Redis-x64-3.0.501.msi

Run:

Redis-x64-3.0.501.msi

##  Installation on Linux

http://redis.io/download

### online install  Redis

```
$ sudo apt install redis-server
```

start redis server
```
$ redis-server
```

### Download, extract and compile Redis with:

```
$ wget http://download.redis.io/releases/redis-3.0.7.tar.gz
$ tar xzf redis-3.0.7.tar.gz
$ cd redis-3.0.7
$ make
```

The binaries that are now compiled are available in the src directory. Run Redis with: 
```
$ src/redis-server
```
You can interact with Redis using the built-in client:
```
$ src/redis-cli
redis> set foo bar
OK
redis> get foo
"bar"
```

## Redis Python Client 

https://github.com/andymccurdy/redis-py

##  Installation

redis-py requires a running Redis server. See Redis's quickstart for installation instructions.

To install redis-py, simply:

Windows
 
```
>pip install redis
```

Linux

```
$ sudo pip3 install redis
```
or
```
$ sudo apt install python3-redis
```
 
## Getting Started

```python
 import redis
 
 r = redis.StrictRedis(host='localhost', port=6379, db=0)
 r.set('foo', 'bar')
 r.get('foo')
```









