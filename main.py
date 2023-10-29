import requests

def hataları_kontrol(url):
    try :
        return requests.get(url)
    except:
        print("404 NOT FAUND!!!!!!!!!! try again")

user_domain = "google.com"
with open("subdomainList.txt","r") as subdomain_list:

    for word in subdomain_list:
        word = word.strip()
        url = "htpp://" + word + "." + user_domain
        response = hataları_kontrol(url)
        if response:
            print("the page found"+ url)
