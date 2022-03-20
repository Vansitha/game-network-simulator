# ************************************************************************
# FILE: UnitTestHashTable.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: Tests for hash table
# REFERENCE: This file has been submitted previously for DSA COMP1002 Practical 7
#            (Hash Tables) submission.
#            Ratanayke, Vansitha Induja. COMP1002 Graphs Practical 7 Submission
# COMMENTS: None
# REQUIRES: DSAHashTable from HashTable.py
# LAST MOD: 14/10/21
# ************************************************************************
from HashTable import DSAHashTable


class testHashTable:

    table = DSAHashTable(10)

    def testPut(self):
        status = False
        try:
            print("<--------Adding Entries to Table------->")
            self.table.put('A', "user1")
            self.table.put('B', "user2")
            self.table.put('C', "user3")
            self.table.put('D', "user4")
            self.table.put('E', "user5")
            self.table.put('F', "user6")
            self.table.put('G', "user7")
            self.table.put("H", "user8")
            self.table.put('I', "user9")
            self.table.put('J', "user10")

            # add duplicates
            self.table.put('A', "user9")
            self.table.put('J', "user2")
            self.table.put('C', "user3")
            status = True

        except Exception as e:
            print("Adding Entries: Failed:", e)

        return status

    def testGet(self):
        status = False
        try:
            print("<--------Get entries in table------->")
            print(self.table.get('A'))
            print(self.table.get('I'))
            print(self.table.get('H'))
            print(self.table.get('D'))

            # Not in table
            print("<--------Get entries not in table------->")
            self.table.get('Z')
            self.table.get('Y')
            self.table.get('X')
            status = True

        except Exception as e:
            print("Get Values: Failed:", e)

        return status

    def testRemove(self):
        status = False

        try:
            print("<--------Remove Entries------->")
            self.table.remove('I')
            self.table.remove('D')
            self.table.remove('E')
            status = True

        except Exception as e:
            print("Remove Entries: Failed", e)

        return status

    def testDisplay(self, mode=None):
        status = False
        try:
            print("<----------Display Table--------->")
            self.table.display(mode)
            status = True
        except Exception as e:
            print("Display Table: Failed", e)

        return status

    def testLoadFactor(self):
        status = False
        try:
            print("<----------Load Factor--------->")
            print(f"Load Facotor = {self.table.getLoadFactor()}%")
            status = True

        except Exception as e:
            print("Get Load Factor: Failed")

        return status

    def testCount(self):
        status = False
        try:
            print("<----------No of Entries--------->")
            print("Entries = ", self.table.getCount())
            status = True

        except Exception as e:
            print("Get Count: Failed")

        return status

    def testUpdate(self):
        status = False
        try:
            print("<----------Update Entry--------->")

            self.table.update('A', 'testUpdate1')
            self.table.update('J', 'testUpdate2')
            status = True

        except Exception as e:
            print("Update Entry: Failed")

        return status


if __name__ == "__main__":

    ht = testHashTable()

    passed = 0

    test1 = ht.testPut()
    if test1 == True:
        print("Adding Entries: Passed")
        passed += 1

    test2 = ht.testDisplay()
    if test2 == True:
        print("\nDisplay Table: Passed")
        passed += 1

    test3 = ht.testGet()
    if test3 == True:
        print("\nGet Entries: Passed")
        passed += 1

    test4 = ht.testRemove()
    if test4 == True:
        print("Remove Entries: Passed")
        passed += 1
        ht.testDisplay()

    test5 = ht.testLoadFactor()
    if test5 == True:
        print("Get Load Factor: Passed")
        passed += 1

    test6 = ht.testCount()
    if test6 == True:
        print("Get Count: Passed")
        passed += 1

    test7 = ht.testUpdate()
    if test7 == True:
        print("Update Entries: Passed")
        passed += 1
        ht.testDisplay()

    print("\n<-------TEST SUMMARY------->")
    totalTests = 7
    print(f"Tests Passed= {passed}/{totalTests}")
