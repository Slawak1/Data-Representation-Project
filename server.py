from flask import Flask, url_for,request,redirect,abort,jsonify,session
from windows_DAO import WindowDAO
import requests


app = Flask(__name__,static_url_path='', static_folder='static_pages')

#create app secret_key for session
app.secret_key = 'super secret key'




@app.route('/')
def index():
    return app.send_static_file('index.html')

# login 
@app.route('/login', methods = ["POST"])
def login():

    login_data = {
        "username":request.json["username"],
        "password":request.json["password"]       
    }
    session['username'] = login_data["username"]

    return jsonify(WindowDAO().login(login_data))


# log out
@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("username", None)
    print("Logged out from server")

    return app.send_static_file('index.html')
 

# register new user
@app.route('/register', methods = ["POST"])
def register():

    register_data = {
        "name":request.json["name"],
        "username":request.json["username"],
        "password":request.json["password"]
    }

    return jsonify(WindowDAO().register(register_data))
    
# get all customers 
@app.route("/customer")
def getAll():
    return jsonify(WindowDAO().get_all())

# fin by id
@app.route("/customer/<int:id>")
def findById(id):
    
    return jsonify(WindowDAO().find_customer_by_id(id))


# create
# curl -X POST  -d "{\"name\":\"test\",\"phone_no\":\"11223344\",\"email\":\"some email\"}" -H "content-type:application/json" http://127.0.0.1:5000/customer
@app.route("/customer", methods = ["POST"])
def create():

    if not request.json:
        abort(400)

    customer = {
        "name":request.json["name"],
        "phone_no":request.json["phone_no"],
        "email":request.json["email"]
    }
    return jsonify(WindowDAO().create_customer(customer))

# update 
# curl -X PUT -d "{\"name\":\"extra name\",\"phone_no\":\"00000\"}" -H "content-type:application/json" http://127.0.0.1:5000/customer/2
@app.route("/customer/<int:id>", methods = ["PUT"])
def update(id):
    found_customer = WindowDAO().find_customer_by_id(id)
    if found_customer == {}:
        return jsonify({}), 404
    
    current_customer = found_customer
    
    if "name" in request.json:
        current_customer["name"] = request.json["name"]

    if "phone_no" in request.json:
        current_customer["phone_no"] = request.json["phone_no"]

    if "email" in request.json:
        current_customer["email"] = request.json["email"]

    WindowDAO().update_customer(current_customer)
    return jsonify(current_customer)

# delete
# curl -X DELETE http://127.0.0.1:5000/customer/13
@app.route("/customer/<int:id>", methods = ["DELETE"])
def delete(id):

    WindowDAO().delete_customer(id)
    return jsonify({"done":True})
  

if __name__ =="__main__":
    
    app.run(debug =True)
