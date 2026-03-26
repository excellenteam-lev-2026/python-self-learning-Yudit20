import re                          

TAILLE_CHUNK = 1024               
with open("resources/logo.jpg", "rb") as f:  
    reste = ""                     
    while True:                    
        chunk = f.read(TAILLE_CHUNK)         

        if not chunk:              
            break

        texte = reste + chunk.decode("latin-1")  
        messages = re.findall(r'[a-z]{5,}!', texte)  

        for message in messages:
            print(message)         

        reste = texte[-20:]        