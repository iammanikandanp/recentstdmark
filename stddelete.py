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
fid=o.getvalue("stdregno")
ki="""select regno from register where regno='%s'"""% (fid)
cur.execute(ki)
tree=cur.fetchone()

if tree !=None:
    lk="""delete from register where regno='%s'"""% (fid)
    cur.execute(lk)
    con.commit()
    print("""
        <script>
        confirm("Are you sure to delete %s ?");
        </script>""")
    in1 = """delete from internal where rego='%s'""" % (fid)
    cur.execute(in1)
    con.commit()
    in2 = """delete from internal2 where regno='%s'""" % (fid)
    cur.execute(in2)
    con.commit()
    in3 = """delete from internal3 where regno='%s'""" % (fid)
    cur.execute(in3)
    con.commit()
    model = """delete from model where regno='%s'""" % (fid)
    cur.execute(model)
    con.commit()
    pra = """delete from practical where regno='%s'""" % (fid)
    cur.execute(pra)
    con.commit()
    semin = """delete from semint where regno='%s'""" % (fid)
    cur.execute(semin)
    con.commit()
    webin = """delete from webinter where regno='%s'""" % (fid)
    cur.execute(webin)
    con.commit()
    javain = """delete from javainter where regno='%s'""" % (fid)
    cur.execute(javain)
    con.commit()
    sem = """delete from semmark where regno='%s'""" % (fid)
    cur.execute(sem)
    con.commit()
    print("""
    <script>
    confirm("Are you sure to delete %s ?");
    location.href="stddetail.py?poiuytrewq=%s"
    </script>"""% (fid,uid))