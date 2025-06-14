import requests

url= 'http://******/mediciones'

def stats ():
    r = requests.get(f'{url}/stats')
    data= r.text
    print(data)
    return data

def all():
    r = requests.get(f'{url}/all')
    data= r.text
    print(data)
    return data

def nodoId(nombreNodo):
    r = requests.get(f'{url}/nodo/{nombreNodo}')
    data= r.text
    print(data)
    return data

def nodoSensor(nombreNodo, idSensor):
    r = requests.get(f'{url}/nodo/{nombreNodo}/sensor/{idSensor}/ultima')
    data= r.text
    print(data)
    return data

