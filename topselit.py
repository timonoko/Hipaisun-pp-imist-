#! /usr/bin/python3

import os, math, time, urllib, web, broadlink

os.chdir('/home/tnoko/Clas_Olhson/')

web.config.debug=False

d=broadlink.discover(local_ip_address="192.168.1.11")

plug=[0,0,0,0,0,0]

while plug[1]==0 and plug[2]==0 and plug[3]==0:
    for x in range(len(d)):
        print(d[x].name)
        if "Jaah" in  d[x].name :
            plug[1]=d[x]
        if  "Tuule" in d[x].name:
            plug[2]=d[x]
        if "pis" in d[x].name:
            plug[3]=d[x]

print(d)
            
def valo(d,x,y):
    try:
        if d.check_power():
            p="VALO.png"
        else:
            p="TYHJA.png"
        return f'<div style="position: absolute; left:{x}; top:{y}">\
                 <img src=static/{p}></div>\n'
    except:
        return ""

def otsikko(kuvio,x,y):
    return f'<div style="position: absolute; left:{x}; top:{y}">\
             <h1>{kuvio}</h1></div>\n'

def nappi(osoite,kuvio,x,y):
    return f'<div style="position: absolute; left:{x}; top:{y}">\
            <a href={osoite}><img src={kuvio}><a></div>\n'

def yksirivi(o,n,y):
    s=otsikko(o,100,y-70)+\
    nappi(f"ON{n}","static/ON.png",100,y)+\
    valo(plug[n],180,y)+\
    nappi(f"OFF{n}","static/OFF.png",260,y)
    return s

def palauta_html(refresh=False):
    s='<html><head> <title>TOPSELIT</title>\n </head> \n'+\
    yksirivi('L&Auml;MMITIN',1,100)+\
    yksirivi('TUULETIN',2,300)+\
    yksirivi('PI',3,500)
    return s

def webbinappi(s1):
    return f"""
try:
    plug[{s1}].auth()
    datoja.urls+=('/ON{s1}','ON{s1}')
    class ON{s1}:
        def GET(self):
            plug[{s1}].set_power(True)
            return palauta_html()
    datoja.urls+=('/OFF{s1}','OFF{s1}')
    class OFF{s1}:
        def GET(self):
            plug[{s1}].set_power(False)
            return palauta_html()
except:
    pass
"""
def uusinappi(s1):
    return f"""
try:
    datoja.urls+=('/ON{s1}','ON{s1}')
    class ON{s1}:
        def GET(self):
            os.system('./nappi{s1}on')
            return palauta_html()
    datoja.urls+=('/OFF{s1}','OFF{s1}')
    class OFF{s1}:
        def GET(self):
            os.system('./nappi{s1}off')
            return palauta_html()
except:
    pass
"""


class datoja:
    urls=('/','index')
class index:
    def GET(self):
        return palauta_html()
exec(webbinappi(1))
exec(webbinappi(2))
exec(webbinappi(3))
exec(uusinappi(101))
exec(uusinappi(102))
exec(uusinappi(103))
exec(uusinappi(104))


os.environ["PORT"] = "8083"
if __name__ == "__main__":
    app = web.application(datoja.urls,globals())
    app.run()
