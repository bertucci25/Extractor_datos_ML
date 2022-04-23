from bs4 import BeautifulSoup
import requests

#Se obtiene con beatifulSoup los datos de los precios y descripciones del top 20 de X Categoria
# cambia el url por la categoria que desees
url = "https://www.mercadolibre.com.ar/mas-vendidos/MLA438566"


page = requests.get(url)

# lee el contenido de la url y devuelve todo el "esqueleto" del html
soup = BeautifulSoup(page.content, "html.parser" )

#devuelve una lista con todos los precios de todos los articulos que tengan 
#las etiquetas html "span", "promotion-item__price"
precios = soup.find_all("span", "promotion-item__price")


# Creo una lista para almacenar todos los precios del top 20
precios_articulos= []

# agrego y limpio los datos a la lista creando un loop para extraer cada valor
# sin las etiquetas html usando .text
for precio in precios:
    precios_articulos.append(precio.text) 

# lo convierto una variable global para utilizarlo en otros archivos py
precio_global = precios_articulos


# devuelve una lista con todos los titulos del top
# que tengan las etiquetas html 'p' y la clase 'promotion-item__title'
titulos = soup.find_all('p', 'promotion-item__title')

descripcion = []

# Creo un loop para almacenar en la lista los titulos de los 
for titulo in titulos:
    descripcion.append(titulo.text)

descripcion_completa = descripcion






