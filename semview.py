#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os
import itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEM MARKS</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
    .ty{
   text-align:center;
   background-image:linear-gradient(blue,green);
   color:transparent;
   background-clip: text;
   }
    nav{
    width:100%;
    }
    .mm{
    overflow-x: scroll;
   }
       #menus{
    position: absolute;
    /* background-image: linear-gradient(to right,gray,white); */
    background-color: lightgray;
    margin-top: 0%;
   }
   .uli{
    position: absolute;
    background-color: aqua;
    text-align: center;
   }
   .uli>ul>li{
    list-style-type: none;
   }
   .ol>li>a{
    color:black;
    text-decoration: none;
   }
   .ol>li>a:hover{
    color: lightgoldenrodyellow;
   }
   .ol>li{
    padding: 10px;
    margin-left: 10px;
    font-weight: bold;
    font-size: 18px;
    list-style-type: none;
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
    <div class="hg">
    <h1 class="ty">SEM MARKSHEET</h1>
    </div>

    <div class="container">
      <form enctype = "multipart/form-data" method = "post">   
<div class="mm">
    <table class="table table-hover table-striped table-bordered">
         <tr>
            <th colspan="2"></th>
            <th colspan="3">INTERNAL</th>
            <th colspan="3">EXTERNAL</th>
            <th colspan="3">TOTAL</th>

        </tr>

        <tr>
            <th>ROLL NO</th>
            <th>NAME</th>
            <th> MACHINE LEARNING</th>
            <th>WEB TECH</th>
            <th>JAVA ADVANCE</th>
            <th> MACHINE LEARNING</th>
            <th>WEB TECH</th>
            <th>JAVA ADVANCE</th>
            <th> MACHINE LEARNING</th>
            <th>WEB TECH</th>
            <th>JAVA ADVANCE</th>
        </tr>
        """)
p = """select regno,name,mli,wdi,javai,eml,ewd,ejava,ml,wd,java from semmark order by regno"""
cur.execute(p)
hot = cur.fetchall()
for i in hot:
    if (i[5]==0):
        c="AA"
    else:
        c=i[5]
    if (i[6]==0):
        d="AA"
    else:
        d=i[6]
    if (i[7]==0):
        e="AA"
    else:
        e=i[7]
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
        </tr>""" % (i[0], i[1], i[2],i[3],i[4],c,d,e,i[8],i[9],i[10]))
print("""
    </table>
    </div>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>
</html>""")