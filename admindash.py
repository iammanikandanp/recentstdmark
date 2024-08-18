#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os
import itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
df=cgi.FieldStorage()
uid=df.getvalue("poiuytrewq")
fid=df.getvalue("lkjhgfdsa")
ry="""select name from adminreg where regno='%s'"""%(uid)
cur.execute(ry)
you=cur.fetchone()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal 2</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
    .dt{
    display:flex;
    justify-content:center;
    gap:30px;
    }
    h4{
    color:blue}
    </style>
    </head>

""")
print("""
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
                    <img src="./media/" alt="userprofile" class="img-circle" width="50px"
                        height="50px" name="pics">
                </div>
                <div class="col-md-8 col-xs-6">
                    <h3 name="uname">%s</h3>
                </div>
            </div>
            <ul class="ol">
                <li><a href="stddash.py?poiuytrewq=%s">INTERNAL 1</a></li>
                <li><a href="internal2.py?poiuytrewq=%s">INTERNAL 2 </a></li>
                <li><a href="internal3.py?poiuytrewq=%s">INTERNAL 3 </a></li>
                <li><a href="demo.py?poiuytrewq=%s">INTERNAL CONVERT</a></li>
                <li><a href="model.py?poiuytrewq=%s">MODEL</a></li>

                <li class="dropdown"><a  class="dropdown-toggle" data-toggle="dropdown" href="">SEM-INTERNAL <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="seminternal.py?poiuytrewq=%s">MACHINE LEARNING</a></li>
                    <li><a href="javainter.py?poiuytrewq=%s">ADVANCED JAVA </a></li>
                    <li><a href="webinter.py?poiuytrewq=%s">WEB TECHNOLOGY</a></li>
                </ul></li>
                <li><a href="practical.py?poiuytrewq=%s">PRACTICAL</a></li>
                <li class="dropdown"><a href="semmark.py?poiuytrewq=%s">SEM-MARK </a></li>

            </ul>
            </div>"""%(you[0],uid, uid, uid, uid, uid, uid, uid, uid, uid, uid))
print("""
<div class="container dt">
<div>
<a href=""><img src="" alt="std image" width="200px" height="200px"></a>
<a href="stddetail.py?poiuytrewq=%s"><h4>STUDENT DETAILS</h4></a>
</div>
<div>
<a href=""><img src="" alt="markssheet" width="200px" height="200px"></a>
<a href="userdash.py?poiuytrewq=%s"><h4>MARKSHEETS</h4></a>
</div>
</div>
</body>
</html>
"""%(uid,uid))