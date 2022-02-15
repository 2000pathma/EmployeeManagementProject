import sqlite3
class Database():
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employee(
        id Integer Primary Key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
    )
    """

        self.cur.execute(sql)
        self.con.commit()

    #insert function
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employee values(NULL,?,?,?,?,?,?,?)",
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()

    #fetch  all data from database
    def fetch(self):
        self.cur.execute('select * from employee')
        rows=self.cur.fetchall()
        #print(rows)-print a data in a console so we are return the rows
        return rows
    #delete a Record in database
    def remove(self,id):
        self.cur.execute("delete from employee where id=?",(id,))
        self.con.commit()

    #update function
    def update(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("update employee set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=?",
                             (name, age, doj, email, gender, contact, address))
        self.con.commit()


o=Database("employee.db")
#o.insert("priya",'20','21-06-2000','pathma@gmail.com','female','7478432783','2/300-5,tenkasi')
#o.insert("ramesh",'21','08-10-1999','ramesh@gmail.com','male','7478432678','2/300-5,ramnadu')
#o.insert("ram",'22','18-10-1999','ram@gmail.com','male','9078432678','2/300-5,tamilnadu')
#o.fetch()
o.remove(6)
#o.update("ramya",'2','18-10-2030','ramya@gmail.com','female','9458432678','2/300-5,ramnadu')
