#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os
import itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
o=cgi.FieldStorage()
uid=o.getvalue("poiuytrewq")
fid=o.getvalue("lkjhgfdsa")
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Userdash</title>
    <link rel="icon" href="./mani.jpg" type="image/x-icon">
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="style/internal.css">
    <style>
        .kl{
            margin-top: 30px;
            overflow-x: scroll;
            
        }
        .kk{
            background-image: linear-gradient(rgb(44, 44, 117),rgb(151, 151, 53),red);
            color: transparent;
            background-clip: text;
            text-align:center;
        }
    </style>
    
</head>
<body>
    <nav>
        <div>
            <a href="#"><i class="jj glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                data-target="#menus"></i></a>&nbsp;&nbsp;
            <a href=""><h2 class="brand">EASC</h2></a>
        </div>
    </nav>
    <div id="menus" class="collapse col-md-4 col-sm-6 col-xs-10">
            <div class="row">
                <div class="col-md-2 col-xs-3" style="padding-top: 5px;">
                    <img src="./media/0ff34f3d1e08b2495e995ab7e6cfaeb7.jpg" alt="userprofile" class="img-circle" width="50px"
                        height="50px" name="pics">
                </div>
                <div class="col-md-8 col-xs-6">
                    <h3 name="uname">Username</h3>
                </div>
            </div>
            <ul class="ol">
                <li><a href="">INTERNAL 1</a></li>
                <li><a href="">INTERNAL 2 </a></li>
                <li><a href="">INTERNAL 3 </a></li>
                <li><a href="">INTERNAL CONVERT</a></li>
                <li><a href="./model.html">MODEL</a></li>
               
                <li class="dropdown"><a  class="dropdown-toggle" data-toggle="dropdown" href="">SEM-INTERNAL <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="">MACHINE LEARNING</a></li>
                    <li><a href="">ADVANCED JAVA </a></li>
                    <li><a href="">WEB TECHNOLOGY</a></li>
                </ul></li>
                <li><a href="">PRACTICAL</a></li>
                <li class="dropdown"><a  class="dropdown-toggle" data-toggle="dropdown" href="">SEM-MARK <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="">MACHINE LEARNING</a></li>
                        <li><a href="">ADVANCED JAVA </a></li>
                        <li><a href="">WEB TECHNOLOGY</a></li>
                    </ul></li>
                
            </ul>
        </div>
        <h1 class="kk">STUDENT DETAILS</h1>
        <div class="kl">
        <table class="table table-bordered table-striped table-hover ">
            <tr>
                <th>REGNO</th>
                <th>NAME</th>
                <th>DOB</th>
                <th>GENDER</th>
                <th>EMAIL</th>
                <th>BLOOD GROUP</th>
                <th>ADDRESS</th>
                <th>PINCODE</th>
                <th>PHONE NO</th>
                <th>AADHAR</th>
                <th>UG PRECENT</th>
                <th>EDIT</th>
                <th>DELETE</th>
            </tr>""")
oi="""select regno,name,dob,gender,email,bloodgrp,address,pincode,phone,aadhar,ugper from register order by regno"""
cur.execute(oi)
hot=cur.fetchall()
for i in hot:
    print("""
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><a href="stdedit.py?stdregno=%s&poiuytrewq=%s"><button class="btn btn-success">Edit</button></a></td> 
                <td><a href="stddelete.py?stdregno=%s&poiuytrewq=%s"> <button class="btn btn-danger">Delete</button></a></td> 
            </tr>"""% (i[0], i[1], i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[0],uid,i[0],uid))
print("""
        </table>
    </div>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>
</html>""")