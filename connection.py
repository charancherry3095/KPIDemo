import pymongo

url = "mongodb+srv://charan12345:charan12345@mongodemo.tbdma.mongodb.net/test"
dbName = "demo1"
colName = "employees"


myClint = pymongo.MongoClient(url)
#print(myClint.list_database_names())

myDb = myClint.get_database(dbName) # get database
# print(myDb.list_collection_names())

myCol = myDb.get_collection(colName) # get colleciton - table
#print(myCol.find_one())
def findEmployee():
    x = myCol.find_one()
    x.pop("_id")
    return x
def getKPIValues():
    kpiDb = myClint.get_database("KPIFormulaTest")
    kpiCalcColl = kpiDb.get_collection("KPICalcData")
    kpiList = kpiCalcColl.find()
    listOfValues = []
    sum1 = 0
    for x in kpiList:
        x.pop("_id")
        sum1 = sum1 + x.pop("KPIValue")
        listOfValues.append(x)
    sum1 = sum1 / len(listOfValues)
    return sum1

def getLEAvg():
    kpiDb = myClint.get_database("KPIFormulaTest")
    kpiData = kpiDb.get_collection("KPICalcData1")
    kpiList = kpiData.find()
    listOfValues = []
    sum1 = 0
    for x in kpiList:
        x.pop("_id")
        sum1 = sum1 + x.pop("KPIValue")
        listOfValues.append(x)
    sum1 = sum1 / len(listOfValues)
    return sum1

#print(getKPIValues())
print(getLEAvg())