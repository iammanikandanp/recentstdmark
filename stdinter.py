#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

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
    <title>Internal MARKS</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
    th,td{
    text-align:center;}
    
    .lk{
    width: 300px;}
    .dd{
    display:inline;
    margin-left:30px;
    }
    .mr{
    margin-left:70px;}
    
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
           
        </div>
     <div class="hg">
    <h1 class="ty">ALL INTERNAL MARKSHEET</h1>
    </div>
    <div class="mk">
   


<div class="container">
     <table class="table"  border="1px">
            <tr>
                <th colspan="2"></th>

                    <th colspan="3">internal 1</th>  
             <th colspan="3">internal 2</th>   
             <th colspan="3">internal 3</th>   
             
                     
            </tr>
            <tr>
                <th>REGNO</th>
                <th>NAME</th>
                <th>MACHINE LEARNING</th>
                <th>WEB TECHNOLOGY</th>
                <th>ADVANCED JAVA</th>
                <th>MACHINE LEARNING</th>
                <th>WEB TECHNOLOGY</th>
                <th>ADVANCED JAVA</th>
                <th>MACHINE LEARNING</th>
                <th>WEB TECHNOLOGY</th>
                <th>ADVANCED JAVA</th>
            </tr>
            """)
p = """select rego,name,mli,wdi,javai from internal where rego='%s' """%(uid)
cur.execute(p)
pri = cur.fetchone()
o = """select mli,wdi,javai from internal2 where regno='%s' """%(uid)
cur.execute(o)
pr = cur.fetchone()

ug = """select mli,wdi,javai from internal3 where regno='%s' """%(uid)
cur.execute(ug)
prl = cur.fetchone()
print("""
            <tr>
                <td>%s</td>
                <td >%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
        """ % (pri[0],pri[1],pri[2],pri[3],pri[4],pr[0],pr[1],pr[2],prl[0],prl[1],prl[2]))
print("""
</table>
<div class="nh container">
    <h1 class="ty">MODEL MARKSHEET</h1>

 <table class="table table-hover table-striped table-bordered">
        <tr>
            <th>ROLL NO</th>
            <th>NAME</th>
           <th>MACHINE LEARNING</th>
                <th>WEB TECHNOLOGY</th>
                <th>ADVANCED JAVA</th>
        </tr>
        """)
iu="""select regno,name,mli,wdi,javai from model where regno='%s' """%(uid)
cur.execute(iu)
jio=cur.fetchone()
print("""
    <tr>
        <td>%s</td>
        <td >%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        </tr>"""%(jio[0],jio[1],jio[2],jio[3],jio[4]))

print("""
</table>
</div>
<h1 class="ty">SEM-INTERNAL</h1>
<table class="table table-hover table-striped table-bordered ">
<tr>
<th>REGNO</th>
<th>NAME</th>
<th>TITLE</th>
<th>INTERNAL</th>
<th>EXTERNAL</th>
<th>ATTENDANCE</th>
<th>ASS/SEMINOR</th>
<th>TOTAL</th>
</tr>""")
po="""select regno,name,internal,model,attendance,sem,total from semint where regno='%s' """%(uid)
cur.execute(po)
wow=cur.fetchone()
print("""
<tr>
<td>%s</td>
<td>%s</td>
<td>MACHINE LEARNING</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
</tr>"""%(wow[0],wow[1],wow[2],wow[3],wow[4],wow[5],wow[6]))
pow="""select regno,name,internal,model,attendance,sem,total from webinter where regno='%s' """%(uid)
cur.execute(pow)
wo=cur.fetchone()
print("""
<tr>
<td>%s</td>
<td>%s</td>
<td>WEB TECHNOLOGY</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
</tr>"""%(wo[0],wo[1],wo[2],wo[3],wo[4],wo[5],wo[6]))
ow="""select regno,name,internal,model,attendance,sem,total from javainter where regno='%s' """%(uid)
cur.execute(ow)
wol=cur.fetchone()
print("""
<tr>
<td>%s</td>
<td>%s</td>
<td>ADVANCED JAVA</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
</tr>
"""%(wol[0],wol[1],wol[2],wol[3],wol[4],wol[5],wol[6]))
print("""
</table>
</div>
<script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
     </body>
     </html>""")

