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

#1
@app.route("/bmd1eWVuaG9uZ25odW5nIAo=/", methods=['GET'])
def nguyenhongnhung1():
    return render_template("nguyenhongnhung1.html")
#2
@app.route("/bmd1eWVuaG9uZ25odW5nIAo=1/", methods=['GET'])
def nguyenhongnhung2():
    return render_template("nguyenhongnhung2.html")

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
#3
@app.route("/bGluaC5zCg==8/", methods=['GET'])
def linhs9():
    return render_template("linhs9.html")
@app.route("/bGluaC5zCg==9/", methods=['GET'])
def linhs10():
    return render_template("linhs10.html")
@app.route("/bGluaC5zCg==10/", methods=['GET'])
def linhs11():
    return render_template("linhs11.html")
@app.route("/bGluaC5zCg==11/", methods=['GET'])
def linhs12():
    return render_template("linhs12.html")


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

#1
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

#2
@app.route("/ZGFtcXVhbmdkdXk==4/", methods=['GET'])
def damquangduy5():
    return render_template("damquangduy5.html")
@app.route("/ZGFtcXVhbmdkdXk==5/", methods=['GET'])
def damquangduy8():
    return render_template("damquangduy8.html")

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


#1
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

#2
@app.route("/dHJhbm5oYW5uaGF0bWluaA==4/", methods=['GET'])
def trannhannhatminh5():
    return render_template("trannhannhatminh5.html")
@app.route("/dHJhbm5oYW5uaGF0bWluaA==5/", methods=['GET'])
def trannhannhatminh6():
    return render_template("trannhannhatminh6.html")
@app.route("/dHJhbm5oYW5uaGF0bWluaA==6/", methods=['GET'])
def trannhannhatminh7():
    return render_template("trannhannhatminh7.html")
@app.route("/dHJhbm5oYW5uaGF0bWluaA==7/", methods=['GET'])
def trannhannhatminh8():
    return render_template("trannhannhatminh8.html")

#-------lyphan

@app.route("/bHlwaGFu/", methods=['GET'])
def lyphan1():
    return render_template("lyphan1.html")

#---------liquidconan

@app.route("/bGlxdWlkY29uYW4=/", methods=['GET'])
def liquidconan1():
    return render_template("liquidconan1.html")
@app.route("/bGlxdWlkY29uYW4=1/", methods=['GET'])
def liquidconan2():
    return render_template("liquidconan2.html")
@app.route("/bGlxdWlkY29uYW4=2/", methods=['GET'])
def liquidconan3():
    return render_template("liquidconan3.html")
@app.route("/bGlxdWlkY29uYW4=3/", methods=['GET'])
def liquidconan4():
    return render_template("liquidconan4.html")

#------vuphanhoanganh

@app.route("/dnVwaGFuaG9hbmdhbmg=/", methods=['GET'])
def vuphanhoanganh1():
    return render_template("vuphanhoanganh1.html")
@app.route("/dnVwaGFuaG9hbmdhbmg=1/", methods=['GET'])
def vuphanhoanganh2():
    return render_template("vuphanhoanganh2.html")
@app.route("/dnVwaGFuaG9hbmdhbmg=2/", methods=['GET'])
def vuphanhoanganh3():
    return render_template("vuphanhoanganh3.html")


#------ngduchuyhp
@app.route("/bmdkdWNodXlocA==/", methods=['GET'])
def ngduchuyhp1():
    return render_template("ngduchuyhp1.html")
@app.route("/bmdkdWNodXlocA==1/", methods=['GET'])
def ngduchuyhp2():
    return render_template("ngduchuyhp2.html")
@app.route("/bmdkdWNodXlocA==2/", methods=['GET'])
def ngduchuyhp3():
    return render_template("ngduchuyhp3.html")
@app.route("/bmdkdWNodXlocA==3/", methods=['GET'])
def ngduchuyhp4():
    return render_template("ngduchuyhp4.html")
@app.route("/bmdkdWNodXlocA==4/", methods=['GET'])
def ngduchuyhp5():
    return render_template("ngduchuyhp5.html")
@app.route("/bmdkdWNodXlocA==5/", methods=['GET'])
def ngduchuyhp6():
    return render_template("ngduchuyhp6.html")

#-----lelinh

@app.route("/bGVsaW5o/", methods=['GET'])
def lelinh1():
    return render_template("lelinh1.html")
@app.route("/bGVsaW5o1/", methods=['GET'])
def lelinh2():
    return render_template("lelinh2.html")
@app.route("/bGVsaW5o2/", methods=['GET'])
def lelinh3():
    return render_template("lelinh3.html")
@app.route("/bGVsaW5o3/", methods=['GET'])
def lelinh4():
    return render_template("lelinh4.html")

#-----kuro28

@app.route("/a3VybzI4/", methods=['GET'])
def kuro281():
    return render_template("kuro281.html")
@app.route("/a3VybzI41/", methods=['GET'])
def kuro282():
    return render_template("kuro282.html")
@app.route("/a3VybzI42/", methods=['GET'])
def kuro283():
    return render_template("kuro283.html")
