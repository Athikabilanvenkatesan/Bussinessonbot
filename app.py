from flask_restful import Resource,Api
# from flask_cors import CORS
from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bot_sqlite.sqlite3"

db = SQLAlchemy(app)
# app.app_context().push()
api = Api(app)
# CORS(app)

class Bank(db.Model):
    ifsc = db.Column(db.String,primary_key=True)
    bank_id = db.Column(db.Integer)
    branch = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    district = db.Column(db.String)
    state = db.Column(db.String)
    bank_name = db.Column(db.String)

# import pandas as pd
# file = pd.read_csv('bank_branches.csv')

# for i in range(file.shape[0]):
#     l=[]
#     for j in range(file.shape[1]):
#         l.append(file.iloc[i,j])
#     user_obj = Bank(ifsc=l[0],
#                     bank_id=int(l[1]),
#                     branch=l[2],
#                     address=l[3],
#                     city=l[4],
#                     district=l[5],
#                     state=l[6],
#                     bank_name=l[7])
#     db.session.add(user_obj)
#     db.session.commit()

import sqlite3
class BANK_SEARCH(Resource):
    def get(self):
        conn = sqlite3.connect(r"C:\Users\athik\OneDrive\Desktop\Bot\instance\bot_sqlite.sqlite3")
        posts = conn.execute('SELECT * FROM bank').fetchall()
        conn.close()
        query = request.args.get('q').upper()
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        ind = []
        
        for i in posts:
            flag=0
            for j in range(2,8):
                if i[j] and query in i[j]:
                    flag=1
            if flag:
                ind.append(i)

    
        obj = ind[(offset+1):(offset+limit+1)]
        l=[]
        for i in obj:
            l.append((i[0],{"ifsc":i[0],
                              "bank_id":i[1],
                              "branch":i[2],
                              "address":i[3],
                              "city":i[4],
                              "district":i[5],
                              "state":i[6],
                              "bank_name":i[7]
                              }))

            # l.append((i.ifsc,{"ifsc":i.ifsc,
            #                   "bank_id":i.bank_id,
            #                   "branch":i.branch,
            #                   "address":i.address,
            #                   "city":i.city,
            #                   "district":i.district,
            #                   "state":i.state,
            #                   "bank_name":i.bank_name
            #                   }))            
            
        l.sort()
        temp=[]
        for i in l:
           temp.append(i[1])
        return {
            "branches":temp
        }

class BANK_BRANCH(Resource):
    def get(self):
        conn = sqlite3.connect(r"C:\Users\athik\OneDrive\Desktop\Bot\instance\bot_sqlite.sqlite3")
        posts = conn.execute('SELECT * FROM bank').fetchall()
        conn.close()
        query = request.args.get('q').lower()
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        ind = []
        
        for i in posts:
            flag=0
            for j in range(2,8):
                if i[j] and query in i[j].lower():
                    flag=1
            if flag:
                ind.append(i)

    
        obj = ind[(offset+1):(offset+limit+1)]
        l=[]
        for i in obj:
            l.append((i[0],{"ifsc":i[0],
                              "bank_id":i[1],
                              "branch":i[2],
                              "address":i[3],
                              "city":i[4],
                              "district":i[5],
                              "state":i[6],
                              "bank_name":i[7]
                              }))

            # l.append((i.ifsc,{"ifsc":i.ifsc,
            #                   "bank_id":i.bank_id,
            #                   "branch":i.branch,
            #                   "address":i.address,
            #                   "city":i.city,
            #                   "district":i.district,
            #                   "state":i.state,
            #                   "bank_name":i.bank_name
            #                   }))            
            
        l.sort(reverse=True)
        temp=[]
        for i in l:
           temp.append(i[1])
        return {
            "branches":temp
        }      

api.add_resource(BANK_SEARCH,'/api/search')
api.add_resource(BANK_BRANCH,'/api/branch')

if __name__ == '__main__':
    app.run(port=5050)
