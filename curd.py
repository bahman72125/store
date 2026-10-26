import sqlite3
import requests

class Database():
    def __init__(self):
        self.db=sqlite3.connect('database.db')
        self.createTablegoods()
        self.create_factor()
        self.create_customer()
        self.create_factor_d()

    def create_factor(self):
        mycursor=self.db.cursor()
        sql='''CREATE TABLE factor (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    date TEXT NOT NULL,
                                    cid INTEGER  FORGIN KEY NOT NULL
                                     
                                   ) ;'''    
        try:
            mycursor.execute(sql)
        except:
           pass

    def insert_factor(self,cid,date):
        URL= 'http://127.0.0.1:8000/factor'
        mydata={'cid':cid,'date':date}
        result=requests.post(url=URL , json=mydata)
        x=result.json()
        return x['id']
      

    def update_factor(self,id):
        URL= f'http://127.0.0.1:8000/factor/{id}'
        result=requests.put(url=URL )
        print(result.status_code)
    

    def create_factor_d(self):
        mycursor=self.db.cursor()
        sql='''CREATE TABLE factor_details(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    fid INTEGER  FORGIN KEY NOT NULL,
                                    pid INTEGER  FORGIN KEY NOT NULL,
                                    no INTEGER NOT NULL,
                                    total INTEGER NOT NULL    
                                    );'''    
        try:
            mycursor.execute(sql)
           
        except:
            pass

    def insert_factor_d(self,data_list):
        URL= 'http://127.0.0.1:8000/factor_details'
        result=requests.post(url=URL , json=data_list)
        print('insert',result.status_code)
      

    def delete_factor_d(self,fid):
        URL= f'http://127.0.0.1:8000/factor_details/{fid}'
        result=requests.post(url=URL)
        print('del',result.status_code)
        

    def findall_factor_d(self):
        URL= 'http://127.0.0.1:8000/factor_details'
        result=requests.get(url=URL)
        print(result.status_code)
           

    def create_customer(self):
        mycursor=self.db.cursor()
        sql='''CREATE TABLE customer(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    pass TEXT NOT NULL,
                                   
                                    );'''    
        try:
            mycursor.execute(sql)
        except:
            pass     


    def insert_customer(self,name,password):
        URL= 'http://127.0.0.1:8000/customer'
        mydata={'username':name,'password':password}
        requests.post(url=URL , json=mydata)
      

    def find_last_id(self):
        URL= 'http://127.0.0.1:8000/customer/max'
        result=requests.get(url=URL)
        if result.status_code==200:
            print(result)
            return result.json()
       

    def createTablegoods(self):
        mycursor=self.db.cursor()
        sql='''CREATE TABLE goods (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    price INTEGER NOT NULL
                                    );'''    
        try:
            mycursor.execute(sql)
              
        except:
           pass  

    def inserttabel(self,myname,myprice):
        URL= 'http://127.0.0.1:8000/product'
        mydata={'name':myname,'price':myprice}
        result=requests.post(url=URL , json=mydata)
        print(result.status_code)
        
      
        

    def findall(self):
        URL= 'http://127.0.0.1:8000/product'
        result=requests.get(url=URL)
        if result.status_code==200:
            return result.json()
       
    
    def update_goods(self,id,name,price):
        URL= f'http://127.0.0.1:8000/product/{id}'
        mydata={'id':id,'name':name,'price':price}
        result=requests.put(url=URL , json=mydata)
        print(result.status_code)
      
    
    def find_goods(self,id='',name='',fprice='',tprice=''):
        if id=='' and name=='' and fprice=='' and tprice=='':
            return self.findall()
    
        if id != '':
            print(id)
            URL= f'http://127.0.0.1:8000/product/{id}'
            result=requests.get(url=URL )
            return result.json()
           
        elif name=='':
            if fprice !='' and tprice!='':
                URL= f'http://127.0.0.1:8000/product/ftprice/{fprice}/{tprice}'
                mydata={'fprice':fprice ,'tprice':tprice}
                result=requests.get(url=URL , json=mydata)
                return result.json()
              
            elif tprice !='':
                URL= f'http://127.0.0.1:8000/product/tprice/{tprice}'
                result=requests.get(url=URL )
                return result.json()
              
            else:
                URL= f'http://127.0.0.1:8000/product/fprice/{fprice}'
                result=requests.get(url=URL )
                return result.json()
           
        else:
            URL= f'http://127.0.0.1:8000/product/name/{name}'
            result=requests.get(url=URL )
            if result.status_code==200:
                return result.json()
 

    def delete_goods(self,id):
        URL= f'http://127.0.0.1:8000/product/{id}'
        result=requests.delete(url=URL )
        if result.status_code==200:
            print(result.json())
       
     

    def delete_all_goods(self):
        URL= 'http://127.0.0.1:8000/product'
        result=requests.delete(url=URL )
        if result.status_code==200:
            print(result.json())
       


    def find_customer_id(self):
        sql=''' SELECT max(id) FROM customer'''
        mycursor=self.db.cursor()
        mycursor.execute(sql)
        result=mycursor.fetchone()
        if result[0]:
            return result[0]+1
        else:
            return 1



if __name__ == "__main__":
    pass

