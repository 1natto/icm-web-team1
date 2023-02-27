from flask import Flask, render_template, request, redirect, url_for, Response
import os

app = Flask(__name__)



#-----------default ny
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
@app.route("/draft1/", methods=['GET'])
def submit():
    return render_template("submit.html")
@app.route("/draft2/", methods=['GET'])
def ny2():
    return render_template("ny2.html")
@app.route("/ny3/", methods=['GET'])
def ny3():
    return render_template("ny3.html")
@app.route("/ny4/", methods=['GET'])
def ny4():
    return render_template("ny4.html")
@app.route("/ny5/", methods=['GET'])
def ny5():
    return render_template("ny5.html")
@app.route("/ny6/", methods=['GET'])
def ny6():
    return render_template("ny6.html")

#-----------------(thaophuongne1)
@app.route("/dGhhb3BodW9uZ25lMTM=/", methods=['GET'])
def thaophuongne1():
    return render_template("thaophuongne1.html")
@app.route("/dGhhb3BodW9uZ25lMTM=1/", methods=['GET'])
def thaophuongne2():
    return render_template("thaophuongne2.html")

#---------------dtrang05

@app.route("/ZHRyYW5nMDU=/", methods=['GET'])
def dtrang1():
    return render_template("dtrang1.html")
@app.route("/ZHRyYW5nMDU=1/", methods=['GET'])
def dtrang2():
    return render_template("dtrang2.html")
@app.route("/ZHRyYW5nMDU=2/", methods=['GET'])
def dtrang3():
    return render_template("dtrang3.html")

#----------phamhongthang0705

@app.route("/cGhhbWhvbmd0aGFuZwo=/", methods=['GET'])
def phamhongthang1():
    return render_template("phamhongthang.html")

#---------hoangphuck43tnhk4hp

@app.route("/aG9hbmdwaHVjaw==/", methods=['GET'])
def hoangphuck():
    return render_template("hoangphuck1.html")
@app.route("/aG9hbmdwaHVjaw==1/", methods=['GET'])
def hoangphuck2():
    return render_template("hoangphuck2.html")
@app.route("/aG9hbmdwaHVjaw==2/", methods=['GET'])
def hoangphuck3():
    return render_template("hoangphuck3.html")
@app.route("/aG9hbmdwaHVjaw==3/", methods=['GET'])
def hoangphuck4():
    return render_template("hoangphuck4.html")

#----------thucbao21122007

@app.route("/dGh1Y2JhbwoK/", methods=['GET'])
def thucbao1():
    return render_template("thucbao1.html")
@app.route("/dGh1Y2JhbwoK1/", methods=['GET'])
def thucbao2():
    return render_template("thucbao2.html")
@app.route("/dGh1Y2JhbwoK2/", methods=['GET'])
def thucbao3():
    return render_template("thucbao3.html")
@app.route("/dGh1Y2JhbwoK3/", methods=['GET'])
def thucbao4():
    return render_template("thucbao4.html")
@app.route("/dGh1Y2JhbwoK4/", methods=['GET'])
def thucbao5():
    return render_template("thucbao5.html")

#-------------Dha162162

@app.route("/RGhhMTYyMTYyCg==/", methods=['GET'])
def dha1():
    return render_template("dha1.html")
@app.route("/RGhhMTYyMTYyCg==1/", methods=['GET'])
def dha2():
    return render_template("dha2.html")
@app.route("/RGhhMTYyMTYyCg==2/", methods=['GET'])
def dha3():
    return render_template("dha3.html")
@app.route("/RGhhMTYyMTYyCg==3/", methods=['GET'])
def dha4():
    return render_template("dha4.html")


#-------------------giabaott.2007.01

@app.route("/Z2lhYmFvdHQK/", methods=['GET'])
def giabaott1():
    return render_template("giabaott1.html")
@app.route("/Z2lhYmFvdHQK1/", methods=['GET'])
def giabaott2():
    return render_template("giabaott2.html")
@app.route("/Z2lhYmFvdHQK2/", methods=['GET'])
def giabaott3():
    return render_template("giabaott3.html")

#------phuclam10hp

@app.route("/cGh1Y2xhbTEwaHAK/", methods=['GET'])
def phuclam10hp1():
    return render_template("phuclam10hp1.html")
@app.route("/cGh1Y2xhbTEwaHAK1/", methods=['GET'])
def phuclam10hp2():
    return render_template("phuclam10hp2.html")
@app.route("/cGh1Y2xhbTEwaHAK2/", methods=['GET'])
def phuclam10hp3():
    return render_template("phuclam10hp3.html")
@app.route("/cGh1Y2xhbTEwaHAK3/", methods=['GET'])
def phuclam10hp4():
    return render_template("phuclam10hp4.html")


#----------cmtri

@app.route("/Y210cmkKCg==/", methods=['GET'])
def cmtri1():
    return render_template("cmtri1.html")
@app.route("/Y210cmkKCg==1/", methods=['GET'])
def cmtri2():
    return render_template("cmtri2.html")

#--------nguyenhongnhung

@app.route("/bmd1eWVuaG9uZ25odW5nIAo=/", methods=['GET'])
def nguyenhongnhung1():
    return render_template("nguyenhongnhung1.html")

#------------quynhanhhoangg

@app.route("/cXV5bmhhbmhob2FuZ2cK/", methods=['GET'])
def quynhanhhoangg1():
    return render_template("quynhanhhoangg1.html")

#------------linh.s

@app.route("/bGluaC5zCg==/", methods=['GET'])
def linhs1():
    return render_template("linhs1.html")
@app.route("/bGluaC5zCg==1/", methods=['GET'])
def linhs2():
    return render_template("linhs2.html")
@app.route("/bGluaC5zCg==2/", methods=['GET'])
def linhs3():
    return render_template("linhs3.html")
@app.route("/bGluaC5zCg==3/", methods=['GET'])
def linhs4():
    return render_template("linhs4.html")

if __name__ == '__main__':
   app.run()
