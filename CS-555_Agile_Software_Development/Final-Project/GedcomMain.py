# -*- coding: utf-8 -*- 
# @Time : 11/29/2022 1:51 AM 
# @Author : Roopa Manjunath Harshith, CWID: 20005252
# @File : GedcomMain.py
# @Description : Import GedcomMain in GEDCOMTest
import time
from typing import List

# import GedcomProcess as ged
from GEDCOMExtract import Person
from GEDCOMExtract import Family
import GEDCOMExtract as Extract


def isBirthAfterParentsDeath(individual_list: List[Person], family_list: List[Family]):
    """
    Written by NM
    """
    flag = 0
    for family in family_list:
        husband_death = ''
        wife_death = ''
        children_birth_date = []
        for individual in individual_list:  # find husband_death and wife_death by matching ID
            if family.husband_id == individual.IID:
                husband_death = individual.death_date
                continue
            if family.wife_id == individual.IID:
                wife_death = individual.death_date
        for child_id in family.children:  # find children's birth date by matching ID
            for individual in individual_list:
                if child_id == individual.IID:
                    children_birth_date.append(individual.birth_date)
        if husband_death == 'NA' and wife_death == 'NA':
            # if parents are both alive, definitely no such problem
            return False
        if husband_death != 'NA':
            husband_death[1] += 9
            if husband_death[1] > 12:
                husband_death[1] -= 12
                husband_death[2] += 1
            for i in range(len(children_birth_date)):
                if Extract.isADayBeforeBDay(husband_death, children_birth_date[i]):
                    print("Individual " + family.children[i] +
                          " 's birthday is even late than 9 months after his/her father " + family.husband_id +
                          "'s death date!")
                    flag = 1
        if wife_death != 'NA':
            for i in range(len(children_birth_date)):
                if Extract.isADayBeforeBDay(wife_death, children_birth_date[i]):
                    print("Individual " + family.children[i] +
                          " 's birthday is after his/her mother " + family.wife_id + "'s death date!")
                    flag = 1
    if flag == 0:
        return False
    else:
        return True


def isBirthAfterParentsMarriage(individual_list: List[Person], family_list: List[Family]):
    """
    Written by NM
    """
    flag = 0
    for family in family_list:
        husband_marr = ''
        wife_marr = ''
        children_birth_date = []
        for individual in individual_list:  # find husband_marr and wife_marr by matching ID
            if family.husband_id == individual.IID:
                husband_marr = individual.marry_date
                continue
            if family.wife_id == individual.IID:
                wife_marr = individual.marry_date
        for child_id in family.children:  # find children's birth date by matching ID
            for individual in individual_list:
                if child_id == individual.IID:
                    children_birth_date.append(individual.birth_date)
        if husband_marr == 'NA' and wife_marr == 'NA':
            # if parents are both alive, definitely no such problem
            return False

        for i in range(len(children_birth_date)):
            if Extract.isADayBeforeBDay(husband_marr, children_birth_date[i]):
                print("Individual " + family.children[i] +
                      " 's birthday is later than his/her father " + family.husband_id +
                      "'s marriage date!")
                flag = 1
        if wife_marr != 'NA':
            for i in range(len(children_birth_date)):
                if Extract.isADayBeforeBDay(wife_marr, children_birth_date[i]):
                    print("Individual " + family.children[i] +
                          " 's birthday is later than his/her mother " + family.wife_id + "'s marriage date!")
                    flag = 1
    if flag == 0:
        return False
    else:
        return True


