#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb,itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
r=cgi.FieldStorage()
uid=r.getvalue("poiuytrewq")
id=r.getvalue("lkjhgfdsa")
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Userdash</title>
    <link rel="icon" href="" type="image/x-icon">
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/userdash.css">

    
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
                    <h3 name="uname">Username</h3>
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
                   
            </ul>"""%(uid,uid,uid,uid,uid,uid,uid,uid,uid,uid))
print("""
        </div>
        <div class="sec container">
        <div class="flip-box ">
            <div class="flip-box-inner">
              <div class="flip-box-front">
                <h2>INTERNAL</h2>
                <ul style="margin-top: 25px;">
                  <li>Internal exam are conduct <u>25 MARKS</u><b>.</b></li>
                  <li>Each Internal Marks is convert by <u>2.5</u><b>.</b></li>
                  <li>3 Internal marks to Add best <br>Two Internal marks </li>
                <li><b>Tab to Insert marks</b></li>
                </ul>
                
              </div>
              <div class="flip-box-back">
                <ul class="kj">
                    <li><a href="stddash.py?poiuytrewq=%s"><button class="btn btn-primary">INTERNAL 1</button></a></li>
                    <li><a href="internal2.py?poiuytrewq=%s"><button class="btn btn-danger">INTERNAL 2</button></a></li>
                    <li><a href="internal3.py?poiuytrewq=%s"><button class="btn btn-warning">INTERNAL 3</button></a></li>
                    <li><a href="demo.py?poiuytrewq=%s"><button class="btn btn-success">INTERNAL CONVERT</button></a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="flip-box flip-box1">
            <div class="flip-box-inner flip-box-inner1">
              <div class="flip-box-front">
                <h2>MODEL</h2>
                <ul style="margin-top: 25px;">
                  <li>Model exam are conduct <u>75 MARKS</u><b>.</b></li>
                  <li>Each Internal Marks is convert by <u>10</u><b>.</b></li>
                <li style="margin-top: 20px;"><b>Tab to Insert marks</b></li>
                </ul>
              </div>
              <div class="flip-box-back flip-box-back1">
                <h2>MODEL</h2>
                <a href="model.py?poiuytrewq=%s"><button class="btn btn-danger btn-lg" style="margin-top: 30px;">MODEL</button></a>
              </div>
            </div>
          </div>
          <div class="flip-box">
            <div class="flip-box-inner">
              <div class="flip-box-front">
                <h2>SEM-INTERNAL</h2>
                <ul style="margin-top: 15px;">
                  <li>Sem-Internal are <u>25 MARKS</u><b>.</b></li>
                  <li>Includes 
                    <ul><li>Internal mark <u>2.5</u><b>.</b></li>
                  <li>Model<u>10</u><b>.</b> Attendance <u>5</u><b>.</b><br>
                  Semnior/Assignment<u>5</u><b>.</b> </li>
                <li><b>Tab to Insert marks</b></li>
                </ul>
                </ul>
                
              </div>
              <div class="flip-box-back">
                <ul class="kj">
                    <li><a href="seminternal.py?poiuytrewq=%s"><button class="btn btn-primary">MACHINE LEARNING</button></a></li>
                    <li><a href="webinter.py?poiuytrewq=%s"><button class="btn btn-danger">WEB TECHNOLOGY</button></a></li>
                    <li><a href="javainter.py?poiuytrewq=%s"><button class="btn btn-warning">ADVANCED JAVA</button></a></li>
                    <li><a href="semtotal.py?poiuytrewq=%s"><button class="btn btn-success ">TOTAL</button></a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="flip-box flip-box1">
            <div class="flip-box-inner flip-box-inner1">
              <div class="flip-box-front">
                <h2>PRACTICAL</h2>
                <ul style="margin-top: 25px;">
                  <li>Practical exam are conduct <u>100 MARKS</u><b>.</b></li>
                  <li>Internal <u>40</u><b>.</b></li>
                  <li>External <u>60</u><b>.</b></li>
                <li style="margin-top: 20px;"><b>Tab to Insert marks</b></li>
                </ul>
              </div>
              <div class="flip-box-back flip-box-back1">
                <h2>PRACTICAL</h2>
                <a href="practical.py?poiuytrewq=%s"><button class="btn btn-danger btn-lg" style="margin-top: 30px;">PRACTICAL</button></a>
              </div>
            </div>
          </div>
          <div class="flip-box">
            <div class="flip-box-inner ">
              <div class="flip-box-front">
                <h2>SEM-MARK</h2>
                <ul style="margin-top: 25px;">
                  <li>Sem exam are conduct <u>100 MARKS</u><b>.</b></li>
                  <li>Internal <u>25</u><b>.</b></li>
                  <li>External <u>75</u><b>.</b></li>
                <li style="margin-top: 20px;"><b>Tab to Insert marks</b></li>
                </ul>
              </div>
              <div class="flip-box-back ">
                <h2>SEM-MARK</h2>
                <a href="semmark.py?poiuytrewq=%s"><button class="btn btn-danger btn-lg" style="margin-top: 30px;">SEM-MARK</button></a>
              </div>
            </div>
          </div>
        
        <div class="flip-box flip-box1">
          <div class="flip-box-inner flip-box-inner1">
            <div class="flip-box-front">
              <h2>STUDENT MARKS</h2>
              <ul style="margin-top: 25px;">
                <li>View all student marks</li>
                <li style="margin-top: 7px;"> Total sem-mark <u>100</u><b>.</b></li>
                
              <li style="margin-top: 20px;"><b>Tab to Insert marks</b></li>
              </ul>
            </div>
            <div class="flip-box-back flip-box-back1">
              <h2>STUDENT MARKS</h2>
              <a href="semview.py?poiuytrewq=%s"><button class="btn btn-danger btn-lg" style="margin-top: 30px;">STUDENT MARKS</button></a>
            </div>
          </div>
        </div>
      </div>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>

</html>
"""%(uid,uid,uid,uid,uid,uid,uid,uid,uid,uid,uid,uid))