# -*- coding: utf-8 -*- 
# @Time : 11/29/2022 1:51 AM 
# @Author : Roopa Manjunath Harshith, CWID: 20005252
# @File : GedcomMain.py
# @Description : Import GedcomMain in GEDCOMTest
import time
from typing import List

import GedcomProcess as ged
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

'''
Sprint 3
Form Sprint 2 and 3 onwards merge the stories to the 
GedcomMain file
'''
def isSiblingsLessThan15(family_list: List[Family]):
    """
    Written by KR
    :return:
    """
    flag = 1
    for family in family_list:
        if len(family.children) >= 15:
            print("There's 15 or more siblings in " + str(family.FID) + " family!")
            flag = 0
    if flag == 1:
        print("All families have less than 15 siblings.")
        return True
    else:
        return False

def isThereDuplicateNameAndBirthDate(individual_list: List[Person]):
    """
    Written by HRM
    :return:
    """
    person_dict = {}
    for individual in individual_list:
        full_name = individual.first_name + '/' + individual.last_name
        id = individual.IID
        if full_name not in person_dict:
            person_dict[full_name] = [individual.birth_date, id]
        else:
            if person_dict[full_name][0][0] == individual.birth_date[0] and \
                    person_dict[full_name][0][1] == individual.birth_date[1] \
                    and person_dict[full_name][0][2] == individual.birth_date[2]:
                print(str(person_dict[full_name][1]) + " and " +
                      str(individual.IID) +
                      " have same name and birth date!")
            return True  # If there's problem
    print("There's no people with same name and birth date!")
    return False

def isUniqueIDs(individual_list: List[Person], family_list: List[Family]):
    """
    Written by SK
    """
    flag1 = 0
    flag2 = 0
    temp1 = {}
    temp2 = {}
    for family in family_list:
        if family.FID not in temp1:
            temp1[family.FID] = [family]
        else:
            temp1[family.FID].append(family)
    for i in temp1.keys():
        if len(temp1[i]) > 1:
            flag1 = 0
        else:
            flag1 = 1
    for individual in individual_list:
        if individual.IID not in temp2:
            temp2[individual.IID] = [individual]
        else:
            temp2[individual.IID].append(individual)
    for i in temp2.keys():
        if len(temp2[i]) > 1:
            flag2 = 0
        else:
            flag2 = 1
    if flag1 == 1 and flag2 == 1:
        print("All is Unique!")
        return True
    else:
        return False

def SiblingsSpacing(individual_list: List[Person], family_list: List[Family]):
    """
    Written by NM
    """
    flag = 0
    for family in family_list:
        children_birth_date = []
        for child_id in family.children:  # find children's birth date by matching ID
            for individual in individual_list:
                if child_id == individual.IID:
                    children_birth_date.append(individual.birth_date)
        children_birth_date = bubbleSort2(children_birth_date)
        children_birth_date_str = []
        for date in children_birth_date:
            temp = []
            for i in range(len(date)):
                temp.append(str(date[i]))
            children_birth_date_str.append(temp)
        for i in range(len(children_birth_date_str) - 1):
            date1 = '-'.join(children_birth_date_str[i][::-1])
            date2 = '-'.join(children_birth_date_str[i + 1][::-1])
            timeSub = Extract.Caltime(date1, date2)
            if timeSub < 2 or timeSub > 240:
                print("It is spacing")
                print(timeSub)
                flag = 1
            else:
                print("Siblings spacing is not valid.")
                print(timeSub)
                flag = 0
    if flag == 1:
        return True
    else:
        return False

def multiple_birth(family_list: List[Family]):
    """
    Written by KR
    """
    for i in family_list:
        if len(i.children) < 5:
            print(i.FID + ' don\'t meet the requirement.')
    return True

def list_deceased_individual(individual_list: List[Person]):
    """
    Written by SK
    """
    for person in individual_list:
        if person.death_date != 'NA':
            print(person.IID)
    return True

'''
Sprint 4
'''
def getRecentBirths(individual_list: List[Person]):
    """
    Written by NM
    """
    present_date = time.strftime("%Y-%m-%d", time.localtime())
    # present_date is day-month-year
    output = []
    for person in individual_list:
        temp_date = []
        for num in person.birth_date:
            temp_date.append(str(num))
        if Extract.Caltime('-'.join(temp_date[::-1]), present_date) < 30:
            print("Birth in recent 30 days: " + person.IID)
            output.append(person)
    return output

def getRecentDeaths(individual_list: List[Person]):
    """
    Written by NM
    """
    present_date = time.strftime("%Y-%m-%d", time.localtime())
    # present_date is day-month-year
    output = []
    for person in individual_list:
        temp_date = []
        for num in person.death_date:
            temp_date.append(str(num))
        if temp_date[0] != 'N' and Extract.Caltime('-'.join(temp_date[::-1]), present_date) < 30:
            print("Death in recent 30 days: " + person.IID)
            output.append(person)
    return output

