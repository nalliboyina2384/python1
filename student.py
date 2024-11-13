import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="jithendra"
)
print(mydb)
c=mydb.cursor()
c.execute("insert into student values(120,'jithendra',100,'vijayawada')")
c.execute("insert into student values(121,'siva',100,'tanuku')")
c.execute("insert into student values(122,'ashok',100,'guntur')")
c.execute("insert into student values(123,'nithin',100,'vijayawada')")
c.execute("insert into student values(124,'mani',100,'rajmundry')")
c.execute("delete from student where sid=123")
c.execute("delete from student where sid=122")
c.execute("update student set city='tanuku'where sid=121")
mydb.commit()
