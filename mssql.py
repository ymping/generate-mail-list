# -*- coding: utf-8 -*-

import pymssql


class MSSQL:
    def __init__(self, args_dict):
        self.host = args_dict['host']
        self.user = args_dict['user']
        self.password = args_dict['password']
        self.database = args_dict['database']
        self.charset = "UTF-8"

    def __GetCursor(self):
        self.conn = pymssql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database,
                                    charset=self.charset)
        return self.conn.cursor(as_dict=True)

    def ExecQuery(self, sql):
        cursor = self.__GetCursor()
        try:
            cursor.execute(sql)
        finally:
            ResultList = cursor.fetchall()
            self.conn.close()
        return ResultList
