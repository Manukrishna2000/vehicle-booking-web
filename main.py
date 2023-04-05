from flask import *

from Dbconnection import Db

app = Flask(__name__)
app.secret_key = "abc"


@app.route('/')
def index():
    c = Db()
    qry = "select * from addvehicle"
    r = c.select(qry)
    return render_template('index.html', data=r)


@app.route('/userview')
def userview():
    c = Db()
    username = session['username']
    qry = "select * from addvehicle"
    qry1 = "select * from register where username='" + str(username) + "'"
    r = c.select(qry)
    r1 = c.selectOne(qry1)
    return render_template('userhome.html', data=r, data1=r1)


@app.route('/login')
def login():
    return render_template('adminlogin.html')


@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')


@app.route('/addvehicle')
def addvehicle():
    return render_template('addvehicle.html')


@app.route('/userhome')
def userhome():
    return render_template('userhome.html')


@app.route('/testdrive')
def testdrive():
    c = Db()
    username = session['username']
    qry = "select * from register where username='" + str(username) + "'"
    r = c.selectOne(qry)
    qry1 = "select model from addvehicle"
    r1 = c.select(qry1)
    return render_template("testdrive.html", data=r, data1=r1)


@app.route('/login_post', methods=['post'])
def login_post():
    c = Db()
    uname = request.form['txt_username']
    password = request.form['txt_password']
    qry = "select * from login where username='" + uname + "'  and `password`='" + password + "'"
    res = c.selectOne(qry)
    if res is not None:
        type = res['type']
        if type == 'admin':
            session['username'] = res['username']
            return adminhome()
        elif type == 'user':
            session['username'] = res['username']
            return userview()
        else:
            return '''<script>alert('invalid username or password');window.location='/'</script>'''
    else:
        return '''<script>alert('invalid username or password');window.location='/'</script>'''


@app.route('/addvehicle_post', methods=['post'])
def seller_add_product_post():
    vname = request.form['textfield']
    model = request.form['textfield1']
    spec = request.form['textfield2']
    price = request.form['textfield3']
    photo = request.files['fileField']
    photo.save("E:\\Project\\vehicle booking\\static\\vehicles\\" + photo.filename)
    path = "/static/vehicles/" + photo.filename
    qry = "insert into addvehicle(vehicle_name,model,specification,price,photo)values('" + vname + "','" + model + "','" + spec + "','" + price + "','" + path + "')"
    c = Db()
    c.insert(qry)
    return '''<script>alert("added successfully");window.location="/addvehicle"</script>'''


@app.route('/delete/<v_id>')
def delete(v_id):
    db = Db()
    qry = "delete from addvehicle where v_id='" + str(v_id) + "'"
    db.delete(qry)
    return '''<script>alert("deleted successfully");window.location="/view_vehicle"</script>'''


@app.route('/')
def vehicles():
    c = Db()
    qry = "select * from addvehicle"
    r = c.select(qry)
    return render_template("index.html", data=r)


@app.route('/register')
def register():
    c = Db()
    qry = "select model from addvehicle"
    r = c.select(qry)

    return render_template('register.html', data=r)



@app.route('/register_post', methods=['post'])
def register_post():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    # date = request.form['date']
    # time = request.form['time']
    # model = request.form['model']
    address = request.form['address']
    zip = request.form['zip']
    city = request.form['city']
    username = request.form['username']
    password = request.form['password']
    qry = "insert into register(name,email,phone,address,zipcode,city,username,password)values('" + name + "','" + email + "','" + phone + "','" + address + "','" + zip + "','" + city + "','" + username + "','" + password + "')"
    qry1 = "insert into login(username,password,type)values('" + username + "','" + password + "','user')"
    c = Db()
    c.insert(qry)
    c.insert(qry1)
    return '''<script>alert("Thank you for registering");window.location="/register"</script>'''


