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
#1
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
#2
@app.route("/bGluaC5zCg==4/", methods=['GET'])
def linhs5():
    return render_template("linhs5.html")
@app.route("/bGluaC5zCg==5/", methods=['GET'])
def linhs6():
    return render_template("linhs6.html")
@app.route("/bGluaC5zCg==6/", methods=['GET'])
def linhs7():
    return render_template("linhs7.html")
@app.route("/bGluaC5zCg==7/", methods=['GET'])
def linhs8():
    return render_template("linhs8.html")

#---------nhaminh1707
@app.route("/bmhhbWluaAo=/", methods=['GET'])
def nhaminh1():
    return render_template("nhaminh1.html")

#-------quannamkhanh
@app.route("/cXVhbm5hbWtoYW5o/", methods=['GET'])
def quannamkhanh1():
    return render_template("quannamkhanh1.html")
@app.route("/cXVhbm5hbWtoYW5o1/", methods=['GET'])
def quannamkhanh2():
    return render_template("quannamkhanh2.html")

#---------tatuanthanh 1+2+3

@app.route("/dGF0dWFudGhhbmg=/", methods=['GET'])
def tatuanthanh1():
    return render_template("tatuanthanh1.html")
@app.route("/dGF0dWFudGhhbmg=1/", methods=['GET'])
def tatuanthanh2():
    return render_template("tatuanthanh2.html")
@app.route("/dGF0dWFudGhhbmg=2/", methods=['GET'])
def tatuanthanh3():
    return render_template("tatuanthanh3.html")
@app.route("/dGF0dWFudGhhbmg=3/", methods=['GET'])
def tatuanthanh4():
    return render_template("tatuanthanh4.html")
@app.route("/dGF0dWFudGhhbmg=4/", methods=['GET'])
def tatuanthanh5():
    return render_template("tatuanthanh5.html")
@app.route("/dGF0dWFudGhhbmg=5/", methods=['GET'])
def tatuanthanh6():
    return render_template("tatuanthanh6.html")

#------canoc1822007

@app.route("/Y2Fub2MxODIyMDA3/", methods=['GET'])
def canoc1():
    return render_template("canoc1.html")

#-------nganv

@app.route("/bmdhbnY=/", methods=['GET'])
def nganv1():
    return render_template("nganv1.html")
@app.route("/bmdhbnY=1/", methods=['GET'])
def nganv2():
    return render_template("nganv2.html")

#---------damquangduy

@app.route("/ZGFtcXVhbmdkdXk==/", methods=['GET'])
def damquangduy1():
    return render_template("damquangduy1.html")
@app.route("/ZGFtcXVhbmdkdXk==1/", methods=['GET'])
def damquangduy2():
    return render_template("damquangduy2.html")
@app.route("/ZGFtcXVhbmdkdXk==2/", methods=['GET'])
def damquangduy3():
    return render_template("damquangduy3.html")
@app.route("/ZGFtcXVhbmdkdXk==3/", methods=['GET'])
def damquangduy4():
    return render_template("damquangduy4.html")

#-------nguyentuongvi

@app.route("/bmd1eWVudHVvbmd2aQ==/", methods=['GET'])
def nguyentuongvi1():
    return render_template("nguyentuongvi1.html")
@app.route("/bmd1eWVudHVvbmd2aQ==1/", methods=['GET'])
def nguyentuongvi2():
    return render_template("nguyentuongvi2.html")
@app.route("/bmd1eWVudHVvbmd2aQ==2/", methods=['GET'])
def nguyentuongvi3():
    return render_template("nguyentuongvi3.html")
@app.route("/bmd1eWVudHVvbmd2aQ==3/", methods=['GET'])
def nguyentuongvi4():
    return render_template("nguyentuongvi4.html")

#-----quochung06hp

#1
@app.route("/cXVvY2h1bmcwNmhw/", methods=['GET'])
def quochung06hp1():
    return render_template("quochung06hp1.html")
@app.route("/cXVvY2h1bmcwNmhw1/", methods=['GET'])
def quochung06hp2():
    return render_template("quochung06hp2.html")
@app.route("/cXVvY2h1bmcwNmhw2/", methods=['GET'])
def quochung06hp3():
    return render_template("quochung06hp3.html")
@app.route("/cXVvY2h1bmcwNmhw3/", methods=['GET'])
def quochung06hp4():
    return render_template("quochung06hp4.html")

#2
@app.route("/cXVvY2h1bmcwNmhw4/", methods=['GET'])
def quochung06hp5():
    return render_template("quochung06hp5.html")
@app.route("/cXVvY2h1bmcwNmhw5/", methods=['GET'])
def quochung06hp6():
    return render_template("quochung06hp6.html")
@app.route("/cXVvY2h1bmcwNmhw6/", methods=['GET'])
def quochung06hp7():
    return render_template("quochung06hp7.html")
@app.route("/cXVvY2h1bmcwNmhw7/", methods=['GET'])
def quochung06hp8():
    return render_template("quochung06hp8.html")

#-------hanhoahau5

@app.route("/aGFuaG9haGF1NQ==/", methods=['GET'])
def hanhoahau51():
    return render_template("hanhoahau51.html")
@app.route("/aGFuaG9haGF1NQ==1/", methods=['GET'])
def hanhoahau52():
    return render_template("hanhoahau52.html")
@app.route("/aGFuaG9haGF1NQ==2/", methods=['GET'])
def hanhoahau53():
    return render_template("hanhoahau53.html")
@app.route("/aGFuaG9haGF1NQ==3/", methods=['GET'])
def hanhoahau54():
    return render_template("hanhoahau54.html")

#-----dxtruonganh

@app.route("/ZHh0cnVvbmdhbmg=/", methods=['GET'])
def dxtruonganh1():
    return render_template("dxtruonganh1.html")

#--------duongmocnhien

@app.route("/ZHVvbmdtb2NuaGllbg==/", methods=['GET'])
def duongmocnhien1():
    return render_template("duongmocnhien1.html")
@app.route("/ZHVvbmdtb2NuaGllbg==1/", methods=['GET'])
def duongmocnhien2():
    return render_template("duongmocnhien2.html")

#------trannhannhatminh

@app.route("/dHJhbm5oYW5uaGF0bWluaA==/", methods=['GET'])
def trannhannhatminh1():
    return render_template("trannhannhatminh1.html")
@app.route("/dHJhbm5oYW5uaGF0bWluaA==1/", methods=['GET'])
def trannhannhatminh2():
    return render_template("trannhannhatminh2.html")
@app.route("/dHJhbm5oYW5uaGF0bWluaA==2/", methods=['GET'])
def trannhannhatminh3():
    return render_template("trannhannhatminh3.html")
@app.route("/dHJhbm5oYW5uaGF0bWluaA==3/", methods=['GET'])
def trannhannhatminh4():
    return render_template("trannhannhatminh4.html")


#-------lyphan

@app.route("/bHlwaGFu/", methods=['GET'])
def lyphan1():
    return render_template("lyphan1.html")

if __name__ == '__main__':
   app.run()
