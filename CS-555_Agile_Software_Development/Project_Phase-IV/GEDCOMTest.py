# -*- coding: utf-8 -*- 
# @Time : 11/20/2022 2:31 PM
# @Author : Harshith Roopa Manjunath, CWID: 20005252
# @File : GEDCOMTest.py
# @Description : Test the class and its functions in GEDCOMExtract

import unittest
import GEDCOMExtract as Extract
import GedcomMain

class TestExtract(unittest.TestCase):
    def testStoreBirthAndDeathDate(self):
        """
        Written by HRM
        :return:
        """
        person1 = Extract.Person("I13", "F4", "Sirius", "Black", 74, "1877-10-9", "1998-8-20", "2028-6-12",
                                     "1952-6-15") #Random date testing
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4",
                                     "2070-10-10") #Example gedcom
        self.assertEqual(person1.birth_date, [9, 10, 1877])
        self.assertEqual(person1.death_date, [15, 6, 1952])
        self.assertEqual(person2.birth_date, [5, 6, 1945])
        self.assertEqual(person2.death_date, [10, 10, 2070])
    
    def testBirthBeforeMarry(self):
        """
        Written by NM - Done
        :return:
        """
        person1 = Extract.Person("I13", "F4", "Sirius", "Black", 74, "1877-10-9", "1998-8-20", "2028-6-12",
                                     "1952-6-15")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "1900-3-25", "1950-5-4",
                                     "1925-10-10")
    
        self.assertTrue(person1.isBirthBeforeMarry())
        self.assertFalse(person2.isBirthBeforeMarry())
    
    def testBirthBeforeDeath(self):
        """
        Written by NM - Done
        :return:
        """
        person1 = Extract.Person("I13", "F4", "Sirius", "Black", 74, "1877-10-9", "1998-8-20", "2028-6-12",
                                     "1952-6-15")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4",
                                     "1900-10-10")
    
        self.assertTrue(person1.isBirthBeforeDeath())
        self.assertFalse(person2.isBirthBeforeDeath())
    
    def testMarryBeforeDeath(self):
        """
        Written by KR - Done
        :return:
        """
        person1 = Extract.Person("I1", "F1", "Oliver", "Black", 92, "929-5-18", "1955-2-27", "NA", "1995-9-7")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 11, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
        print(person2.isMarryBeforeDeath())
        self.assertTrue(person1.isMarryBeforeDeath())
        self.assertFalse(person2.isMarryBeforeDeath())
    
    def testDivorceBeforeDeath(self):
        """
        Written by KR - Done
        :return:
        """
        person1 = Extract.Person("I1", "F1", "Reagan", "Black", 91, "1906-11-4", "1930-6-11", "1935-3-4",
                                     "1998-4-18")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
    
        self.assertTrue(person1.isDivorceBeforeDeath())
        self.assertFalse(person2.isDivorceBeforeDeath())
    
    def testMarryBeforeDivorce(self):
        """
        Written by SK - Done
        :return:
        """
        person1 = Extract.Person("I1", "F1", "Reagan", "Black", 91, "1906-11-4", "1930-6-11", "1935-3-4",
                                     "1998-4-18")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
    
        self.assertTrue(person1.isMarryBeforeDivorce())
        self.assertFalse(person2.isMarryBeforeDivorce())

    """
    Sprint 2 Tests below
    """
    
    def testIsLessThan150YearOld(self):
        """
        Written by HRM
        :return:
        """
        person1 = Extract.Person("I1", "F1", "Reagan", "Black", 91, "1800-11-4", "1930-6-11", "1935-3-4",
                                     "1998-4-18")
        self.assertTrue(person1.isLessThan150YearOld())
    
    def testIsBirthAfterParentsDeath(self):
        """
        Written by NM
        :return:
        """
        individuals = [Extract.Person("I1", "F1", "Father", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
                       Extract.Person("I3", "F1", "Normal", "Isme", 15,
                                          "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                       Extract.Person("I4", "F1", "Ghost", "Isme", 15,
                                          "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       Extract.Person("I5", "F1", "Monster", "Isme", 15,
                                          "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       ]
        families = [Extract.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isBirthAfterParentsDeath(individuals, families))
    
    def testIsBirthAfterParentsMarriage(self):
        """
            Written by NM
            :return:
        """
        individuals = [Extract.Person("I1", "F1", "Father", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
                       Extract.Person("I3", "F1", "Normal", "Isme", 15,
                                          "1982-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                       Extract.Person("I4", "F1", "Ghost", "Isme", 15,
                                          "1988-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       Extract.Person("I5", "F1", "Monster", "Isme", 15,
                                          "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       ]
        families = [Extract.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isBirthAfterParentsMarriage(individuals, families))
    
    def testIsMarriageAfter14(self):
        """
            Written by KR
            :return:
        """
        individuals = [Extract.Person("I1", "F1", "Father", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
                       ]
        families = [Extract.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isMarriageAfter14(individuals, families))
    
    def testIsParentsNotTooOld(self):
        """
        Written by SK
        :return:
        """
        individuals = [Extract.Person("I1", "F1", "Father", "Isme", 15,
                                          "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
                       Extract.Person("I3", "F1", "Normal", "Isme", 15,
                                          "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                       Extract.Person("I4", "F1", "Ghost", "Isme", 15,
                                          "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       Extract.Person("I5", "F1", "Monster", "Isme", 15,
                                          "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       ]
        families = [Extract.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isParentsNotTooOld(individuals, families))
    
    def testIsThereBigamy(self):
        """
        Written by SK
        :return:
        """
        families1 = [Extract.Family("F1", "1985-2-27",
                                        "1986-2-27", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4']),
                     Extract.Family("F2", "1987-2-27",
                                        "NA", "I1", "Father /Isme/", "I2", "Mother /Ash/", ['I5']),
                     ]
        families2 = [Extract.Family("F1", "1985-2-27",
                                        "1995-2-27", "I1", "Father /Buck/", "I2", "Mother /Jenny/", ['I3', 'I4']),
                     Extract.Family("F2", "1990-2-27",
                                        "2000-2-27", "I6", "Father /Bob/", "I2", "Mother /Jenny/", ['I5']),
                     ]
        self.assertFalse(GedcomMain.isThereBigamy(families1))
        self.assertTrue(GedcomMain.isThereBigamy(families2))  

    """
    Sprint 3 Tests below
    """
    
    def testIsSiblingsLessThan15(self):
        """
        Written by KR
        :return:
        """
        families1 = [Extract.Family("F1", "1985-2-27",
                                        "1986-2-27", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4']),
                     Extract.Family("F2", "1987-2-27",
                                        "NA", "I1", "Father /Adam/", "I2", "Mother /Eve/", ['I5']),
                     ]
        families2 = [Extract.Family("F1", "1985-2-27",
                                        "1995-2-27", "I1",
                                        "Father /Bob/",
                                        "I2",
                                        "Mother /Jassica/",
                                        ['I3', 'I4', 'I8', 'I9', 'I3',
                                         'I4', 'I8', 'I9', 'I3', 'I4',
                                         'I8', 'I9', 'I3', 'I4', 'I8',
                                         'I9', 'I3', 'I4', 'I8', 'I9']),
                     Extract.Family("F2", "1990-2-27",
                                        "2000-2-27", "I6", "Father /Bob/", "I2", "Mother /Jassica/", ['I5']),
                     ]
        self.assertTrue(GedcomMain.isSiblingsLessThan15(families1))
        self.assertFalse(GedcomMain.isSiblingsLessThan15(families2))
    
    def testIsThereDuplicateNameAndBirthDate(self):
        """
        Written by HRM
        :return:
        """
        individuals1 = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                           "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                        Extract.Person("I4", "F1", "Father", "Adam", 15,
                                           "1920-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        Extract.Person("I5", "F1", "Monster", "Adam", 15,
                                           "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        individuals2 = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                           "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                        Extract.Person("I4", "F1", "Whatever", "Adam", 15,
                                           "1920-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        Extract.Person("I5", "F1", "Monster", "Adam", 15,
                                           "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        self.assertTrue(GedcomMain.isThereDuplicateNameAndBirthDate(individuals1))
        self.assertFalse(GedcomMain.isThereDuplicateNameAndBirthDate(individuals2))
    
    def testIsUniqueIDs(self):
        """
        Written by SK
        :return:
        """
        individualsTrue = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                              "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                           Extract.Person("I2", "F1", "Mother", "Adam", 15,
                                              "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
                           Extract.Person("I3", "F1", "Normal", "Adam", 15,
                                              "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                           Extract.Person("I4", "F1", "Ghost", "Adam", 15,
                                              "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                           Extract.Person("I5", "F1", "Monster", "Adam", 15,
                                              "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                           ]
        familiesTrue = [Extract.Family("F1", "1985-2-27",
                                           "NA", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4', 'I5']),
                        Extract.Family("F2", "1987-2-27",
                                           "NA", "I1", "Father /Adam/", "I2", "Mother /Eve/", ['I5'])
                        ]
        individualsFalse = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                               "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                            Extract.Person("I2", "F3", "Mother", "Adam", 15,
                                               "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
                            Extract.Person("I2", "F2", "Normal", "Adam", 15,
                                               "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                            Extract.Person("I4", "F2", "Ghost", "Adam", 15,
                                               "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                            ]
        familiesFalse = [Extract.Family("F1", "1985-2-27",
                                            "NA", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4', 'I5']),
                         Extract.Family("F1", "1987-2-27",
                                            "NA", "I1", "Father /Adam/", "I2", "Mother /Eve/", ['I5'])
                         ]
        self.assertTrue(GedcomMain.isUniqueIDs(individualsTrue, familiesTrue))
        self.assertFalse(GedcomMain.isUniqueIDs(individualsFalse, familiesFalse))
        self.assertFalse(GedcomMain.isUniqueIDs(individualsTrue, familiesFalse))
    
    def testIsSiblingsSpacing(self):
        """
        Written by NM
        :return:
        """
        individuals = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                          "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F1", "Mother", "Adam", 15,
                                          "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
                       Extract.Person("I3", "F1", "Normal", "Adam", 15,
                                          "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                       Extract.Person("I4", "F1", "Ghost", "Adam", 15,
                                          "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
                       Extract.Person("I5", "F1", "Monster", "Adam", 15,
                                          "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       ]
        families = [Extract.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.SiblingsSpacing(individuals, families))
    
    def testlist_deceased_individual(self):
        """
        Written by SK
        :return:
        """
        individuals = [Extract.Person("I1", "F1", "Andy", "Smith", 15,
                                          "1980-3-5", "1999-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F2", "San", "Zhang", 40,
                                          "1981-3-5", "1998-2-27", "NA", "NA")
                       ]
        self.assertTrue(GedcomMain.list_deceased_individual(individuals))
    
    def testmultiple_birth(self):
        """
        Written by KR
        :return:
        """
        families = [Extract.Family("F2", "1985-2-27", "NA",
                                       "I4", "Father /Adam/",
                                       "I3", "Mother /Adam/",
                                       ['I3', 'I4', 'I5']),
                    Extract.Family("F7", "1985-3-6", "NA",
                                       "I5", "Father /Adam/",
                                       "I9", "Mother /Adam/",
                                       ['I1', 'I4', 'I6', 'I7']),
                    ]
        self.assertTrue(GedcomMain.multiple_birth(families))

    """
    Sprint 4 Tests below
    """

    def testGetRecentBirths(self):
        """
        Written by NM
        """
        individuals = [Extract.Person("I1", "F1", "Andy", "Smith", 15,
                                          "2021-11-9", "1999-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F2", "San", "Zhang", 40,
                                          "1981-3-5", "1998-2-27", "NA", "NA")
                       ]
        self.assertTrue(GedcomMain.getRecentBirths(individuals))
    
    def testGetRecentDeaths(self):
        """
        Written by NM
        """
        individuals = [Extract.Person("I1", "F1", "Andy", "Smith", 15,
                                          "1985-2-27", "1999-2-27", "NA", "2021-11-25"),
                       Extract.Person("I2", "F2", "San", "Zhang", 40,
                                          "1981-3-5", "1998-2-27", "NA", "NA")
                       ]
        self.assertTrue(GedcomMain.getRecentDeaths(individuals))

    def testlist_living_single(self):
        """
        Written by HRM
        :return:
        """
        individuals = [Extract.Person("I1", "F1", "Andy", "Smith", 15,
                                          "1980-3-5", "NA", "NA", "NA"),
                       Extract.Person("I2", "F2", "San", "Zhang", 40,
                                          "1981-3-5", "NA", "NA", "NA")
                       ]
        self.assertTrue(GedcomMain.list_living_single(individuals))

    def testlist_name_and_age(self):
        """
        Written by HRM
        :return:
        """
        individuals = [Extract.Person("I1", "F1", "Andy", "Smith", 15,
                                          "1980-3-5", "1999-2-27", "NA", "1989-6-4"),
                       Extract.Person("I2", "F2", "San", "Zhang", 40,
                                          "1981-3-5", "1998-2-27", "NA", "NA")
                       ]
        self.assertTrue(GedcomMain.list_name_and_age(individuals))

    def testListLivingMarried(self):
        """
        Written by KR
        :return:
        """
        individuals1 = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                           "1920-3-5", "1985-2-27", "NA", "NA"),
                        Extract.Person("I2", "F1", "Mother", "Adam", 15,
                                           "1940-3-5", "1985-2-27", "NA", "NA"),
                        Extract.Person("I3", "F1", "Normal", "Adam", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        Extract.Person("I4", "F1", "Ghost", "Adam", 15,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
                        Extract.Person("I5", "F1", "Monster", "Adam", 15,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families1 = [Extract.Family("F1", "1985-2-27",
                                        "NA", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4', 'I5'])]
        individuals2 = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                           "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                        Extract.Person("I2", "F1", "Mother", "Adam", 15,
                                           "1940-3-5", "1985-2-27", "NA", "1989-1-1"),
                        Extract.Person("I3", "F1", "Normal", "Adam", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        Extract.Person("I4", "F1", "Ghost", "Adam", 15,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
                        Extract.Person("I5", "F1", "Monster", "Adam", 15,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families2 = [Extract.Family("F1", "1988-1-1",
                                        "NA", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.listLivingMarried(individuals1, families1))
        self.assertFalse(GedcomMain.listLivingMarried(individuals2, families2))

    def testListOrphans(self):
        """
        Written by SK
        :return:
        """
        individuals1 = [Extract.Person("I1", "F1", "Father", "Adam", 72,
                                           "1920-3-5", "1985-2-27", "NA", "1992-1-1"),
                        Extract.Person("I2", "F1", "Mother", "Adam", 52,
                                           "1940-3-5", "1985-2-27", "NA", "1992-1-1"),
                        Extract.Person("I3", "F1", "Normal", "Adam", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        Extract.Person("I4", "F1", "Ghost", "Adam", 30,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "NA"),
                        Extract.Person("I5", "F1", "Monster", "Adam", 5,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families1 = [Extract.Family("F1", "1985-2-27",
                                        "NA", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4', 'I5'])]
        individuals2 = [Extract.Person("I1", "F1", "Father", "Adam", 15,
                                           "1920-3-5", "1985-2-27", "NA", "NA"),
                        Extract.Person("I2", "F1", "Mother", "Adam", 15,
                                           "1940-3-5", "1985-2-27", "NA", "1989-1-1"),
                        Extract.Person("I3", "F1", "Normal", "Adam", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        Extract.Person("I4", "F1", "Ghost", "Adam", 15,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
                        Extract.Person("I5", "F1", "Monster", "Adam", 15,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families2 = [Extract.Family("F1", "1985-2-27",
                                        "NA", "I1", "Father /Adam/", "I2", "Mother /Adam/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.listOrphans(individuals1, families1))
        self.assertFalse(GedcomMain.listOrphans(individuals2, families2))

if __name__ == '__main__':
    unittest.main()