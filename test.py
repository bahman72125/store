import sqlite3


class Database():
    def __init__(self):
        self.db=sqlite3.connect('database2.db')
    
    def findall(self):
        mycursor=self.db.cursor()
        print(1)
        sql='''SELECT * FROM factor'''    
        mycursor.execute(sql)
        data= mycursor.fetchall()
        for d in data: 
         print(d)    

        print(2)
        sql='''SELECT count(*),sum(total) FROM factor''' 
        mycursor.execute(sql)
        print(mycursor.fetchone())  

        print(3)
        sql='''SELECT cid,count(*),sum(total) FROM factor GROUP BY cid''' 
        mycursor.execute(sql)
        data= mycursor.fetchall()
        for d in data: 
         print(d)  

        print(4)
        sql='''SELECT date,count(*),sum(total) FROM factor GROUP BY date''' 
        mycursor.execute(sql)
        data= mycursor.fetchall()
        for d in data: 
         print(d) 

        print(5)
        sql='''SELECT cid,count(*),sum(total) FROM factor  WHERE total>1000 GROUP BY cid''' 
        mycursor.execute(sql)
        data= mycursor.fetchall()
        for d in data: 
         print(d)   

        print(6)
        sql='''SELECT cid,count(*),sum(total) FROM factor  GROUP BY cid''' 
        mycursor.execute(sql)
        data= mycursor.fetchall()
        for d in data: 
         print(d)   

        print(7)
        sql='''SELECT name FROM 
                customers  JOIN 
                (SELECT cid ,MAX(total) FROM factor)f
                ON f.cid=customers.id ''' 
        mycursor.execute(sql)
        print(mycursor.fetchone())
          
        print(8)
        sql='''SELECT name FROM 
                customers JOIN 
                (SELECT cid,SUM(total) 
                FROM factor  
                GROUP BY cid 
                ORDER BY SUM(total) DESC
                LIMIT 1)f 
                ON customers.id=f.cid''' 
        mycursor.execute(sql)
        print(mycursor.fetchone())

        print(9)
        sql='''SELECT factor.* FROM factor LEFT JOIN factor_details ON factor.id=factor_details.fid WHERE factor_details.id IS NULL ''' 
        mycursor.execute(sql)
        data= mycursor.fetchall()
        for d in data: 
         print(d)    
        self.db.commit()
    

    def all(self):
        mycursor=self.db.cursor()
        sql='''SELECT count(*),sum(total) FROM factor'''    
        mycursor.execute(sql)
        self.db.commit()
        print(mycursor.fetchall())


    def factor3(self):
        mycursor=self.db.cursor()
        sql='''SELECT cid,count(*),sum(total) FROM customers JOIN factor ON customers.id=factor.cid'''    
        mycursor.execute(sql)
        self.db.commit()
        return mycursor.fetchall()

    def factor4(self):
        mycursor=self.db.cursor()
        sql='''SELECT * FROM factor JOIN customers '''    
        mycursor.execute(sql)
        self.db.commit()
        print(mycursor.fetchall()) 


if __name__ == "__main__":
    db=Database()
    db.findall()
     