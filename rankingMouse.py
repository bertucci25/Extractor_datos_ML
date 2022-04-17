from bs4 import BeautifulSoup
import requests

#Se obtiene con beatifulSoup los datos de los precios y descripciones del top 20 de mouses 

url = "https://www.mercadolibre.com.ar/mas-vendidos/MLA1714"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser" )

#devuelve una lista con todos los precios de los mouse que tengan 
#las etiquetas html "span", "promotion-item__price"
precios = soup.find_all("span", "promotion-item__price")


preciosMouse= []

# limpio los datos creando un loop para extraer cada valor sin las etiquetas html
for precio in precios:
    preciosMouse.append(precio.text)

#lo convierto una variable global para utilizarlo en otros archivos py
precioDeMouse = preciosMouse


# devuelve una lista con todos los titulos de los mouse
# que tengan las etiquetas html 'p' y la clase 'promotion-item__title'
titulos = soup.find_all('p', 'promotion-item__title')

descripcion = []

for titulo in titulos:
    descripcion.append(titulo.text)

descripcionCompleta = descripcion