@app.route('/booked_post', methods=['post'])
def booked_post():
    username = session['username']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']
    model = request.form['model']
    address = request.form['address']
    zip = request.form['zip']
    city = request.form['city']
    qry = "insert into booked(username,name,email,phone,date,time,model,address,zipcode,city,status)values('" + username + "','" + name + "','" + email + "','" + phone + "','" + date + "','" + time + "','" + model + "','" + address + "','" + zip + "','" + city + "','pending')"
    c = Db()
    c.insert(qry)
    return '''<script>alert("Thank you for registering, Our sales Executive will contact you shortly");window.location="/userview"</script>'''


@app.route('/view_booking')
def view_booking():
    c = Db()
    qry = "select * from booked where status='pending'"
    r = c.select(qry)
    return render_template('view_booking.html', data=r)


@app.route('/view_users')
def view_users():
    c = Db()
    qry = "select * from register"
    r = c.select(qry)
    return render_template('view_users.html', data=r)


@app.route('/view_vehicle')
def view_vehicle():
    c = Db()
    qry = "select * from addvehicle"
    r = c.select(qry)
    return render_template('vehicle.html', data=r)


@app.route('/view_vehicle_edit/<v_id>')
def view_vehicle_edit(v_id):
    c = Db()
    qry = "select * from addvehicle where v_id='" + str(v_id) + "'"
    r = c.selectOne(qry)
    return render_template('edit_vehicle.html', data=r)


@app.route('/testdrive_complete/<slno>')
def testdrive_complete(slno):
    c = Db()
    qry = "update booked set status='complete' where slno='" + str(slno) + "'"
    c.update(qry)
    return '''<script>alert("updated");window.location="/adminhome"</script>'''



@app.route('/edit_vehicle_post', methods=['post'])
def edit_vehicle_post():
    v_id = request.form['vid']
    model = request.form['textfield1']
    vname = request.form['textfield']
    spec = request.form['textfield2']
    price = request.form['textfield3']
    photo = request.files['fileField']
    photo.save("E:\\Project\\vehicle booking\\static\\vehicles\\" + photo.filename)
    path = "/static/vehicles/" + photo.filename
    qry = "update addvehicle set vehicle_name='" + vname + "', model='" + model + "', specification='" + spec + "', price='" + price + "', photo='" + path + "' where v_id='" + v_id + "'"
    c = Db()
    c.update(qry)
    return '''<script>alert("update succesfull");window.location="/view_vehicle"</script>'''


@app.route('/userview_booking')
def userview_booking():
    username = session['username']
    c = Db()
    qry = "select * from booked where username='" + username + "'"
    r = c.select(qry)
    return render_template('userview_booking.html', data=r)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/checkusername', methods=['POST'])
def checkusername():
    c = Db()
    print(request.form)
    email=request.form['un']
    qr="SELECT * FROM `register` WHERE `username`='"+email+"' "
    res=c.selectOne(qr)
    print(res)
    if res is None:
        resp = make_response(json.dumps(""))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        resp = make_response(json.dumps("Username Existing"))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


@app.route('/checkemail1', methods=['POST'])
def checkemail1():
    c = Db()
    print(request.form)
    email=request.form['em']
    qr="SELECT * FROM `register` WHERE `email`='"+email+"'"
    res=c.selectOne(qr)
    print(res)
    if res is None:
        resp = make_response(json.dumps(""))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        resp = make_response(json.dumps("Email Existing"))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

@app.route('/checkphone1', methods=['POST'])
def checkphone1():
    c=Db()
    print(request.form)
    email=request.form['ph']
    qr="SELECT * FROM `register` WHERE `phone`='"+email+"'"
    res=c.selectOne(qr)
    print(res)
    if res is None:
        resp = make_response(json.dumps(""))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        resp = make_response(json.dumps("Phone number Existing"))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


@app.route('/view_complete')
def view_complete():
    c = Db()
    qry = "select * from booked where status='complete'"
    r = c.select(qry)
    return render_template('view_completed_booking.html', data=r)


@app.route('/checkmodel', methods=['POST'])
def checkmodel():
    c=Db()
    print(request.form)
    email=request.form['mo']
    qr="SELECT * FROM `addvehicle` WHERE `model`='"+email+"'"
    res=c.selectOne(qr)
    print(res)
    if res is None:
        resp = make_response(json.dumps(""))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        resp = make_response(json.dumps("Model Existing"))
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
