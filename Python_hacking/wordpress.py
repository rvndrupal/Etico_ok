import requests
from bs4 import BeautifulSoup

def main():
    url="https://demo.theme-fusion.com/"
    cabecera={'User-Agent':'Firefox'}
    peticion=requests.get(url=url,headers=cabecera)
    soup=BeautifulSoup(peticion.text,'html5lib')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator': 
            ver = v.get('content')
            print(ver)
            

        
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
    