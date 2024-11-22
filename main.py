from flask import Flask, request
from flask_restful import Api, Resource
import db

app = Flask(__name__)
api = Api(app)

class callMySlt:
    def exeDb(self):
        conn = db.DbConnection.dbconnHadwh("")
        sql = 'SELECT * FROM OSS_FAULTS.LTE_OCS_PCRF_DATA'
        c = conn.cursor()
        c.execute(sql)
        result = {}
        data=[]
        for row in c:
            data.append({"PACKAGE_TYPE": row[0],
                        "ADDON_NAME": row[1],
                        "RECURRENCE": row[2],
                        "DATA_VOLUME_GB": row[3],
                        "VALIDITY": row[4],
                        "PRICE_LKR_WITHOUT_TAX": row[5],
                        "PRICE_LKR_WITH_TAX": row[6],
                        "PACKAGE_ID": row[7],
                        "OFFERING_NAME": row[8],
                        "OFFERING_ID": row[9],
                        "OFFERING_CATEGORY": row[10],
                        "VOICE_VOLUME": row[11],})   
        result['data'] = data
        return result

class getDetails(Resource):
    def get(self):
        return  callMySlt.exeDb("")
        #print(data)
        #return {'data': result}

api.add_resource(getDetails, '/api/mySltOcs/mapping/')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=20002)

    