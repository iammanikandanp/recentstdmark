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
ry="""select regno,id,name from register where regno='%s'"""%(uid)
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
            </div>
  """%(you[2]))
print("""
<div class="container dt">
<div>
<a href=""><img src="" alt="std image" width="200px" height="200px"></a><br>
<a href="stdview.py?poiuytrewq=%s"><h4 class="kj">STUDENT DETAILS</h4></a>
</div>
<div>
<a href=""><img src="" alt="markssheet" width="200px" height="200px"></a><br>
<a href="stdinter.py?poiuytrewq=%s"><h4 class="kj">MARKSHEETS</h4></a>
</div>
<div>
<a href=""><img src="" alt="sem mark" width="200px" height="200px"></a><br>
<a href="stdmark.py?poiuytrewq=%s"><h4 class="kj">SEM-MARK</h4></a>
</div>
</div>
</body>
</html>
"""%(uid,uid,uid))