#Imports required before Executing The code
from flask import Flask, jsonify
from flask_restplus import Api, Resource #pip install flask-restplus Werkzeug==0.16.1 
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
from statistics import mean
import math
from datetime import datetime
from time import gmtime, strftime
import time
client = MongoClient(
    'mongodb+srv://pharmauser:Welcome123@cluster0.oha8u.mongodb.net')
mydb = client["KPIFormulaTest"]
collection = mydb["KPICalcData1"]
flask_app = Flask(__name__)
flask_app.config["MONGO_DBNAME"] = "KPIFormulaTest"
flask_app.config["MONGO_URI"] = "mongodb+srv://pharmauser:Welcome123@cluster0.oha8u.mongodb.net/KPIFormulaTest"
mongo = PyMongo(flask_app)

app = Api(app=flask_app)
name_space = app.namespace('Api/Asset', description="Asset Api's")
#Maximum Value Of First Pass Yield
@name_space.route("/maxfpy")

class MainClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'id': 'Specify the Id associated with the person'})
    def get(self):
        framework = mongo.db.KPICalcData1
        output = []
        for q in framework.find({"AppName": "FPY"}):
            output.append(int(q["KPIValue"]))
        response_2 = str(max(output))
        response = jsonify(response_2)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
#Mean(Average) Value Of First Pass Yield
@name_space.route("/meanfpy")
class MainClassTwo(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'id': 'Specify the Id associated with the person'})
    def get(self):
       framework=mongo.db.KPICalcData1
       output=[]
       for q in framework.find({ "AppName": "FPY"}):
	       output.append(int(q["KPIValue"]))
       response_2=str(math.floor(mean(output)))
       response=jsonify(response_2)
       response.headers.add('Access-Control-Allow-Origin', '*')
       return response

#maxolq
#Maximum Value Of OLQ
@name_space.route("/maxolq")
class MainClassThree(Resource):
    def get(self):
        framework=mongo.db.KPICalcData1
        output=[]
        for q in framework.find({ "AppName": "OLQ"}):
            output.append(int(q["KPIValue"]))
        response_2=str(max(output))
        response=jsonify(response_2)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
#meanolq
#Mean(Average) Value Of OLQ
@name_space.route("/meanolq")
class MainClassFour(Resource):
    def get(self):
        framework=mongo.db.KPICalcData1
        output=[]
        for q in framework.find({ "AppName": "OLQ"}):
            output.append(int(q["KPIValue"]))
        response_2=str(math.floor(mean(output)))
        response=jsonify(response_2)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
#meanos
#Mean(Average) Value Of OS
@name_space.route("/meanos")
class MainClassFive(Resource):
    def get(self):
        framework=mongo.db.KPICalcData1
        output=[]
        out_1=[]
        out_3=[]
        tot_1=0
        tot_2=0
        # tot_is=0
        # tot_os=0
        for q in framework.find({ "AppName": "FPY"}):
            output.append(q["tags"])
        for w in range(len(output)):
            out_1.append(int(output[w][7].get("val")))
        for e in range(len(output)):
            out_3.append(int(output[e][8].get("val")))
        tot_1=math.floor(mean(out_1))
        tot_2=math.floor(mean(out_3))
        res_os = jsonify(str(tot_1))
        res_is = jsonify(str(tot_2))
        res_os.headers.add('Access-Control-Allow-Origin', '*')
        res_is.headers.add('Access-Control-Allow-Origin', '*')
        return res_os
#meanis
#Mean(Average) Value Of IS
@name_space.route("/meanis")
class MainClassSix(Resource):
    def get(self):
        framework=mongo.db.KPICalcData1
        output=[]
        out_1=[]
        out_3=[]
        tot_1=0
        tot_2=0
        # tot_is=0
        # tot_os=0
        for q in framework.find({ "AppName": "FPY"}):
            output.append(q["tags"])
        for w in range(len(output)):
            out_1.append(int(output[w][7].get("val")))
        for e in range(len(output)):
            out_3.append(int(output[e][8].get("val")))
        tot_1=math.floor(mean(out_1))
        tot_2=math.floor(mean(out_3))
        res_os = jsonify(str(tot_1))
        res_is = jsonify(str(tot_2))
        res_os.headers.add('Access-Control-Allow-Origin', '*')
        res_is.headers.add('Access-Control-Allow-Origin', '*')
        return res_is
