# -*- coding: utf-8 -*-

import pandas as pd


class GenerateCSV:
    def __init__(self, account_list, csv_full_name):
        self.account_list = account_list
        self.csv_full_name = csv_full_name

    def save_csv(self):
        df = pd.DataFrame({
            '英文称谓': '',
            '名': [i['FirstName'] for i in self.account_list],
            '中间名': '',
            '姓': [i['LastName'] for i in self.account_list],
            '中文称谓': [i['UserTName'] for i in self.account_list],
            '单位': [i['WorkCompanyName'] for i in self.account_list],
            '部门': [i['WorkGroupName'] for i in self.account_list],
            '职务': [i['UserZW'] for i in self.account_list],
            '商务电话': [i['UserTel'] for i in self.account_list],
            '移动电话': [i['UserMobile'] for i in self.account_list],
            '电子邮件地址': [i['UserEmail'] for i in self.account_list],
            '电子邮件类型': [i['EmailType'] for i in self.account_list],
            '电子邮件显示名称': [i['Email_Display_Name'] for i in self.account_list],
            '纪念日': '',
            '敏感度': [i['sensitivity'] for i in self.account_list],
            '身份证编号': '',
            '生日': '',
            '私有': [i['private'] for i in self.account_list],
            '性别': [i['UserSex'] for i in self.account_list],
            '优先级': [i['priority'] for i in self.account_list]
        })
        df.to_csv(path_or_buf=self.csv_full_name, index=False, sep=',')
