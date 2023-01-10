import socket
import urllib.request
import requests 

#Color_Tools
#==================
#bi=\033[34;1m
#ij=\033[32;1m
#un=\033[35;1m
#cy=\033[36;1m
#me=\033[31;1m
#pu=\033[37;1m
#ku=\033[33;1m
#===================

def icon():
    print(f"""
\033[31;1m (                 (        )             )  
 )\ )          (   )\ )  ( /(    (     ( /(  
(()/(    (   ( )\ (()/(  )\())   )\    )\()) 
 /(_))   )\  )((_) /(_))((_)\  (((_) |((_)\  
(_))  _ ((_)((_)_ (_))    ((_) )\___ |_ ((_) 
\033[35;1m/ __|| | | | | _ )| |    / _ \((/ __|| |/ /  
\__ \| |_| | | _ \| |__ | (_) || (__   ' <   
|___/ \___/  |___/|____| \___/  \___| _|\_\  
                            \033[1;33mCode By @HunX04     

\033[1;37m===========================================
\033[1;37m[ \033[1;33m+ \033[1;37m] \033[1;33mUser Name\033[1;37m  : \033[1;33m{host}
\033[1;37m[ \033[1;33m+ \033[1;37m] \033[1;33mIP Address\033[1;37m : \033[1;33m{ipadd}
\033[1;37m===========================================
""")

host = socket.gethostname()
ipadd = requests.get('https://api.ipify.org').text

#Start Coding
def subdoamin():
    get_url = input(f"\033[1;37m[ \033[1;33m+ \033[1;37m] \033[1;37mMasukan Domain target : \033[33;1m")
    line =  print("\033[37;1m___________________________________________")
    word = open("wordlist.txt")
    content = word.read()

    subdo_domain = content.splitlines()

    for subdo in subdo_domain:
        url_domain = (f"https://{subdo}.{get_url}")
        try:
            requests.get(url_domain)
            print("\033[33;1m[ \033[37;1m! \033[33;1m] \033[37;1mMendapatkan Subdomain \033[33;1m>>\033[37;1m",url_domain)
        except requests.ConnectionError:
            pass
    #End Coding
    #icon()
    #subdoamin()
try:
    icon()
    subdoamin()
except KeyboardInterrupt:
    print("\n\033[31;1mScann Subdomain Berhenti...")
