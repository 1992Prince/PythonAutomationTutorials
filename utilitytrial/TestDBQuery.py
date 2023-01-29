from utilities import DBManagerUtility_3

DBManagerUtility_3.createDbConnection()
dbresult = DBManagerUtility_3.getMySqlQuery("select * from CustomerInfo")
print(dbresult[0],"---",dbresult)