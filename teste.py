import threading
import psutil 



def italo():
  x = 0
  while x < 15:
    print("italo")
    x += 1 

def hercilio():
  y = 0
  while y < 15:
    print("hercilio")
    y +=  1

def bruno():
  z = 0
  while z < 15:
    print("bruno")
    z += 1

def lucas():
  c = 0 
  while c < 15:
    print("lucas")
    c += 1

threading.Thread(target=italo).start()
threading.Thread(target=hercilio).start()
threading.Thread(target=bruno).start()
lucas()

print(psutil.cpu_percent())                    # Em porcentagem, uso da CPU
print(psutil.virtual_memory()._asdict())       # Em dicionário informações de memória física