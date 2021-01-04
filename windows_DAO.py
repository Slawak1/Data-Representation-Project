

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config

class WindowDAO:
    # db = ""
    def __init__(self):
        print("Hi")


    # method to register customer
    # param : JSON : info taken from HTML form - name, username and password
    def register(self, register_data):
        print(register_data)     

        values = [
            register_data["name"],
            register_data["username"],
            register_data["password"],
        ]
        try: 
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            if conn.is_connected():
        
                sql = "INSERT INTO users (name, username, password) VALUES (%s, %s,%s)"
                cursor.execute(sql,values)
                conn.commit()
                print ("JOB DONE")
                return 1
            else:
                print("Not Connected to Database")
        except Error as e:
            print("ERROR: ")
            print(e)
        
        finally:
            
            if conn is not None and conn.is_connected():
                print("conn_closed")
                cursor.close()
                conn.close()
            
    # method to login 
    # param : JSON : login data (username, password)
    def login(self, login_data):

        values = [login_data["username"]]
        try: 
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            if conn.is_connected():
                
                sql = "SELECT username, password FROM users WHERE username = %s"
                cursor.execute(sql,values)
                data = cursor.fetchone()
                print(data)

                
                if data[0] == "" and data[1]=="":
                    print("Not Found")
                    return 0
                else:
                    if login_data["password"] == data[1]:
                        print("logged in")
                        return 1
                    else:
                        print("Wrong Password")

                        return 0
            else:
                print("Not Connected to Database")
        except Error as e:
            print("ERROR: ")
            print(e)
        
        finally:
            
            if conn is not None and conn.is_connected():
                print("conn_closed")
                cursor.close()
                conn.close()
            
        
    # method to create customer
    # param : JSON : customer information (name, phone_no, email)
    def create_customer(self, customer):
        try: 
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            if conn.is_connected():

                sql = "INSERT INTO Customer ( name, phone_no, email) VALUES ( %s,%s,%s)"

                values = [
                    customer["name"],
                    customer["phone_no"],
                    customer["email"]
                    ]  

                cursor.execute(sql, values)
                conn.commit()

                return cursor.lastrowid 
            else:
                print("Not Connected to Database")
        except Error as e:
            print("ERROR: ")
            print(e)
        
        finally:
            if conn is not None and conn.is_connected():
                print("conn_closed")
                cursor.close()
                conn.close()

    # method to display all customers in HTML table
    def get_all(self):
        try: 
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            if conn.is_connected():
                
                sql = "SELECT * FROM Customer"

                cursor.execute(sql)

                result = cursor.fetchall()
                return_arr = []
                
                for r in result:
                    result_as_dict = self.convert_to_dict(r)
                    return_arr.append(result_as_dict)     

                return return_arr
            else:
                print("Not Connected to Database")
        except Error as e:
            print("ERROR: ")
            print(e)
        
        finally:
            if conn is not None and conn.is_connected():
                print("conn_closed")
                cursor.close()
                conn.close()

    # method to convert to dictionary
    def convert_to_dict(self,result):
        colnames = ["id","name","phone_no","email"]
        customer= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                customer[col_name] = value
        return customer

    # method to find customer by its id 
    def find_customer_by_id(self,id):
        try: 
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            if conn.is_connected():
                
                sql = "SELECT * FROM Customer WHERE id = %s"
                values = [id]
                cursor.execute(sql,values)
                result = cursor.fetchone()
                    
                return self.convert_to_dict(result)
            else:
                print("Not Connected to Database")
        except Error as e:
            print("ERROR: ")
            print(e)
        
        finally:
            if conn is not None and conn.is_connected():
                print("conn_closed")
                cursor.close()
                conn.close()

    # method to update customer data in MySQL table 
    def update_customer(self, customer):

        try: 
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            if conn.is_connected():

                
                sql = '''UPDATE customer SET
                            name = %s, 
                            phone_no = %s, 
                            email = %s 
                            WHERE id = %s'''

                values = [
                    customer["name"],
                    customer["phone_no"],
                    customer["email"],
                    customer["id"]
                    ]  

                cursor.execute(sql, values)
                conn.commit()

                return customer
            else:
                print("Not Connected to Database")
        except Error as e:
            print("ERROR: ")
            print(e)
        
        finally:
            if conn is not None and conn.is_connected():
                print("conn_closed")
                cursor.close()
                conn.close()
    
    # method to remove customer from database
    def delete_customer (self, id):
        try: 
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            if conn.is_connected():

                
                sql = "DELETE FROM Customer WHERE id = %s"
                values = [id]
                cursor.execute(sql,values)
                conn.commit()

                return {}
            else:
                print("Not Connected to Database")
        except Error as e:
            print("ERROR: ")
            print(e)
        
        finally:
            if conn is not None and conn.is_connected():
                print("conn_closed")
                cursor.close()
                conn.close()


