# -*- coding: utf-8 -*- 
# @Time : 11/20/2022 1:30 PM 
# @Author : Harshith Roopa Manjunath, CWID: 20005252
# @File : GEDCOMExtract.py 
# @Description : Extract information from output.txt and Class definition

import time
import datetime

month_dict = {
    "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9,
    "OCT": 10, "NOV": 11, "DEC": 12
}

def Caltime(date1, date2):
    # input should be year-month-day
    # date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
    # date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return (date2 - date1).days


def isADayBeforeBDay(Data_A, Date_B):
    """
    Compare 2 dates, to see if A is before B
    :param Data_A: format should be [day, month, year], all are integers
    :param Date_B: same as above
    :return: whether A is before B
    """
    if not isDateValid(Data_A):
        print("Date A is invalid!")
        return False
    if not isDateValid(Date_B):
        print("Date B is invalid!")
        return False
    if Data_A[2] > Date_B[2]:
        return False
    if Data_A[2] == Date_B[2]:  # if 2 dates in same year
        if Data_A[1] > Date_B[1]:
            return False
    if Data_A[1] == Date_B[1]:  # if 2 date in same month
        if Data_A[0] > Date_B[0]:
            return False
    return True


def convertDate(date: str):
    # The input is Year-Month-Day
    if date == 'NA' or date == 'Y':
        return date
    else:
        temp = date.split(' ')
        if temp[0] == "about":  # about 1998-2-3
            without_abt = temp[1].split('-')
            output = []
            for str in without_abt:
                output.append(int(str))
            return output[::-1]
        else:
            return list(map(int, temp[0].split('-')))[::-1]
    # The output is Day-Month-Year


def isDateValid(date):
    if date == 'NA':
        return False
    else:
        return True

class Person:
    def __init__(self, IID: str, FID: str, first_name: str, last_name: str, age: int, birth_date: str, marry_date: str, divorce_date: str, death_date: str):
        self.IID = IID
        self.FID = FID
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        # format: day-month-year
        self.birth_date = convertDate(birth_date)
        self.marry_date = convertDate(marry_date)
        self.divorce_date = convertDate(divorce_date)
        self.death_date = convertDate(death_date)

    def showInfo(self):
        print("------------------------")
        print('IID: ' + self.IID)
        print('FID: ' + self.FID)
        print(self.first_name + '.' + self.last_name)
        print('birth date: ' + '-'.join([str(i) for i in self.birth_date]))
        print('marry date: ' + '-'.join([str(i) for i in self.marry_date]))
        print('divorce date: ' + '-'.join([str(i) for i in self.divorce_date]))
        print('death date: ' + '-'.join([str(i) for i in self.death_date]))

    def isBirthBeforeMarry(self):
        """
        Written by NM
        :return:
        """
        return isADayBeforeBDay(self.birth_date, self.marry_date)
    
    def isBirthBeforeDeath(self):
        """
        Written by NM
        :return:
        """
        return isADayBeforeBDay(self.birth_date, self.death_date)

    def isMarryBeforeDeath(self):
        """
        Written by KR
        :return:
        """
        return isADayBeforeBDay(self.marry_date, self.death_date)

    def isDivorceBeforeDeath(self):
        """
        Written by KR
        :return:
        """
        return isADayBeforeBDay(self.divorce_date, self.death_date)
    
    def isMarryBeforeDivorce(self):
        """
        Written by SK
        :return:
        """
        return isADayBeforeBDay(self.marry_date, self.divorce_date)

    def isDatesBeforeCurrent(self):
        """
        Written by HRM
        :return:
        """
        return isADayBeforeBDay(self.birth_date, convertDate(datetime.datetime.now().strftime('%Y-%m-%d')))


    # def BirthBeforeDeath(self):
    #     """
    #     Written by NM - Planning
    #     :return:
    #     """
    #     if self.birth_date[2] > self.death_date[2]:
    #         return False
    #     if self.birth_date[2] == self.death_date[2]:  # if 2 dates in same year
    #         if self.birth_date[1] > self.death_date[1]:
    #             return False
    #     if self.birth_date[1] == self.death_date[1]:  # if 2 date in same month
    #         if self.birth_date[0] > self.death_date[0]:
    #             return False
    #     return True

    # def MarryBeforeDeath(self):
    #     """
    #     Written by KR - Planning
    #     :return:
    #     """
    #     if self.marry_date[2] > self.death_date[2]:
    #         return False
    #     if self.marry_date[2] == self.death_date[2]:  # if 2 dates in same year
    #         if self.marry_date[1] > self.death_date[1]:
    #             return False
    #     if self.marry_date[1] == self.death_date[1]:
    #         if self.marry_date[0] > self.death_date[0]:
    #             return False
    #     return True

    def isLessThan150YearOld(self):
        """
        Written by HRM - Done
        :return:
        """
        return True if self.age < 150 else False
        # return True if self.age < 150 else False
        # after refactor, the age calculation is written as a function, and redundant variables are removed

class Family:
    def __init__(self, FID: str, marry_date: str, divorce_date: str, husband_id: str,
                 husband_name: str, wife_id: str, wife_name: str, children: list):
        self.FID = FID
        self.husband_id = husband_id
        self.husband_name = husband_name
        self.wife_id = wife_id
        self.wife_name = wife_name
        self.children = children
        self.marry_date = convertDate(marry_date)
        self.divorce_date = convertDate(divorce_date)

    def showInfo(self):
        print("------------------------")
        print('FID: ' + self.FID)
        print('marry date: ' + '-'.join([str(i) for i in self.marry_date]))
        print('divorce date: ' + '-'.join([str(i) for i in self.divorce_date]))
        print('husband ID: ' + self.husband_id)
        print('husband name: ' + self.husband_name)
        print('wife ID: ' + self.wife_id)
        print('wife name: ' + self.wife_name)
        print('children_ids: ' + str(self.children))