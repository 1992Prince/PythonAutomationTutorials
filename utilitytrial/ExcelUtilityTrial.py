from utilities.ExcelUtility import *#getRowCount, getColCount, getCellData

path = "..//testData/PythonTestData.xlsx"
sheetName = "Sheet1"

rows = getRowCount(path,sheetName)
cols = getColCount(path,sheetName)

print(rows,"--------",cols)

print(getCellData(path,sheetName,2,1))
setCellData(path,sheetName,8,1,"Bharat")

