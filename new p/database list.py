import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="shilpa")
cur=myconn.cursor()
sql=("insert into shilpa(name,address,salary) values(%s,%s,%s)")
val=[("anju",150,16000.00),("manju",170,17000.00),("gudda",190,18000.00)]
cur.executemany(sql,val)
cur.execute("select * from shilpa")
result=cur.fetchall()
for x in result:
    print(x)
myconn.commit()
myconn.close()
