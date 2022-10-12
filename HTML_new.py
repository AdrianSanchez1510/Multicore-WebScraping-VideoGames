import urllib.request, json, requests #to extract the html code of the pages 
from bs4 import BeautifulSoup         #this is going to be helpful to extract the classes and body text  
from Multiprocessing import Process   # 
import time 
#from selenium.webdriver.firefox.options import options

#To Extract the amazon price 
def Amazon(i):
  
    file = open(i+ ".txt", "a")
    
    try:
        
        dictURL = {"Cry": "-Standard/dp/B08FS6BB8W/",
                   "FIFA" : "/dp/B0B6JR3YDW/",
                   "Returnal" : "/dp/B08QFPS48J/",
                   "Dance": "/dp/B0973KMCFG/",
                   "Nickelodeon": "dp/B099JPMZCZ/",
                   "Chronicles": "/dp/B01MU9VUKN/",
                   "Houses": "/dp/B07NSNT5HQ/",
                   "Kart": "/dp/B01N1037CV/",
                   "Souls": "/dp/B079MH7844/",
                   "Clank": "/dp/B095T8C99C/",
                   "War": "-PS4/dp/B0798DQ9KT/"}
        
        string = i   
        u = string.split(" ")
        h = ""
        k = ""
        a = u[0]
       
        for i in u:
        
            if i != u[0]:
                a = "-" + i
            
            try:
            
                k = dictURL[i]
            
            except:
            
                k = k

            h = h + a 

        url = "http://www.amazon.com/-/es/" + h + k 
        
        user_agent = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
                     'Accept-Language': 'en-US, en;q=0.5'})

        response = urllib.request.Request(url, headers = user_agent)
        
        html = urllib.request.urlopen(response).read()
        
        newhtml = BeautifulSoup(html, "html.parser")
        
        title = newhtml.find("span", attrs = {"id": "productTitle"})
        price = newhtml.find("span", attrs = {"id": "priceblock_ourprice"})
        image = newhtml.find(id = "imgTagWtrapperId")
        
        try:
            sale = newhtml.find("span", attrs = {"class": "priceBlockStrikePriceString a-text-strike"})
        
        except AttributeError:
            sale = ""


        try:
            file.write("/Amazon" + " Normal Price: " + sale.get_text() + " New Price: " + price.get_text() + "/")
        
        except:
            file.write(string + price.get_text())
        
        
        file.close()
  
    except urllib.error.HTTPError:
        return

def NintendoPrice(i):
    
    file = open(i + ".txt", "a")
    
    dictURL = {"dance": "7212", "nickelodeon": "7729", "chronicles": "333",
               "houses": "2577", "kart": "164", "souls": "439"}

    string = i.lower()
    u = string.split(" ")
    h = ""
    k = ""
    
    for i in u:
    
        if i == "playstation":
            return
        
        elif i == "nintendo" or i == "switch":
            break 
        
        else:
            h = h + "-" + i


        try:           
            k = dictURL[i]
        
        except:
            k = k 


    url = "https://eshop-prices.com/games/" + k + h + "?currency=USD"
    
    user_agent = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
                     'Accept-Language': 'en-US, en;q=0.5'})
    
    response = urllib.request.Request(url, headers = user_agent)
    
    html = urllib.request.urlopen(response).read()
    
    newhtml = BeautifulSoup(html, "html.parser")
    
    prices = newhtml.find_all("td", class_ = "price-value")

    normal = ""
    
    oferta = "No hay Oferta"
    
    for i in prices:
    
        try:
        
            normal = i.get_text().split("$")[1]
            oferta = i.get_text().split("$")[2]
        
            if (float(normal) < 60) and (float(normal) > 20):
                break 
        
        except:
        
            try:
                
                normal = i.get_text().split("$")[1]
            
                if (float(normal) < 60) and (float(normal) > 20):
                    break 
            
            except:
                continue

    time.sleep(5)
    
    file.write("/Nintendo Eshop Normal: " + normal + " Oferta " + oferta)
    file.close()


def Metacrtic(nuevo):
    
    file = open(nuevo + ".txt", "a")
    
    try:
    
        string = nuevo.lower()
        u = string.split(" ")
        h = ""
        f = ""
        a = u[0]
        
        for i in u:
        
            if i != u[0]:
                a = "-" + i  

            
            if i == "switch":
                f = "switch"
            
            elif i == "playstation":
                f = i
            
            elif i == "4" or "5":
                f = f + "-" + i 

            
            if i != "switch" and i != "nintendo" and i != "playstation" and i != "4" and  i != "5":
                h = h + a 

        url = "https://www.metacritic.com/game/" + f + "/" + h 
        
        user_agent = {"User-Agent": "Mozilla/5.0"}

        response = urllib.request.Request(url, headers = user_agent)
        
        html = urllib.request.urlopen(response).read()
        
        newhtml = BeautifulSoup(html, "html.parser")
        
        data = json.loads(newhtml.find("script", type = "application/ld+json").text)
        
        metaScore = data["aggregateRating"]["ratingValue"]
        
        time.sleep(1.34)
        file.write(nuevo + " Nota Metacrtic: " + metaScore)
        file.close()
    
    except:
    
        file.write(nuevo + " Nota Metacrtic: " + "No Disponible")
        file.close()



#This function with link all the functions into the Multiprocessing style
def Info(i): 

    f = Process(target = Metacrtic, args = (i,)) #The Metacritic function
    x = Process(target = Amazon, args = (i, )) #The Amazon function
    g = Process(target = NintendoPrice, args = (i, ))
    
    myProcess = [x, f, g] #Store all the Processes  
    
    x.start() #Starts the Amazon process 
    f.start() #Starts the 
    g.start()

    for my in myProcess:
    
        x.join()
        f.join()
        g.join()

if __name__ == '__main__':
    
    listaJuegos = ["Far Cry 6 PlayStation 5", 
                   "FIFA 23 PlayStation 5", 
                   "Returnal PlayStation 5", 
                   "Just Dance 2022 Nintendo Switch",
                   "Nickelodeon All Star Brawl Nintendo Switch", 
                   "Xenoblade Chronicles 2 Nintendo Switch",
                   "Fire Emblem Three Houses Nintendo Switch",
                   "Mario Kart 8 Deluxe Nintendo Switch",
                   "Dark Souls Remastered Nintendo Switch", 
                   "Ratchet Clank Rift Apart PlayStation 5",
                   "God of War PlayStation 4"] #Some game names to try 

    myDatos = [] #Creates a list of Process
    for i in listaJuegos: 
        k = open(i + ".txt", "w")
        k.close()
        p = Process(target = Info, args = (i,))  
        myDatos.append(i)
        p.start()

    for i in myDatos:
        p.join()


