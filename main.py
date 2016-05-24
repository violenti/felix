#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from census import water;
import sqlite3 as dbapi



pawsdb= dbapi.connect("paws.dat") #init db

cursor= pawsdb.cursor()

cursor.execute("""create table if not exists water(level text, date text, time text)""")

valu= water(0)
level=str(valu)

cursor.execute("""insert  into water (level) values('?'),[str(level,)]""")
pawsdb.commit()

