#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb,itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PRACTICAL</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
        .kk{
   text-align:center;
   background-image:linear-gradient(red,blue);
   color:transparent;
   background-clip: text;
   }
     .mm{
    overflow-x: scroll;
   }    #menus{
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
    <div class="container-fluid">

     <h1 class="kk">PRACTICAL MARKSHEET</h1>
<div class="ji">
    <a href="practicaledit.py"><button class="btn btn-primary btn-lg">Edit</button></a>
    </div>
    <br>
 <form enctype = "multipart/form-data" method = "post"> 
    <div class="mm">
    <table class="table table-responsive table-hover table-striped table-bordered om">
        <tr>
            <th colspan="2"></th>
            <th colspan="3">INTERNAL</th>
            <th colspan="2">EXTERNAL</th>
            
        </tr>
        <tr>
            <th>ROLL NO</th>
            <th>NAME</th>
            <th>REGULAR</th>
            <th>OBSERVATION</th>
            <th>MODEL/VIVA</th>
            <th>RECORD</th>
            <th>PRACTICAL</th>
        </tr>""")
p = """select regno,name from register order by regno"""
cur.execute(p)
hot = cur.fetchall()
for i in hot:
    print("""
        <tr>
         <td>%s</td>
           <td>%s</td>
           <td><input type="text" name="reg" class="regular" required></td>
           <td><input type="text" name="obs" class="obser" required ></td>
           <td><input type="text" name="viva" class="viva" required></td>
           <td><input type="text" name="recs" class="record" required></td>
           <td><input type="text" name="pra" class="pra" required ></td>
 
        </tr>"""%(i[0],i[1]))


print("""
    </table>
</div>
    <input type="submit" placeholder="submit"  class="btn btn-success btn-lg" name="upt">
""")

k=cgi.FieldStorage()

reg=k.getvalue("reg")
obs=k.getvalue("obs")
viva=k.getvalue("viva")
recs=k.getvalue("recs")
pra=k.getvalue("pra")
submit=k.getvalue("upt")


if submit != None:
    for (i, y, z, k,j,l) in itertools.zip_longest(hot, reg,obs, viva,recs,pra):
        a = int(y)
        b = int(z)
        if "A" in k:
            c =0
        else:
            c = int(k)
        d = int(j)
        if "A" in l:
            e=0
        else:
            e = int(l)
        b= a + b + c + d + e
        jk="""insert into practical (regno,name,regular,observation,viva,records,external,total) values ('%s','%s','%s','%s','%s','%s','%s','%s')on duplicate key update name=values(name),regular=values(regular),observation=values(observation),viva=values(viva),records=values(records),external=values(external),total=values(total)""" %(i[0],i[1],y,z,k,j,l,b)
        cur.execute(jk)
        con.commit()
        print("""
            <script>
              alert("marks Insert successfully");
            
              </script>""")

print("""
</form>
</div>
<script>
    document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".regular")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (/[^0-9]/.test(values)||(values && (Number(values) < 0 || Number(values) > 10))){
                    alert("Marks upto 10. Invalid characters are not allowed ")
                    input.value=""
                }
            })
        })
    })
    document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".obser")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (/[^0-9]/.test(values)||(values && (Number(values) < 0 || Number(values) > 10))){
                    alert("Marks upto 10. Invalid characters are not allowed ")
                    input.value=""
                }
            })
        })
    })
    document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".viva")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (!((values >= 0 && values <=20) || values === 'A')){
                    alert("Marks upto 20. Invalid characters are not allowed ")
                    input.value=""
                }
            })
        })
    })
    document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".record")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (/[^0-9]/.test(values)||(values && (Number(values) < 0 || Number(values) > 10))){
                    alert("Marks upto 10. Invalid characters are not allowed ")
                    input.value=""
                }
            })
        })
    })
    document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".pra")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (!((values >= 0 && values <=50) || values === 'A')){
                    alert("Marks upto 50. Invalid characters are not allowed ")
                    input.value=""
                }
            })
        })
    })
</script>

    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>
</html>
""")