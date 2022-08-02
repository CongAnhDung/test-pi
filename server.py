from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler
# from demo_mysql_connect import Data
import os
import mysql.connector 


class Server(BaseHTTPRequestHandler):
    # student_info =[]
    def show_all_data():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dunggttn1512.",
        database="WEBAPI_DB"
        )
        mycursor = mydb.cursor()
        sql = " SELECT * FROM Employee"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.close()
        return myresult
    
    # student_info = show_all_data()
    # datas = list(student_info[0])
    # datas = 1

    
    def do_GET(self):
        print(Server.show_all_data())
        if self.path == '/':
            self.path = '/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                f += '<div class="hidden">'
                for i in Server.show_all_data() :
                    f += '<div class="data-student" attr-id="1">'
                    f += f'<div id=ID>{i[0]}</div>'
                    f += f'<div id=FirstName>{i[1]}</div>'
                    f += f'<div id=LastName>{i[2]}</div>'
                    f += f'<div id=Gender>{i[3]}</div>'
                    f += f'<div id=Salary>{i[4]}</div>'


            # f += '<div class="data-student" attr-id="1">'
            # f += '<div id=number>1</div>'
            # f += '<div id=name>Dung</div>'
            # f += '<div id=class>PHP</div>'
            # f += '<div id=class>23</div>'

                f += '</div>'
                print(f)
                self.send_response(200)
                self.send_header('value', 1)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
                #self.wfile.write(bytes(f, 'utf-8'))
            else:
                print(1)
                f = "File not found"
                self.send_error(404,f)
        except Exception as e:
            print(str(e))
            f = "File not found"
            self.send_error(404,f)