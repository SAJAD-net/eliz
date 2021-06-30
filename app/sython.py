
def timer(fun, url = None):
    from time import time
    st = time()
    try:
        if url:
            fun(url)
        else:
            fun()
    except Exception as e:
        print("[e]--> error, check url and connection !")
    et = time() - st
    print("[!]--> Total time : %1.2f s"%et)
    print("[!]--> Finished !")

def help():
    print("""[!]--> `*` sython help `*`
        
        how:
            python3 sython.py [args] [url] OR python3 sython.py

        args:
                -u  --> dow.. with urllib
                -u2 --> dow.. with urllib2
                -r  --> dow.. with requests
                -w  --> dow.. with wget
                -h  --> help
    """)
def checkurl(url = None):
    if not(url):
        url = input("[+]--> enter url -> ")
    else:
        if "/" not in url:
            print("[e]--> error, check url and try again !")
            exit()
        elif url == "quit":
            exit()
        elif "http" and "https" not in url:
            url = "http://" + url
            return url

def findname(url):
    fn = url.split("/")
    nf = fn[-1]
    return nf

def urllib(url = None):
    from urllib.request import urlretrieve
    if url:
        url = checkurl(url)
    else:
        url = checkurl()
    name = finename(url)
    print("[!]--> download started with urllib !")
    urlretrieve(url, name)
    
def urllib2(url = None):
    try:
        from urllib2 import urlopen
    except:
        print("[e]--> error, urllib is not installed !")
        exit()
    if url:
        url = checkurl(url)
    else:
        url = checkurl()
    name = finename(url) 
    print("[!]--> download started with urllib2 !")
    filer = urlopen(url)
    filew = filer.read()
    with open(name, "wb") as filen:
        filen.write(filew)
    filen.close()

def requests(url = None):
    try:
        from requests import get
    except:
        print("[e]--> error, requests is not installed !")
        exit()
    if url:
        url = checkurl(url)
    else:
        url = checkurl()
    name = finename(url) 
    header = {"user-agent" : "sython", "referer" : "google.com"}
    print("[!]--> download started with requests !")
    res = get(url, headers = header)
    print(f"status : {res.status_code}")
    with open(name, "wb") as filen:
        filen.write(res.content)
    filen.close()
def wget(url = None):
    try:
        from wget import download 
    except:
        print("[e]--> error, wget is not installed !")
        exit()
    if url:
        url = checkurl(url)
    else:
        url = checkurl()
    name = finename(url)
    print("[!]--> download started with wget !")
    download(url, name)

def run():
    from sys import argv
    if len(argv) > 1:
        if argv[1] == "-h":
            help()
        elif argv[1] != "-u" and "-u2" and "-r" and "-w":
            print(f"[e]--> error, enter valid argument !, this not found --> {argv[1]}")
        elif argv[2]:
            if argv[1] == "-u":
                timer(urllib, argv[2])
            elif argv[1] == "-u2":
                timer(urllib2, argv[2])
            elif argv[1] == "-r":
                timer(requests, argv[2])
            elif argv[1] == "-w":
                timer(wget, argv[2])
            else:
                print("[e]--> enter valid argument !")
                help()
        else:
            print("[e]--> error, enter url !")
    else:
        print("[!]--> `*` welcome to sython `*`")
        fits = ["urllib", "urllib2", "requests", "wget", "help", "exit"]
        count = 1
        for fit in fits:
            print(f"[{count}]- {fit}", end="\t")
            count += 1
            if count == 4:
                print("")
        print("")
        try:
            num = int(input("[+]--> enter num of property -> "))
        except:
            print("[e]--> error, enter num. not found this --> {num} !")
            exit()
        if num == 1:
             timer(urllib)
        elif num == 2:
             timer(urllib2)
        elif num == 3:
            timer(requests)
        elif num == 4:
            timer(wget)
        elif num == 5:
            help()
        elif num == 6:
            exit()
        else:
            print(f"[e]--> enter valid num, not found this --> {num}")
run()
