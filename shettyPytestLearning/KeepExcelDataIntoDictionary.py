from utilities.ExcelUtility import *

dict1 = {}
path = "..//testData/PythonTestData.xlsx"
sheet = "Sheet1"
max_row = getRowCount(path, sheet)
max_col = getColCount(path, sheet)

print("-------------------Keeping only Test1 Data into Dictionary----------------------")
for i in range(2, max_row + 1):
    if getCellData(path,sheet,i,1) == "Test1":
        for j in range(1, max_col+1):
            dict1[getCellData(path,sheet,1,j)] = getCellData(path, sheet, i, j)

print("Dictionary is :",dict1," dict1.get('username') ",dict1.get("username"))

print("-------------------Keeping all Testcases testdata into Dictionary----------------------")

list2 = []
for i in range(2, max_row + 1):
    dict2 = {}
    for j in range(1, max_col+1):
        dict2[getCellData(path,sheet,1,j)] = getCellData(path, sheet, i, j)
    list2.append(dict2)

print("Dictionary is :",list2)

