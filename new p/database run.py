import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="shilpa"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE T2(id INT NOT NULL,name VARCHAR(100),salary VARCHAR(100)")
sql=("insert into T2(id,name,salary)values(%s,%s,%s)")
val=[(1,"arihant","45 lakh"),(2,"shashank","42 lakh"),(3,"pallav","44 lakh")]
mycursor.executemany(sql,val)
mycursor.execute("select * from T2")
result=mycursor.fetchall()
for x in result:
    print(x)
mydb.commit()
mydb.close()

                 
