#!/usr/bin/env python
# -*- coding: utf-8 -*-
#LoadSchema

import sqlite3


def main():
    conn = sqlite3.connect('cheese.db')
    f = open('schema.sql','r')
    sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
