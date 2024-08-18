#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os
import itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
pr = cgi.FieldStorage()
uid=pr.getvalue("poiuytrewq")
id=pr.getvalue("lkjhgfdsa")
o = """select regno,name from register"""
cur.execute(o)
hot = cur.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal 2</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
    .ty{
   text-align:center;
   background-image:linear-gradient(red,blue);
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
  .ji{
  display:flex;
  justify-content:end;
  margin-right:20px;
  }
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
                    <h3 name="uname">Username</h3>
                </div>
            </div>
            <ul class="ol">
                <li><a href="stddash.py?poiuytrewq=%s">INTERNAL 1</a></li>
                <li><a href="internal2.py?poiuytrewq=%s">INTERNAL 2 </a></li>
                <li><a href="internal2.py?poiuytrewq=%s">INTERNAL 3 </a></li>
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
     <div class="hg">
    <h1 class="ty">2 INTERNAL MARKSHEET</h1>
    </div>
  <div class="ji">
    <a href="intern2edit.py"><button class="btn btn-primary btn-lg">Edit</button></a>
    </div>
    <div class="container">
      <form enctype = "multipart/form-data" method = "post">   
<div class="mm">
    <table class="table table-hover table-striped table-bordered">
        <tr>
          <th>ROLL NO</th>
            <th>NAME</th>
            <th> MACHINE LEARNING</th>
            <th>WEB TECH</th>
            <th>JAVA ADVANCE</th>
        </tr>
        """)
p = """select regno,name from register order by regno"""
cur.execute(p)
hot = cur.fetchall()
for i in hot:
    print("""

        <tr>
           <td>%s</td>
           <td>%s</td>
           <td><input type="text" name="ml" class="mani" required ></td>
           <td><input type="text" name="wb" class="mani" required ></td>
           <td><input type="text" name="java" class="mani" required  ></td>
        </tr>""" % (i[0], i[1]))
print("""
    </table>
    </div>
    <a href=""><button class="btn btn-success btn-lg" name="upt">submit</button></a>
""")


ml = pr.getvalue("ml")
wb = pr.getvalue("wb")
java = pr.getvalue("java")
submit = pr.getvalue("upt")

if submit != None:
    for (i, y, z, k) in itertools.zip_longest(hot, ml, wb, java):
        if "A" in (y and z and k):
            if "A" in y:
                iml = y
            else:
                iml = int(y) / 10
            if "A" in z:
                iwb = z
            else:
                iwb = int(z) / 10
            if "A" in k:
                ijava = k
            else:
                ijava = int(k) / 10
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
            i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                              alert("marks all a successfully ");
                              </script>""")
        elif "A" in (y and z):
            if "A" in y:
                iml = y
            else:
                iml = int(y) / 10
            if "A" in z:
                iwb = z
            else:
                iwb = int(z) / 10
            ijava = int(k) / 10
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
            i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                      alert("marks first 2 successfully ");
                      </script>""")
        elif "A" in (y and k):
            if "A" in y:
                iml = y
            else:
                iml = int(y) / 10
            if "A" in k:
                ijava = k
            else:
                ijava = int(k) / 10
            iwb=int(z)/10
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
            i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                      alert("marks first and last successfully ");
                      </script>""")
        elif "A" in (z and k):
            iml = y / 10
            if "A" in z:
                iwb = z
            else:
                iwb = int(z) / 10
            if "A" in k:
                ijava = k
            else:
                ijava = int(k) / 10
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
            i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                  alert("marks econd and third successfully ");

                  </script>""")
        elif "A" in y:
            iml=y
            iwb=int(z)/10
            ijava=int(k)/10
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
                i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                              alert("marks first successfully ");

                              </script>""")
        elif "A" in z:
            iml=int(y)/10
            iwb=z
            ijava=int(k)/10
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
                i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                              alert("marks first successfully ");

                              </script>""")
        elif "A" in k:
            iml=int(y)/10
            iwb=int(z)/10
            ijava=k
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
                i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                              alert("marks first successfully ");

                              </script>""")
        else:
            iml = int(y) / 10
            iwb = int(z) / 10
            ijava = int(k) / 10
            gh = """insert into internal2 (regno,name,ml,wd,java,mli,wdi,javai) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),ml=values(ml),wd=values(wd),java=values(java),mli=values(mli),wdi=values(wdi),javai=values(javai)""" % (
            i[0], i[1], y, z, k, iml, iwb, ijava)
            cur.execute(gh)
            con.commit()
            print(gh)
            print("""<script>
                              alert("marks a and y successfully ");
                              </script>""")

print("""
</form>
</div>

<script>
    document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".mani")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (!((values >= 0 && values <=25) || values === 'A')){
                    alert("Marks upto 25. Invalid characters are not allowed ")
                    input.value=""
                }else{
                     console.log(inputValue)
                   }
            })
        })
    })

</script>

    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>
</html>""")