#meanr
#Mean(Average) Value Of Reject
@name_space.route("/meanr")
class MainClassSeven(Resource):
    def get(self):
        framework=mongo.db.KPICalcData1
        output=[]
        out_2=[]
        total=0
        for q in framework.find({ "AppName": "OLQ"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][3].get("val")))
        total=math.floor(mean(out_2))
        response=jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


#meanah
#Mean(Average) Value Of AH
@name_space.route("/meanah")
class MainClassEight(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        out_2=[]
        total = 0
        for q in avloss.find({"AppName": "LE"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][0].get("val")))
        total=round(mean(out_2),2)
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


#meansh
#Mean(Average) Value Of SH
@name_space.route("/meansh")
class MainClassNine(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        out_2=[]
        total = 0
        for q in avrej.find({"AppName": "LE"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][1].get("val")))
        total=math.floor(mean(out_2))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
#meandt
#Mean(Average) Value Of DT
@name_space.route("/meandt")
class MainClassTen(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        out_2=[]
        total = 0
        for q in avrej.find({"AppName": "OLD"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][2].get("val")))
        total=math.floor(mean(out_2))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
#meanpt
#Mean(Average) Value Of PT
@name_space.route("/meanpt")
class MainClassEleven(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        out_2=[]
        total = 0
        for q in avloss.find({"AppName": "OLLE"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][0].get("val")))
        total=math.floor(mean(out_2))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


#meanp
#Mean(Average) Value Of Produced
@name_space.route("/meanp")
class MainClassTwelve(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        out_2=[]
        total = 0
        for q in avrej.find({"AppName": "QBR"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][1].get("val")))
        total=math.floor(mean(out_2))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#meangp
#Mean(Average) Value Of Good Parts
@name_space.route("/meangp")
class MainClassThirteen(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        out_2=[]
        total = 0
        for q in avrej.find({"AppName": "QBR"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][0].get("val")))
        total=math.floor(mean(out_2))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#osval
#Unused
@name_space.route("/osval")
class MainClassFourteen(Resource):
    def get(self):
        framework=mongo.db.KPICalcData1
        output=[]
        out_2=[]
        for q in framework.find({ "AppName": "FPY"}):
            output.append(q["tags"])
        for i in range(len(output)):
            out_2.append(int(output[i][7].get("val")))
        response=jsonify(str(out_2))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#total asset 2
