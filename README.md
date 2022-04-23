# Extraer datos de Articulos mas vendidos en MeLi

Script simple para obtener datos de cualquier categoria en la seccion "Mas vendidos". 

## Herramientas usadas:

- Python junto con la libreria BeautifulSoup, y los modulos requests y xlsxwriter.
- Excel.

### Funcion del script:

El script basicamente localiza las etiquetas HTML del sitio web y filtra de manera que solo sean escritos en la hoja de calculo el Precio y Titulo del item.

Importante: no todas las etiquetas pueden ser iguales, sin embargo en ML, esta relativamente estandarizado asi que no deberia tener problema en usarlo para cualquier categoria con "Mas vendidos".

Nota: para hacer que funcione correctamente le script se debe virtualizar el espacio donde estan ubicado los archivos .py del repo. 
¿Cómo hacerlo? : en el powershell ubicados en la carpeta del projecto escribimos: 
`virtualenv env` y luego escribimos `env/scripts/activate` 

¿Aun no estas canchero con la linea de comandos? Puedes leer esta guía practica del sitio web Programming Historian haciendo click [acá](https://programminghistorian.org/es/lecciones/introduccion-a-powershell)


