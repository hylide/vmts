# -*- coding: utf-8 -*-

from sqlobject import *
from config import config

def mysql_init():
    host = config.mysql.host
    port = config.mysql.port
    pwd = config.mysql.pwd

    sqlhub.processConnection = connectionForURI('mysql://{user}:{pwd}@{host}:{port}/vmts'.format(user='root', pwd=pwd, host=host, port=port))

def table_isExist(table_obj, createWhenNone = True):
    if table_obj.tableExists():
        return True
    else:
        if createWhenNone:
            table_obj.createTable()
        return False


class User(SQLObject):
    ''''''

    user = StringCol(length=120, notNone=True, unique=True)
    passwd = StringCol(length=120)
    description = StringCol(length=20)
    email = StringCol(length=120)
    last_login = DateTimeCol()

class TestSuit(SQLObject):
    ''''''

    suit_name = StringCol(length=100, notNone=True)
    case_id = IntCol(length=100, notNone=True, unique=True)
    overview = StringCol(length=255, notNone=True)
    target = StringCol(length=255, notNone=True)
    status = StringCol(length=25)
    detail = BLOBCol()

class Device(SQLObject):
    ''''''

    dev_id = StringCol(length=120, notNone=True, unique=True)
    dev_ip = StringCol(length=120, notNone=True)
    status = StringCol(length=30)
    static_info = BLOBCol()
    dynamic_period_info = BLOBCol()



if __name__ == '__main__':
    mysql_init()
    print table_isExist(User)
    print table_isExist(TestSuit)
    print table_isExist(Device)