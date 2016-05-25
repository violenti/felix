#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from census import water;
import sqlite3 as dbapi
import time



def base():

    pawsdb= dbapi.connect("paws.dat") #init db
    cursor= pawsdb.cursor()
    cursor.execute("""create table if not exists water(level text, date text, time text)""")
    return 0

base()
pawsdb= dbapi.connect("paws.dat") #init db
cursor= pawsdb.cursor()
while base() == 0:
    valu= water(0) #import water from census
    nivel=str(valu)
    cursor.execute('''insert  into water (level) values(?)''',(nivel,))
    pawsdb.commit()
    time.sleep(60)#stop 60 seconds
