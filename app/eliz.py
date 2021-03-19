
def timer(fun, url):
    from time import time
    st = time()
    try:
        fun(url)
    except:
        print("[e]--> error, check url and connection !")
    et = time() - st
    print("[!]--> Total time : %1.2f s"%et)
    print("[!]--> Finished !")

def help():
    print("""[!]--> `*` eliz help `*`
        
        how:
            python3 eliz.py [args] [url] OR python3 eliz.py

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
    name = findname(url)
    print("[!]--> download started with urllib !")
    urlretrieve(url, name)
    
def urllib2(url = None):

    from urllib2 import urlopen
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

def requests(url = None):
    from requests import get
    print("[!]--> download started with requests !")
    if url:
        url = checkurl(url)
    else:
        url = checkurl()
    name = finename(url)
    header = {"user-agent" : "eliz", "referer" : "google.com"}
    res = get(url, headers = header)
    print(f"status : {res.status_code}")
    with open(name, "wb") as filen:
        filen.write(res.content)

def wget(url = None):
    from wget import download 
    print("[!]--> download started with wget !")
    if url:
        url = checkurl(url)
    else:
        url = checkurl()
    name = findname(url)
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
        print("[!]--> `*` welcome to eliz `*`")
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
