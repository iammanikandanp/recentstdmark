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
fid=oo.getvalue("lkjhgfdsa")
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Userdash</title>
    <link rel="icon" href="" type="image/x-icon">
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="style/internal.css">
    <style>
    p{
        margin: 0%;
    
    }
    .lk{
        font-size: small;
    }
    th{
        text-align: center;
    }
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
        .rd{
            text-align: left;
        }
      .rr{
        text-align: right;
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
        <h1 class="kk">SEM-INTERNAL</h1>
        <div class="kl container">
        <table class="table table-bordered table-striped table-hover ">
           
           
            <tr>
                <th colspan="8"><p>ERODE ARTS AND SCIENCE COLLEGE </p>
                    <p class="lk">(Autonomous-Accredited by NAAC A+Level)</p>
                    <p>RANGAMPALAYAM,ERODE-638009,TAMILNADU</p>
                </th>
            </tr>
            <tr>
                <th colspan="8">PG RESEARCH DEPARTMENT OF COMPUTER SCIENCE<br>
                    <U>SEMESTER MARK RESULT</U><BR>
                    (2024-2025 ODD SEMESTER)
                </th>
            </tr>
        <tr >
        """)
ty="""select dob from register where regno='%s' """%(uid)
cur.execute(ty)
now=cur.fetchone()
yu="""select regno,name,mli,wdi,javai,eml,ewd,ejava,ml,wd,java from semmark where regno='%s' """%(uid)
cur.execute(yu)
hot=cur.fetchone()

print("""
                <th class="rd" colspan="3">Register No : %s</th>
                <td class="rr" colspan="5">Exam.Ref : DEC42</td>
            </tr>
            <tr>
                <th class="rd" colspan="3">NAME : %s</th>
                <td class="rr" colspan="5">Degree : MCAMC</td>
            </tr>
            <tr>
                <th c class="rd" colspan="3">DOB : %s</th>
                <td class="rr" colspan="5">Per.of.study : 2023-2025</td>
                </tr>"""%(hot[0],hot[1],now[0]))
print("""
            
            <tr>
            <th>SEM NO</th>
            <th>SUB.CODE</th>
            <th>TITLE</th>
            <th>C</th>
            <th>IA</th>
            <th>EA</th>
            <th>TOTAL</th>
            <th>RESULT</th>
            </tr>""")
c=hot[8]
if c >= 35:
    print("""      
                <tr>
                    <td>3</td>
                    <td>23MCA3</td>
                    <td>MACHINE LEARNING</td>
                    <td>5</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>p</td>
                    
                </tr>"""%(hot[2],hot[5],hot[8]))
elif c < 35:
    print("""      
                    <tr>
                        <td>3</td>
                        <td>23MCA3</td>
                        <td>MACHINE LEARNING</td>
                        <td>5</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>RA</td>

                    </tr>""" % (hot[2], hot[5], hot[8]))
d=hot[9]
if d >= 35:
   print("""      
            <tr>
                <td>3</td>
                <td>23MCA3</td>
                <td>WEB TECHNOLOGY</td>
                <td>5</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>p</td>

            </tr>"""%(hot[3],hot[6],hot[9]))
elif d < 35:
   print("""      
            <tr>
                <td>3</td>
                <td>23MCA3</td>
                <td>WEB TECHNOLOGY</td>
                <td>5</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>RA</td>

            </tr>"""%(hot[3],hot[6],hot[9]))
j=hot[10]
if j >=35:
    print("""      
                <tr>
                    <td>3</td>
                    <td>23MCA3</td>
                    <td>ADVANCED JAVA</td>
                    <td>5</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>p</td>
    
                </tr>"""%(hot[4],hot[7],hot[10]))
elif j < 35:
    print("""      
                <tr>
                    <td>3</td>
                    <td>23MCA3</td>
                    <td>ADVANCED JAVA</td>
                    <td>5</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>RA</td>

                </tr>""" % (hot[4], hot[7], hot[10]))
print("""
            <tr>
                <th colspan="8">AVERAGE : %s</th>
            </tr>
            <tr>
                <th colspan="8">PERCENTAGE : %s </th>
            </tr>
        </table>
    </div>""")
print("""
<script>
console.log("This web page partially developed by INBASARATHY [2ND MCA] Thanks for your contribute <3 ")
</script>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>
</html>""")