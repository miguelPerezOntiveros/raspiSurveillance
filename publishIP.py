#!/usr/bin/python
import MySQLdb
import datetime
import time
import subprocess
import os
import secret
import sys

time.sleep(float(sys.argv[1]))

try:
	db = MySQLdb.connect(secret.host1, secret.user1, secret.pwd1, secret.db1)
except MySQLdb.Error:
	db = MySQLdb.connect(secret.host2, secret.user2, secret.pwd2, secret.db2)
	
p = os.popen("ifconfig wlan0 | grep -Po 't addr:\K[\d.]+'")
ip0 = p.read()
p.close()

p = os.popen("ifconfig wlan1 | grep -Po 't addr:\K[\d.]+'")
ip1 = p.read()
p.close()

now = str(datetime.datetime.now())
query = "insert into updates (data, datetime) values ('" + ip0 + ", " + ip1 + "', '" + now + "')"

cur = db.cursor()
cur.execute(query)
db.commit()
