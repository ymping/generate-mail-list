# -*- coding: utf-8 -*-

def list_clean(account_list):
    # remove space
    for d in account_list:
        for k in d:
            if isinstance(d[k], str):
                d[k] = d[k].strip()

    # filter "实验室" or "测试机" from list
    exp = lambda d: not (d['UserTName'].find('实验室') != -1 or d['UserTName'].find('测试机') != -1)
    return list(filter(exp, account_list))


def list_handle(account_list):
    for i in account_list:
        # generate first name and last name
        i['LastName'] = i['UserTName'][:1]
        i['FirstName'] = i['UserTName'][1:]

        # generate email type default SMTP
        i['EmailType'] = 'SMTP'

        # generate email display name
        i['Email_Display_Name'] = i['UserTName'] + ' ' + '(' + i['UserEmail'] + ')'

        # generate sensitivity
        i['sensitivity'] = '普通'

        # private or not
        i['private'] = 'FALSE'

        # generate priority
        i['priority'] = '中'

        # generate sex
        if i['UserSex'] == 1:
            i['UserSex'] = '男'
        elif i['UserSex'] == 2:
            i['UserSex'] = '女'
        else:
            i['UserSex'] = '未指定'
