import statistics
from datetime import date
import os
import unittest
sys.path.insert(0, "MLForensics-farzana")
from mining import getPythonFileCount
#methods to fuzz -----------------------
# from mining.py


# from report.py

def Average(Mylist):
    return sum(Mylist) / len(Mylist)

def Median(Mylist):
    return statistics.median(Mylist)

# from dataset.stats.py

def getFileLength(file_):
    return sum(1 for line in open(file_, encoding='latin-1'))

def days_between(d1_, d2_): ## pass in date time objects
    return abs((d2_ - d1_).days)

# from mining.py
def getPythonFileCount(path2dir):
    valid_list = []
    for _, _, filenames in os.walk(path2dir):
        for file_ in filenames:
            if ((file_.endswith('py')) or (file_.endswith('ipynb'))):
                valid_list.append(file_)
    return len(valid_list)

#fuzzers-------------------------------------
def fuzzAv():
    print("Fuzzing Average()--------------------------------------------------------------")
    args = [["Case1-Traditional Input", [0, 1, 4, 7], 3], ["Case2-Empty Input", [], 0], ["Case3-String Input", ["abc", "def"], "invalid"], ["Case4-Decimal Input", ['1', '4', '7.0'], 3], ["Case5-List Input", [4, [1, 2, 3], "invalid"]]]
    for arr in args:
        try:
            temp=Average(arr[1])
            if (temp != arr[2]):
                raise Exception("{scenario} Failed\n\tExpected: {exp}\n\tFound: {found}".format(scenario=arr[0], exp=arr[2], found=temp))
            print("{scen}: Case Passed".format(scen=arr[0]))
        except Exception as e:
            print(arr[0], "Error:", e)

def fuzzMed():
    print("\nFuzzing Median()----------------------------------------------------------------")
    args = [["Case1-Traditional Input", [0, 1, 4, 7], 2.5], ["Case2-Empty Input", [], "invalid"], ["Case3-String Input", ["abc", "def"], "invalid"], ["Case4-Decimal Input", [1, '4.5'], 2.25], ["Case5-List Input", [4, [1, 2, 3]], "invalid"]]
    for arr in args:
        try:
            temp=Median(arr[1])
            if (temp != arr[2]):
                raise Exception("{scenario} Failed\n\tExpected: {exp}\n\tFound: {found}".format(scenario=arr[0], exp=arr[2], found=temp))
            print("{scen}: Case Passed".format(scen=arr[0]))
        except Exception as e:
            print(arr[0], "Error:", e)

def fuzzFileLength():
    print("\nFuzzing getFileLength()--------------------------------------------------------")
    args = [["Case1-File in pwd", '5', 95], ["Case2-Valid File Path", 'MLForensics-farzana/empirical/report.py', 106], ["Case3-Invalid File Path", 'bad/path/unknown.py', "invalid path"], ["Case4-Empty Path", [], "invalid path"], ["Case5-Number Path", 5, "invalid path"]]
    for arr in args:
        try:
            temp=getFileLength(arr[1])
            if (temp != arr[2]):
                raise Exception("{scenario} Failed\n\tExpected: {exp}\n\tFound: {found}".format(scenario=arr[0], exp=arr[2], found=temp))
            print("{scen}: Case Passed".format(scen=arr[0]))
        except Exception as e:
            print(arr[0], "Error:", e)

def fuzzDaysBetween():
    print("\nFuzzing day_between()----------------------------------------------------------")
    dateA = date(2025, 1,1)
    dateB= date(2025, 1,2)
    dateC= date(2026, 1,1)
    dateD = date(2000, 2, 1)
    dateE = date(1900, 2, 1)
    args = [["Case1-Different Days, Same Year", dateA, dateB, 1], ["Case2-Same Date", dateA, dateA, 0], ["Case3-Same Day, Different Year", dateA, dateC, 365], ["Case4-Backwards in Time", dateC, dateA, 365], ["Case5-Contain Leap Years", dateD, dateE, 36524], ["Case6-Number Input", 5, 6, "invalid"], ["Case7-String Input", 'abc', 'def', "invalid"], ["Case8-None Input", dateA, None]]
    for arr in args:
        try:
            temp=days_between(arr[1], arr[2])
            if (temp != arr[3]):
                raise Exception("{scenario} Failed\n\tExpected: {exp}\n\tFound: {found}".format(scenario=arr[0], exp=arr[3], found=temp))
            print("{scen}: Case Passed".format(scen=arr[0]))
        except Exception as e:
            print(arr[0], "Error:", e)

def fuzzPyFileCount():
    print("\nFuzzing getPythonFileCount()--------------------------------------------------------")
    args = [["Case1-Valid FilePath", 'MLForensics-farzana/mining', 4], ["Case2-Invalid Path", 'bad/path/unknown.py', 0], ["Case3-Empty Path", '', 0], ["Case4-None Input", None, 0]]
    for arr in args:
        try:
            temp=getPythonFileCount(arr[1])
            if (temp != arr[2]):
                raise Exception("{scenario} Failed\n\tExpected: {exp}\n\tFound: {found}".format(scenario=arr[0], exp=arr[2], found=temp))
            print("{scen}: Case Passed".format(scen=arr[0]))
        except Exception as e:
            print(arr[0], "Error:", e)

if __name__=='__main__':
    fuzzAv()
    fuzzMed()
    fuzzFileLength()
    fuzzDaysBetween()
    fuzzPyFileCount()
