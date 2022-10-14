from flask import Flask,render_template
from tkinter import Pack
import urllib.request, json, requests #to extract the html code of the pages 
from bs4 import BeautifulSoup         #this is going to be helpful to extract the classes and body text  
from multiprocessing import Process   # 
import time, random 


#To Extract the amazon price 
def Amazon(string):

    try:
        file = open(string + ".txt", "a")
      
        dictURL = {"Far": "-Standard/dp/B08FS6BB8W/",
                   "FIFA" : "/dp/B0B6JR3YDW/",
                   "Returnal" : "/dp/B08QFPS48J/",
                   "Just": "/dp/B0973KMCFG/",
                   "Nickelodeon": "/dp/B099JPMZCZ/",
                   "Xenoblade": "/dp/B01MU9VUKN/",
                   "Fire": "/dp/B07NSNT5HQ/",
                   "Mario": "/dp/B01N1037CV/",
                   "Dark": "/dp/B079MH7844/",
                   "Ratchet": "/dp/B095T8C99C/",
                   "God": "-PS4/dp/B0798DQ9KT/"}
    
        h = string.replace(" ", "-")
    
        k = dictURL[string.split(" ")[0]]

        url = "http://www.amazon.es/" + h + k 

        agents = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                  "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7"]

        other = {"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"}

        user_agent = ({"User-Agent": random.choice(agents), 
                    'Accept-Language': 'en-US, en;q=0.5'})

        response = requests.get(url, headers = user_agent)
        newhtml = BeautifulSoup(response.content, "html.parser")

        price = newhtml.find("span", attrs = {"id": "priceblock_ourprice"})
            
        try:
            sale = newhtml.find("span", attrs = {"class": "priceBlockStrikePriceString a-text-strike"})
        
        except:
            sale = "NULL"
    
        file.write("/Amazon" + " Normal Price: " + sale.get_text() + " New Price: " + price.get_text())
        
        file.close()
    
    except:
        print("ME RINDO")
        Amazon(string)

def NintendoPrice(string):
    
    file = open(string + ".txt", "a")
    
    dictURL = {"just": "7212", "nickelodeon": "7729", "xenoblade": "333",
               "fire": "2577", "mario": "164", "dark": "439"}

    string = string.lower()
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


    k = dictURL[u[0]]
        

    url = "https://eshop-prices.com/games/" + k + h + "?currency=USD"
    
    user_agent = ({'User-Agent': "Mozilla/5.0"})
    
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

    time.sleep(1)
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
        
        file.write(nuevo + "/" + " Nota Metacrtic: " + metaScore)
        file.close()
    
    except:
    
        file.write(nuevo + " Nota Metacrtic: " + "No Disponible")
        file.close()

def impresionLista(lista):
    
    for i in lista:
        file = open(i + ".txt", "r")
        h = file.readline()
        for i in h.split("/"):
            print(i)
        file.close()


app = Flask("My-website")

@app.route('/')
def leerdatos():
    
    time.sleep(4)

    f = open ("Far Cry 6 PlayStation 5.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Precio = lista[2]
    Normal = Precio[0]
    Oferta = "New"+Precio[1]
    Data = []
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Normal)
    Data.append(Oferta)
    f.close()
    
    #fifa
    f = open ("FIFA 23 PlayStation 5.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Normal = lista[2] 
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Normal)
    f.close()
    #God of war
    f = open ("God of War PlayStation 4.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Normal = lista[2] 
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Normal)
    f.close()
    #RaC
    f = open ("Ratchet Clank Rift Apart PlayStation 5.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Precio = lista[2].split("New")
    Normal = Precio[0]
    Oferta = "New"+Precio[1]
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Normal)
    Data.append(Oferta)
    f.close()
    
    #Returnal
    f = open ("Returnal PlayStation 5.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Precio = lista[2].split("New")
    Normal = Precio[0]
    Oferta = "New"+Precio[1]
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Normal)
    Data.append(Oferta)
    f.close()
    #Dark souls
    f = open ("Dark Souls Remastered Nintendo Switch.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Precio = lista[3]
    amazonnew = lista[2]
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Precio)
    Data.append(amazonnew)
    f.close()
    #Fire emblem
    f = open ("Fire Emblem Three Houses Nintendo Switch.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Precio = lista[2]
    nintendo = lista[3]
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Precio)
    Data.append(nintendo)

    f.close()
    
    #just dance
    f = open ("Just Dance 2022 Nintendo Switch.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Precio = lista[2]
    nintendo = lista[3]
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Precio)
    Data.append(nintendo)
    f.close()
    
    #Mario kart 8
    f = open ("Mario Kart 8 Deluxe Nintendo Switch.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Precio = lista[2]
    amazonnew = lista[3]
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Precio)
    Data.append(amazonnew)
    f.close()
    
    #Nickelodeon all stars
    f = open ("Nickelodeon All Star Brawl Nintendo Switch.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Amazon = lista[2]
    nintendo = lista[3]
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Amazon)
    Data.append(nintendo)
    f.close()
    
    #xenoblade
    f = open ("Xenoblade Chronicles 2 Nintendo Switch.txt",'r')
    mensaje = f.read()
    lista = mensaje.split("/")
    NombreG = lista[0]
    NotaG = lista[1]
    Amazon = lista[2]
    nintendo = lista[3].split("\n")
    Data.append(NombreG)
    Data.append(NotaG)
    Data.append(Amazon)
    Data.append(nintendo)
    f.close()

    
    return render_template('index.html',Juego1 = Data)

@app.route("/")
def hello_world():
    return render_template("index.html")

#This function with link all the functions into the Multiprocessing style
def Info(i): 

    DictGames = {"a": Amazon, "b": Metacrtic, "c": NintendoPrice}
    
    myProcess = [] #Store all the Processes  

    for h in DictGames:
        x = Process(target = DictGames[h], args = (i,))
        myProcess.append(x)
        x.start()

    for my in myProcess:
        x.join()

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

    app.run(debug=True,host='0.0.0.0',port='5000')