def isMarriageAfter14(individual_list: List[Person], family_list: List[Family]):
    """
    Written by KR
    """
    flag = 0
    for family in family_list:
        husband_birth = []
        husband_marr = []
        wife_birth = []
        wife_marr = []
        for individual in individual_list:  # find husband_marr and wife_marr by matching ID
            if family.husband_id == individual.IID:
                husband_marr = individual.marry_date
                husband_birth = individual.birth_date
                continue
            if family.wife_id == individual.IID:
                wife_marr = individual.marry_date
                wife_birth = individual.birth_date
        if husband_marr == 'NA' and wife_marr == 'NA' and husband_birth == 'NA' and wife_birth == 'NA':
            return False
        else:
            if husband_marr[2] - husband_birth[2] < 14:
                print(family.husband_id + ' got marriage before he was 14 years old.')
                flag = 1
            else:
                print(family.husband_id + ' got marriage after he was 14 years old.')
            if wife_marr[2] - wife_birth[2] < 14:
                print(family.wife_id + ' got marriage before she was 14 years old.')
                flag = 1
            else:
                print(family.wife_id + ' got marriage after she was 14 years old.')

    if flag == 0:
        return False
    else:
        return True


def isParentsNotTooOld(individual_list: List[Person], family_list: List[Family]):
    """
    Written by SK
    """
    flag = 0
    for family in family_list:
        husband_birth = ''
        wife_birth = ''
        children_birth_date = []
        for individual in individual_list:  # find husband_death and wife_death by matching ID
            if family.husband_id == individual.IID:
                husband_birth = individual.birth_date
                husband_birth[2] += 80
                continue
            if family.wife_id == individual.IID:
                wife_birth = individual.birth_date
                wife_birth[2] += 60
                # change the original data
        for child_id in family.children:  # find children's birth date by matching ID
            for individual in individual_list:
                if child_id == individual.IID:
                    children_birth_date.append(individual.birth_date)
        for i in range(len(children_birth_date)):
            if Extract.isADayBeforeBDay(children_birth_date[i], husband_birth) and Extract.isADayBeforeBDay(
                    children_birth_date[i], wife_birth):
                print("success")
                flag = 1
            else:
                print("error")
                print(husband_birth)
                print(wife_birth)
                flag = 0
        if flag == 1:
            return True
        else:
            return False


def isThereBigamy(family_list: List[Family]):
    """
    Written by SK
    """
    flag = 0
    temp = {}
    for family in family_list:
        if family.husband_id not in temp:
            temp[family.husband_id] = [family]
        else:
            temp[family.husband_id].append(family)
    suspect = []
    for i in temp.keys():
        if len(temp[i]) > 1:
            suspect.append(temp[i])
    if len(suspect) == 0:
        print("Husbands are well")
        flag = 0
    for FWSH in suspect:  # Families With Same Husband
        FWSH = bubbleSort(FWSH)
        for i in range(0, len(FWSH) - 1):
            if Extract.isADayBeforeBDay(FWSH[i].divorce_date,
                                            FWSH[i + 1].marry_date) and FWSH[i].divorce_date != 'NA':
                flag = 0
            else:
                print(FWSH[i].husband_id + " conducts a Bigamy!! So Shameless!")
                flag = 1
    temp = {}
    for family in family_list:
        if family.wife_id not in temp:
            temp[family.wife_id] = [family]
        else:
            temp[family.wife_id].append(family)
    suspect = []
    for i in temp.keys():
        if len(temp[i]) > 1:
            suspect.append(temp[i])
    if len(suspect) == 0:
        print("Wives are well")
        return False
    for FWSW in suspect:  # Families With Same Wife
        FWSW = bubbleSort(FWSW)
        for i in range(0, len(FWSW) - 1):
            if Extract.isADayBeforeBDay(FWSW[i].divorce_date,
                                            FWSW[i + 1].marry_date) and FWSW[i].divorce_date != 'NA':
                flag = 0
            else:
                print(FWSW[i].wife_id + " conducts a Bigamy!! So Shameless!")
                flag = 1
    if flag == 0:
        print("All is well!")
        return False
    else:
        return True

def bubbleSort(arr: List[Family]):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if not Extract.isADayBeforeBDay(arr[j].marry_date, arr[j + 1].marry_date):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSort2(arr: list):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if not Extract.isADayBeforeBDay(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == '__main__':
    original_ged_file_path = "Black-Family.ged"
    preprocessed_file_path = "PreprocessedOutput.txt"
