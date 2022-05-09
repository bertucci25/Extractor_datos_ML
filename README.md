# Extraer datos de Articulos mas vendidos en MeLi

Script simple para obtener datos de cualquier categoria en la seccion "Mas vendidos" del unicornio amarillo. 

## Herramientas usadas:

- Python junto con la libreria BeautifulSoup, y los modulos requests y xlsxwriter.
- Excel.

### Funcion del script:

El script localiza las etiquetas HTML del sitio web y filtra de manera que solo sean escritos en la hoja de calculo el Precio y Titulo del item.

No todas las etiquetas pueden ser iguales, sin embargo en ML, esta relativamente estandarizado asi que no deberia tener problema en usarlo para cualquier categoria con 
seccion de "Mas vendidos".

Nota: para hacer que funcione correctamente el script se debe virtualizar el espacio donde estan ubicado los archivos .py <br>

**¿Cómo hacerlo?** : en el powershell ubicados en la carpeta del projecto escribimos: 
`virtualenv env` y luego escribimos `env/scripts/activate` <br>
Se deben instalar las librerias/modulos, lo podes hacer con el archivo del repo requirements.txt y el comando `pip install -r requirements.txt` <br>
Para hacer correr el script tenemos que ejecutarlo desde la poweshell con `python cargar_datos_excel.py`

Dentro del archivo ranking_ml podes colocar la url la cual quieras scrapear

¿Aun no estas canchero con la linea de comandos? Puedes leer esta guía practica del sitio web Programming Historian haciendo click [acá](https://programminghistorian.org/es/lecciones/introduccion-a-powershell)



## Excel 

Utilizando algunas formulas basicas de excel con los datos extraidos del script se pueden hacer visualizaciones sencillas para mejores efectos demostrativos

![image](https://user-images.githubusercontent.com/81843234/164878337-c9490b11-43a3-4b71-b13a-f881c389f980.png)

En el repo esta el excel con estas visualizaciones