def list_living_single(individual_list: List[Person]):
    """
    Written by HRM
    """
    for person in individual_list:
        if person.death_date == 'NA' and person.marry_date == 'NA':
            print(person.IID)
    return True

def list_name_and_age(individual_list: List[Person]):
    """
    Written by HRM
    """
    for person in individual_list:
        print(person.first_name + ' ' +person.last_name + ' age: ' + str(person.age))
    return True

def listLivingMarried(individual_list: List[Person], family_list: List[Family]):
    """
    Written by KR
    """
    flag1 = 0   # judge if husband is alive
    flag2 = 0   # judge if wife is alive
    for family in family_list:
        husband_death = []
        wife_death = []
        for individual in individual_list:  # find husband_death and wife_death by matching ID
            if family.husband_id == individual.IID:
                husband_death.append(individual.death_date)
                for i in range(len(husband_death)):
                    if husband_death[i] == 'NA':
                        flag1 = 1
                continue
            if family.wife_id == individual.IID:
                wife_death.append(individual.death_date)
                for j in range(len(wife_death)):
                    if wife_death[j] == 'NA':
                        flag2 = 1
    if flag1 == 1 and flag2 == 1:
        # both requirements should be meeted
        print("\n-TestListLivingMarried-\nSome family's parents are survived:\n")
        family.showInfo()   #print living-married information
        return True
    else:
        print("\nLivingMarried error! Some people in families died\n")
        return False

def listOrphans(individual_list: List[Person], family_list: List[Family]):
    """
    Written by SK
    """
    flag1 = 0       # judge if parents are dead (dead: 1, alive: 0)
    flag2 = 0       # judge if children are younger than 18 (teenage: 1, adult: 0)
    for family in family_list:
        husband_death = ''
        wife_death = ''
        children_age = 0
        for individual in individual_list:  # find husband_death and wife_death by matching ID
            if family.husband_id == individual.IID:
                husband_death = individual.death_date
                continue
            if family.wife_id == individual.IID:
                wife_death = individual.death_date
            if husband_death != 'NA' and wife_death != 'NA':
                flag1 = 1
        for child_id in family.children:  # find children's age by matching ID
            for individual in individual_list:
                if child_id == individual.IID:
                    children_age = individual.age
                if children_age <= 18:      # judge if children are younger than 18 years old
                    flag2 = 1
        if flag1 == 1 and flag2 == 1:
            print('There is orphan!')
            family.showInfo()   #print orphan's information
            return True
        else:
            print('There is no orphan!')
            return False
       
if __name__ == '__main__':
    original_ged_file_path = "/home/harsh/Documents/Academics/CS 555 - Agile/Assignments/Project-10:Sprint4/Black-Family.ged"
    preprocessed_file_path = "PreprocessedOutput.txt"
    valid_records_path = "ValidRecords.txt"
    pretty_table_path = "/home/harsh/Documents/Academics/CS 555 - Agile/Assignments/Project-10:Sprint4/Table.txt"

    ged.getGEDCOM(original_ged_file_path, preprocessed_file_path)
    ged.getValidRecords(preprocessed_file_path, valid_records_path)
    indi_fami_dict_list = ged.getIndiFamiList(valid_records_path)
    ged.getTable(indi_fami_dict_list, pretty_table_path)

    individuals = ged.getIndividuals(indi_fami_dict_list)
    families = ged.getFamilies(indi_fami_dict_list)

    # for i in individuals:
    #     i.showInfo()
    # print("isBirthBeforeMarry: " + str(i.isBirthBeforeMarry()))
    # print("isBirthBeforeDeath: " + str(i.isBirthBeforeDeath()))
    # print("isMarryBeforeDeath: " + str(i.isMarryBeforeDeath()))
    # print("isDivorceBeforeDeath: " + str(i.isDivorceBeforeDeath()))
    # print("isMarryeBeforeDivorce: " + str(i.isMarryeBeforeDivorce()))
    # print("isDatesBeforeCurrent: " + str(i.isDatesBeforeCurrent()))
    # for i in families:
    #     i.showInfo()

    isBirthAfterParentsDeath(individuals, families)
    isParentsNotTooOld(individuals, families)
    isSiblingsLessThan15(families)
    isThereDuplicateNameAndBirthDate(individuals)
    isUniqueIDs(individuals, families)
    SiblingsSpacing(individuals, families)
    multiple_birth(families)
    list_deceased_individual(individuals)
    print("-----------------------------------")
    recent_births = getRecentBirths(individuals)
    for person in recent_births:
        person.showInfo()

    list_living_single(individuals)
    list_name_and_age(individuals)

    listLivingMarried(individuals, families)
    listOrphans(individuals, families)