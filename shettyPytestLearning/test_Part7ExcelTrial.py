from utilities.ExcelUtility import *

def test_fetchExcelData():
    path = "..//testData/PythonTestData.xlsx"
    sheet = "Sheet1"
    max_row = getRowCount(path, sheet)
    max_col = getColCount(path, sheet)

    for i in range(1, max_row + 1):
        for j in range(1, max_col+1):
            print(getCellData(path, sheet, i, j),end=" ")
        print()

    print("-------------------Fetching Test1 Data----------------------")
    # print only Test1 username and password
    for i in range(2, max_row + 1):
        if getCellData(path,sheet,i,1) == "Test3":
            for j in range(1, max_col+1):
                print(getCellData(path, sheet, i, j),end=" ")
            print()