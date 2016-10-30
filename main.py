#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from census import water;
import sqlite3 as dbapi
import time,datetime



def base():

    pawsdb= dbapi.connect("paws.dat") #init db
    cursor= pawsdb.cursor()
    cursor.execute("""create table if not exists water(value text, date text, petId text)""")
    return 0

base()

while base() == 0:
    pawsdb= dbapi.connect("paws.dat") #init db
    cursor= pawsdb.cursor()
    valu= water(0) #import water from census, create test diff to 0
    value=str(valu)
    print(value)
    Date=datetime.datetime.now().isoformat()
    Pet='56596fe86154f0f0746ca456' #this value is hardcode, have to get of a table
    cursor.execute("insert  into water (level) values(?),(value,),(date) values(?),(Date,),(petId) values(?),(Pet,)")
    pawsdb.commit()
    time.sleep(60)#stop 60 seconds
