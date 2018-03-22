# -*- coding: utf-8 -*-

import sys
from mssql import MSSQL
from utils import list_clean, list_handle
from CSV import GenerateCSV
from getargs import get_args


def main(args_dict):
    sql = """
    SELECT
        ul.UserTName,
        ul.UserTel,
        ul.UserMobile,
        ul.UserEmail,
        ul.UserZW,
        ul.UserSex,
        ul.UserAddress,
        wg.WorkGroupName,
        (SELECT dbo.GetTopWorkGroupName(wgul.WorkGroupId)) AS WorkCompanyName
    FROM
        UserList ul
    LEFT JOIN WorkGroupUserList wgul ON ul.UserId = wgul.UserNo
    LEFT JOIN WorkGroup wg ON wg.WorkGroupId = wgul.WorkGroupId
    """
    ms = MSSQL(args_dict)
    account_list = ms.ExecQuery(sql)
    account_list = list_clean(account_list)
    list_handle(account_list)
    csv = GenerateCSV(account_list=account_list, csv_full_name=args_dict['path'])
    csv.save_csv()


if __name__ == '__main__':
    main(get_args(sys.argv[1:]))
