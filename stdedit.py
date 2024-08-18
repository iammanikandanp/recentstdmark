#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os
import itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
oo=cgi.FieldStorage()
uid=oo.getvalue("poiuytrewq")
fid=oo.getvalue("stdregno")
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
        .ee{
        display:flex;
        justify-content:end;
        margin-right:30px;
        margin-bottom:50px;
        }
        table{
        width:300px;
        }
        textarea{
        border:none;
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
        <h1 class="kk">STUDENT DETAILS [edit]</h1>
        <div class="container">
        <form enctype = "multipart/form-data" method = "post"> 
        <table class="table table-bordered table-striped table-hover ">
           """)
oi = """select regno,name,dob,gender,email,bloodgrp,address,pincode,phone,aadhar,ugper from register where regno='%s'"""%(fid)
cur.execute(oi)
hot = cur.fetchone()
print("""

            <tr>
                <tr> <th>REGNO </th> <td><input type="text" name="regno" value="%s"></td></tr>
               <tr> <th>NAME</th> <td><input type="text" name="name" value="%s"></td></tr>
                <tr><th>DOB</th> <td><input type="text" name="dob" value="%s"></td></tr>
                <tr><th>GENDER</th> <td><input type="text" name="gender" value="%s"></td></tr>
                <tr><th>EMAIL</th> <td><input type="text" name="email" value="%s"></td></tr>
                 <tr><th>BLOOD GROUP</th><td><input type="text" name="bldgrp" value="%s"></td></tr>
               <tr> <th>ADDRESS</th><td><textarea name="add" row="3" cols="50">%s</textarea></td></tr>
                 <tr><th>PINCODE</th><td><input type="text" name="pincode" value="%s"></td></tr>
               <tr> <th>PHONE NO</th><td><input type="text" name="phnum" value="%s"></td></tr>
               <tr><th>AADHAR</th> <td><input type="text" name="aadhar" value="%s"></td></tr>
                 <tr><th>UG PRECENT</th><td><input type="text" name="ug" value="%s"></td></tr>
            """ % (hot[0], hot[1],hot[2], hot[3], hot[4], hot[5], hot[6], hot[7], hot[8], hot[9], hot[10]))

print("""
        </table>
    </div>
    <div class="ee">
    <button class="btn btn-success btn-lg" name="upt">Update</button>
    </div>
    </form>""")
reg=oo.getvalue("regno")
name=oo.getvalue("name")
dob=oo.getvalue("dob")
gen=oo.getvalue("gender")
email=oo.getvalue("email")
bldgrp=oo.getvalue("bldgrp")
add=oo.getvalue("address")
aadhar=oo.getvalue("aadhar")
pin=oo.getvalue("pincode")
phnum=oo.getvalue("phnum")
ug=oo.getvalue("ug")
submit=oo.getvalue("upt")
if submit != None:
    po="""update register set regno='%s',name='%s',dob='%s',gender='%s',email='%s',bloodgrp='%s',address='%s',pincode='%s',phone='%s',aadhar='%s',ugper='%s' where regno='%s'"""%(reg,name,dob,gen,email,bldgrp,add,pin,phnum,aadhar,ug,fid)
    cur.execute(po)
    con.commit()
    print("""<script>
    alert("update ayruchu!");
    location.href="stddetail.py"
    </script>""")
print("""
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>   
</body>
</html>""")