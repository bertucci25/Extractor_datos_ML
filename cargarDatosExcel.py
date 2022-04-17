# Importo el modulo xlsxwriter para crear un archivo de excel
import xlsxwriter
from rankingMouse import precioDeMouse, descripcionCompleta


# funcion para añadir datos a la hoja de calculo
def agregarDatosColumna(fila, columna, infoColumna):
    index = 0
    while fila <= 20:
        worksheet1.write(fila, columna, infoColumna[index])
        fila = fila + 1
        index = index + 1

# Crea el archivo de excel "DatosML"
workbook = xlsxwriter.Workbook('datosML.xlsx')
 
# Añado la hoja donde vamos a cargar los datos en el archivo 
worksheet1 = workbook.add_worksheet()

# Convierte los encabezados de la hoja en negrita
bold = workbook.add_format({'bold': True})

# uso el objeto worksheet1 para escribir
# data con el metodo write()
worksheet1.write(0, 0, 'Precios Mouse', bold)
worksheet1.write(0, 1, "Titulo publicacion", bold)

# Uso la funcion agregarDatosColumna para llenar las columnas A y B desde segunda fila  
agregarDatosColumna(1,0,precioDeMouse)

agregarDatosColumna(1, 1, descripcionCompleta)



# Finalmente termino de editar con el metodo close()
workbook.close()