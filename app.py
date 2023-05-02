from flask import Flask,render_template,redirect,request,flash,url_for
import pymysql

app = Flask(__name__,static_folder="staticfile")



@app.route('/')
def index():
    db=pymysql.connect(host="localhost",user="root",password="",database="emp")
    cur= db.cursor()
    sql="select * from emp_details"
    cur.execute(sql)
    res= cur.fetchall()
    return render_template('index.html',d=res)
    
    

@app.route('/add')
def add():
    return render_template('adduser.html')

@app.route('/adduser',methods=['get','post'])
def adduser():
    if request.method == "POST":
        en= request.form['ename']
        ee = request.form['eemail']
        edo = request.form['edob']
        ed = request.form['edept']
        em = request.form['emobile']
        es = request.form['esalary']

        db= pymysql.connect(host="localhost",user="root",password="",database="emp")
        cur = db.cursor()
        sql="insert into emp_details (name,email,dob,dept,mobile,salary) values ('{}','{}','{}','{}','{}','{}')".format(en,ee,edo,ed,em,es)
        cur.execute(sql)
        db.commit()
        return render_template('adduser.html')
    
@app.route('/update',methods=['get','post'])
def update():
    db=pymysql.connect(host="localhost",user="root",password="",database="emp")
    cur= db.cursor()
    sql="select * from emp_details"
    cur.execute(sql)
    res= cur.fetchall()
    return render_template('edit.html',d=res)

@app.route('/editu/<string:id>',methods=['get','post'])
def editu(id):
    db=pymysql.connect(host="localhost",user="root",password="",database="emp")
    cur= db.cursor()
    sql="select * from emp_details where empid ={}".format(id)
    cur.execute(sql)
    res= cur.fetchone()
    return render_template('edituser.html',d=res)

@app.route('/updateuser/<string:id>' ,methods=['post','get'] )
def updateuser(id):
    if request.method == "POST":

        en = request.form['ename']
        edo = request.form['edob']
        ee = request.form['eemail']
        ed= request.form['edept']
        em = request.form['emobile']
        es = request.form['esalary']
        
        db=pymysql.connect(host="localhost",user="root",password="",database="emp")
        cur = db.cursor()
        sql="update emp_details set name = '{}', email ='{}', dob='{}', dept='{}',mobile={}, salary='{}' where empid='{}'".format(en,ee,edo,ed,em,es,id)
        cur.execute(sql)
        db.commit()
        return redirect(url_for('update'))
        


@app.route('/delete/<string:id>',methods=['get','post'])
def delete(id):
    db=pymysql.connect(host="localhost",user="root",password="",database="emp")
    cur = db.cursor()
    sql = "delete from emp_details where empid={}".format(id)
    cur.execute(sql)
    db.commit()
    return redirect(url_for('update'))
    
app.run(debug=True)