@app.route("/a3VybzI43/", methods=['GET'])
def kuro284():
    return render_template("kuro284.html")

#------vanhatrinh

@app.route("/dmFuaGF0cmluaA==/", methods=['GET'])
def vanhatrinh1():
    return render_template("vanhatrinh1.html")
@app.route("/dmFuaGF0cmluaA==1/", methods=['GET'])
def vanhatrinh2():
    return render_template("vanhatrinh2.html")

#dongocminh

@app.route("/ZG9uZ29jbWluaA==/", methods=['GET'])
def dongocminh1():
    return render_template("dongocminh1.html")

#------ngocquang25

@app.route("/bmdvY3F1YW5nMjU=/", methods=['GET'])
def ngocquang251():
    return render_template("ngocquang251.html")
@app.route("/bmdvY3F1YW5nMjU=1/", methods=['GET'])
def ngocquang252():
    return render_template("ngocquang252.html")

#-------iamlunastarry

@app.route("/aWFtbHVuYXN0YXJyeQ==/", methods=['GET'])
def iamlunastarry1():
    return render_template("iamlunastarry1.html")
@app.route("/aWFtbHVuYXN0YXJyeQ==1/", methods=['GET'])
def iamlunastarry2():
    return render_template("iamlunastarry2.html")
@app.route("/aWFtbHVuYXN0YXJyeQ==2/", methods=['GET'])
def iamlunastarry3():
    return render_template("iamlunastarry3.html")
@app.route("/aWFtbHVuYXN0YXJyeQ==3/", methods=['GET'])
def iamlunastarry4():
    return render_template("iamlunastarry4.html")

#-------thanhdattranphu

@app.route("/dGhhbmhkYXR0cmFucGh1/", methods=['GET'])
def thanhdattranphu1():
    return render_template("thanhdattranphu1.html")
@app.route("/dGhhbmhkYXR0cmFucGh11/", methods=['GET'])
def thanhdattranphu2():
    return render_template("thanhdattranphu2.html")
@app.route("/dGhhbmhkYXR0cmFucGh12/", methods=['GET'])
def thanhdattranphu3():
    return render_template("thanhdattranphu3.html")
@app.route("/dGhhbmhkYXR0cmFucGh13/", methods=['GET'])
def thanhdattranphu4():
    return render_template("thanhdattranphu4.html")

#----dochi

@app.route("/ZG9jaGk=/", methods=['GET'])
def dochi1():
    return render_template("dochi1.html")

#-----khoa24

@app.route("/a2hvYTI0/", methods=['GET'])
def khoa241():
    return render_template("khoa241.html")

#------le37

@app.route("/bGUzNw==/", methods=['GET'])
def le371():
    return render_template("le371.html")
@app.route("/bGUzNw==1/", methods=['GET'])
def le372():
    return render_template("le372.html")
@app.route("/bGUzNw==2/", methods=['GET'])
def le373():
    return render_template("le373.html")

#-----nguyenviettung

@app.route("/bmd1eWVudmlldHR1bmc=/", methods=['GET'])
def nguyenviettung1():
    return render_template("nguyenviettung1.html")
@app.route("/bmd1eWVudmlldHR1bmc=1/", methods=['GET'])
def nguyenviettung2():
    return render_template("nguyenviettung2.html")
@app.route("/bmd1eWVudmlldHR1bmc=2/", methods=['GET'])
def nguyenviettung3():
    return render_template("nguyenviettung3.html")

#----pokedung

@app.route("/cG9rZWR1bmc=/", methods=['GET'])
def pokedung1():
    return render_template("pokedung1.html")
@app.route("/cG9rZWR1bmc=1/", methods=['GET'])
def pokedung2():
    return render_template("pokedung2.html")
@app.route("/cG9rZWR1bmc=2/", methods=['GET'])
def pokedung3():
    return render_template("pokedung3.html")
@app.route("/cG9rZWR1bmc=3/", methods=['GET'])
def pokedung4():
    return render_template("pokedung4.html")

#---FL.ShadowLege (lam dai tung)

@app.route("/ZmxzaGFkb3dsZWdl/", methods=['GET'])
def flshadowlege1():
    return render_template("flshadowlege1.html")
@app.route("/ZmxzaGFkb3dsZWdl1/", methods=['GET'])
def flshadowlege2():
    return render_template("flshadowlege2.html")
@app.route("/ZmxzaGFkb3dsZWdl2/", methods=['GET'])
def flshadowlege3():
    return render_template("flshadowlege3.html")
@app.route("/ZmxzaGFkb3dsZWdl3/", methods=['GET'])
def flshadowlege4():
    return render_template("flshadowlege4.html")

#---------khiemdt

@app.route("/a2hpZW1kdA==/", methods=['GET'])
def khiemdt1():
    return render_template("khiemdt1.html")

#-------congduoc

@app.route("/Y29uZ2R1b2M=/", methods=['GET'])
def congduoc1():
    return render_template("congduoc1.html")
@app.route("/Y29uZ2R1b2M=1/", methods=['GET'])
def congduoc2():
    return render_template("congduoc2.html")


if __name__ == '__main__':
   app.run()