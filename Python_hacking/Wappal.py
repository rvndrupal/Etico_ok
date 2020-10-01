# pip install python-Wappalyzer

from Wappalyzer import WebPage, Wappalyzer

def main():
    wap=Wappalyzer.latest()
    try: 
        web=WebPage.new_from_url("https://prod.senasica.gob.mx/sisia/login") #Se pone la url a scanear
        tecno=wap.analyze(web)
        Categorias=wap.analyze_with_categories(web)
        for t in tecno:
            print("Tecnologias Detectadas son: {}".format(t))
        for c in Categorias:
            print("Categorias Detectadas: {}".format(c))
            
            
            
    except:
        print("Ha ocurriod un error")
        
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
    