#totrej
#Total(Sum) Value Of Reject
@name_space.route("/totrej")
class MainClassFifteen(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        total = 0
        for q in avloss.find({"AppName": "OLQ"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total += int(output[i][3].get("val"))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#totos
#Total(Sum) Value Of OS
@name_space.route("/totos")
class MainClassSixteen(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        total_os = 0
        for q in avrej.find({"AppName": "FPY"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total_os += int(output[i][7].get("val"))
        res_os = jsonify(str(total_os))
        res_os.headers.add('Access-Control-Allow-Origin', '*')
        return res_os

#totis
#Total(Sum) Value Of IS
@name_space.route("/totis")
class MainClassSeventeen(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        total_is = 0
        for q in avrej.find({"AppName": "FPY"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total_is += int(output[i][8].get("val"))
        res_is = jsonify(str(total_is))
        res_is.headers.add('Access-Control-Allow-Origin', '*')
        return res_is
#totah
#Total(Sum) Value Of AH
@name_space.route("/totah")
class MainClassEighteen(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        total = 0
        for q in avloss.find({"AppName": "LE"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total += int(output[i][0].get("val"))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#totsh
#Total(Sum) Value Of SH
@name_space.route("/totsh")
class MainClassNineteen(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        total_os = 0
        for q in avrej.find({"AppName": "LE"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total_os += int(output[i][1].get("val"))
        res_os = jsonify(str(total_os))
        res_os.headers.add('Access-Control-Allow-Origin', '*')
        return res_os

#totdt
#Total(Sum) Value Of DT
@name_space.route("/totdt")
class MainClassTwenty(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        total_is = 0
        for q in avrej.find({"AppName": "OLD"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total_is += int(output[i][2].get("val"))
        res_is = jsonify(str(total_is))
        res_is.headers.add('Access-Control-Allow-Origin', '*')
        return res_is
#totpt
#Total(Sum) Value Of PT
@name_space.route("/totpt")
class MainClassTwentyOne(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        total = 0
        for q in avloss.find({"AppName": "OLLE"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total += int(output[i][0].get("val"))
        response = jsonify(str(total))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#totp
#Total(Sum) Value Of Produced
@name_space.route("/totp")
class MainClassTwentyTwo(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        total_os = 0
        for q in avrej.find({"AppName": "QBR"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total_os += int(output[i][1].get("val"))
        res_os = jsonify(str(total_os))
        res_os.headers.add('Access-Control-Allow-Origin', '*')
        return res_os
#totgp
#Total(Sum) Value Of Good Parts
@name_space.route("/totgp")
class MainClassTwentyThree(Resource):
    def get(self):
        avrej = mongo.db.KPICalcData1
        output = []
        total_is = 0
        for q in avrej.find({"AppName": "QBR"}):
            output.append(q["tags"])
        for i in range(len(output)):
            total_is += int(output[i][0].get("val"))
        res_is = jsonify(str(total_is))
        res_is.headers.add('Access-Control-Allow-Origin', '*')
        return res_is


#maxle
#Maximum value of LE
@name_space.route("/maxle")
class MainClassTwentyFour(Resource):
    def get(self):
        framework = mongo.db.KPICalcData1
        output = []
        for q in framework.find({"AppName": "LE"}):
            output.append(q["KPIValue"])
        out = str(max(output))
        response = jsonify(out)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


#avgle
#Average Value of LE
@name_space.route("/avgle")
class MainClassTwentyFive(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        for q in avloss.find({"AppName": "LE"}):
            output.append(q["KPIValue"])
        avgloss = str(round(mean(output), 2))
        response = jsonify(avgloss)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


#Maximum OLD
#maxold
#Maximum Value of OLD
@name_space.route("/maxold")
class MainClassTwentySix(Resource):
    def get(self):
        framework = mongo.db.KPICalcData1
        output = []
        for q in framework.find({"AppName": "OLD"}):
            output.append(q["KPIValue"])
        out = str(max(output))
        response = jsonify(out)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#Average OLD
#avgold
#Average Value of OLD
@name_space.route("/avgold")
class MainClassTwentySeven(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        for q in avloss.find({"AppName": "OLD"}):
            output.append(q["KPIValue"])
        avgloss = str(round(mean(output), 2))
        response = jsonify(avgloss)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#Maximum OLLE
#maxolle
#Average Value of OLLE
@name_space.route("/maxolle")
class MainClassTwentyEight(Resource):
    def get(self):
        framework = mongo.db.KPICalcData1
        output = []
        for q in framework.find({"AppName": "OLLE"}):
            output.append(q["KPIValue"])
        out = str(max(output))
        response = jsonify(out)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
#Average OLLE
#avgolle
#Average Value of OLLE
@name_space.route("/avgolle")
class MainClassTwentyNine(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        for q in avloss.find({"AppName": "OLLE"}):
            output.append(q["KPIValue"])
        avgloss = str(round(mean(output), 2))
        response = jsonify(avgloss)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#Maximum QBR
#maxqbr
#Maximum Value of QBR
@name_space.route("/maxqbr")
class MainClassThirty(Resource):
    def get(self):
        framework = mongo.db.KPICalcData1
        output = []
        for q in framework.find({"AppName": "QBR"}):
            output.append(q["KPIValue"])
        out = str(max(output))
        response = jsonify(out)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#Average QBR
#avgqbr
#Average Value of QBR
@name_space.route("/avgqbr")
class MainClassThirtyOne(Resource):
    def get(self):
        avloss = mongo.db.KPICalcData1
        output = []
        for q in avloss.find({"AppName": "QBR"}):
            output.append(q["KPIValue"])
        avgloss = str(round(mean(output), 2))
        response = jsonify(avgloss)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
#osgraph
#Graph of OS
@name_space.route("/osgraph")
class MainClassThirtyTwo(Resource):
    def get(self):

        vals = mongo.db.KPICalcData1
        out = []
        count=0
        #a=vals.find_one({"AppName": "FPY"})["StartTime"]+1800
        for q in vals.find({"AppName": "FPY"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][7].get("val"))})
                count+=1
            # inp.clear()
        
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#produced yield (graph)
#ygraph

@name_space.route("/ygraph")
class MainClassThirtyThree(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "FPY"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#osgraphtwo
#Graph of OS (2nd Asset)
@name_space.route("/osgraphtwo")
class MainClassThirtyFour(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLQ"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][7].get("val"))})
                count+=1
            # inp.clear()

        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#rgraphtwo
#Graph of Reject(2nd Asset)
@name_space.route("/rgraphtwo")
class MainClassThirtyFive(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "FPY"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][3].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#rgraph
#Graph of Reject
@name_space.route("/rgraph")
class MainClassThirtySix(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0 
        for q in vals.find({"AppName": "OLQ"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][3].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#isgraph
#Graph of IS
@name_space.route("/isgraph")
class MainClassThirtySeven(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "FPY"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][8].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#isgraphtwo
#Graph of IS(2nd Asset)
@name_space.route("/isgraphtwo")
class MainClassThirtyEight(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLQ"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][8].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#pgraph
#Graph of Produced
@name_space.route("/pgraph")
class MainClassThirtyNine(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "QBR"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start": strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][1].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output

#ptwograph
#Graph of Produced(2nd Asset)
@name_space.route("/ptwograph")
class MainClassForty(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "QBR"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start": strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][1].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#ptgraph
#Graph of PT
@name_space.route("/ptgraph")
class MainClassFortyOne(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLLE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start": strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][0].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#pttwograph
#Graph of PT(2nd Asset)
@name_space.route("/pttwograph")
class MainClassFortyTwo(Resource):
    def get(self):
        count=0
        vals = mongo.db.KPICalcData1
        out = []
        for q in vals.find({"AppName": "OLLE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start": strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][0].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#gpgraph
#Graph of Good Parts
@name_space.route("/gpgraph")
class MainClassFortyThree(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "QBR"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start": strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][0].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#gptwograph
#Graph of Good Parts(2nd Asset)
@name_space.route("/gptwograph")
class MainClassFortyFour(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "QBR"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start": strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][0].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#ahgraph
#Graph of AH
@name_space.route("/ahgraph")
class MainClassFortyFive(Resource):
    def get(self):
        count=0
        vals = mongo.db.KPICalcData1
        out = []
        for q in vals.find({"AppName": "LE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][0].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#ahgraphtwo
#Graph of AH(2nd Asset)
@name_space.route("/ahgraphtwo")
class MainClassFortySix(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "LE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][0].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#shgraph
#Graph of SH
@name_space.route("/shgraph")
class MainClassFortySeven(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "LE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][1].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#shgraphtwo
#Graph of SH(2nd Asset)
@name_space.route("/shgraphtwo")
class MainClassFortyEight(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "LE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
               out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][1].get("val"))})
               count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#dtgraph
#Graph of DT
@name_space.route("/dtgraph")
class MainClassFortyNine(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLD"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][2].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#dtgraphtwo
#Graph of DT(2nd Asset)
@name_space.route("/dtgraphtwo")
class MainClassFifty(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLD"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":int(q["tags"][2].get("val"))})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#legraph
#Graph of LE
@name_space.route("/legraph")
class MainClassFiftyOne(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "LE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#legraphtwo
#Graph of LE(2nd Asset)
@name_space.route("/legraphtwo")
class MainClassFiftyTwo(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "LE"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#oldgraph
#Graph of OLD
@name_space.route("/oldgraph")
class MainClassFiftyThree(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLD"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#oldgraphtwo
#Graph of OLD(2nd Asset)
@name_space.route("/oldgraphtwo")
class MainClassFiftyFour(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLD"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#olqgraph
#Graph of OLQ
@name_space.route("/olqgraph")
class MainClassFiftyFive(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLQ"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
        # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#olqgraphtwo
#Graph of OLQ(2nd Asset)
@name_space.route("/olqgraphtwo")
class MainClassFiftySix(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLQ"}):
        # inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
        # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#ollegraph
#Graph of OLLE
@name_space.route("/ollegraph")
class MainClassFiftySeven(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLLE"}):
        # inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#olletwograph
#Graph of OLLE(2nd Asset)
@name_space.route("/olletwograph")
class MainClassFiftyEight(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "OLLE"}):
        # inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#qbrgraph
#Graph of QBR(2nd Asset)
@name_space.route("/qbrgraph")
class MainClassFiftyNine(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "QBR"}):
        # inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output
#qbrgraphtwo
#Graph of QBR(2nd Asset)
@name_space.route("/qbrtwograph")
class MainClassSixty(Resource):
    def get(self):
        vals = mongo.db.KPICalcData1
        out = []
        count=0
        for q in vals.find({"AppName": "QBR"}):
            #inp = [q["StartTime"], q["KPIValue"]]
            if(count<10):
                out.append({"start":strftime(str(datetime.fromtimestamp(q["StartTime"]))), "KPIValue":q["KPIValue"]})
                count+=1
            # inp.clear()
        output = jsonify(out)
        output.headers.add('Access-Control-Allow-Origin', '*')
        return output    
# api.add_resource(MainClass,'/')
#flask_app.run(host="0.0.0.0")
