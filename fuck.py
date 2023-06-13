
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.05)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
o = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
s = '\033[40m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
os.system('clear')
#print(f' [{o}■{x}] {P}Follow My Github Account...');time.sleep(2)
#os.system(' xdg-open https://github.com/Mkr404-Cyber/')
logo =f'''\x1b[1;96m
  ()     ()    ()    ()    ()()()()    {xr}B{x}\x1b[1;96m
  ({xr}●\x1b[1;96m)   ({xr}●\x1b[1;96m)    ()   ()     ()     ()   {xr}L{x}\x1b[1;96m
  ()() ()()    ()  ()      ()     ()   {xr}A{x}\x1b[1;96m
  () ({P}—\x1b[1;96m) ()    ()-()       ()()()()    {xr}C{x}\x1b[1;96m
  ()     ()    ()  ()      ()   ()     {xr}K{x}\x1b[1;96m
  ()     ()    ()   ()     ()    ()
  ()     ()    ()    ()    ()     (){x}  {xr}BOY{x}{P}
 ══════════════════════════════════════════ 
 [{xr}■{x}] {P}Author    : MKR                 
 [{xr}■{x}]{P} Github    : Mkr404-Cyber
 [{xr}■{x}] {P}Facebook  : Mustak Khan
 [{xr}■{x}]{P} Tool Type : Bypass
 [{xr}■{x}] {P}Version   : 404 — Error :():
{P} ══════════════════════════════════════════  {x}'''
def linex():
	print(" ══════════════════════════════════════════")
def xxr():
    os.system("clear")
    print(logo)
    jalan(f'{xr}           🔰 Bypass by MKR 🔰{x} ')
    linex()
    jalan(f'{xr}          🖕 FUCK  XYTEEE-XD{x} 🖕  ')
    print(" ══════════════════════════════════════════")
    print(f" [{xr}1{x}] XYTEEE XD ")
    linex()
    MKR =input(f'{P} [{xr}■{x}{P}] CHOOSE : ')
   # if MKR in ["1", "01"]:
    #os.system('curl -L https://github.com/X-R-404/XR/blob/main/filev1.cpython-311.so?raw=true -o mkr.so')
    import filev1
    import mkr
    

xxr()
