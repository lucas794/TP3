''' para promediar QUE camino conectar energia electrica
	el criterio que yó personalmente tomaria es CUANTA cantidad de gente
	es favorecida con esto + el largo de la ruta.
	La idea es conseguir largos de ruta mas cortos pero con varias poblaciones.
	'''
import csv
import ciudades

def cargar_ciudades(archivo_ciudades)
	with open(archivo_ciudades) as archivo:
			archivo_csv = csv.reader(archivo)
			ciudades = []
			for id, nombre, long, lat, prov, hab in archivo_csv:
				ciudad = CIUDAD(id, nombre, long, lat, prov, hab)
				ciudades.append(ciudad)
		
	return ciudades

def cargar_rutas(archivo_rutas)
	with open(archivo_rutas) as archivo:
		archivo_csv = csv.reader(archivo)
		for	id_ciudad_1, id_ciudad_2 ,puntaje ,distancia in archivo_csv
			ruta = RUTA(id_ciudad_1, id_ciudad_2, puntaje, distancia)
			
def main( ):
	# Inicialmente podemos pedirle al usuario a travez de un input que ingrese la conexion de 2 provincias
	# a las cuales conectar de forma electricamente y de tendido mínimo, Esa conexión en sí es un grafo, el algoritmo PRIM se encarga de esta conexión
	
	
	# Aquí deberiamos armar la conexión entre todas las rutas y las provincias que las unen
	# y utilizar primitivas del grafo para armar la conexion mínima.
	
	
	# https://en.wikipedia.org/wiki/Haversine_formula La fórmula para calcular la distancia entre 2 puntos, va a servir demasiado.
	# ó , ( x² + y² )^0.5
	
'''
Esto a continuacion tranquilamente puede pertenecer a una clase llamada Sistema y metes todo el funcionamiento
del programa ahí adentro, así evitas tener multiples funciones. dejo un pseudo código
def graficar_rutas():
		
		coordenadas, distancia = obtener camino_optimo(idf)
		f = open( 'ruta_' + idciudad1 + '_' + id_ciudad2 + '.kml', 'w')
		f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
		f.write("<Document>\n")
		f.write("	<name> EJEMPLO </name>\n").
		f.write("		<Placemark>\n")
		linea = "			<name> UBICACION 1 </name>\n".format(nombre ciudad 1)"
		f.write(linea)
		f.write("			<Point>\n")
		f.write("				<coordinates> COORDENADAS-UBICACION-1 </coordinates\n")
		f.write("			</Point>\n")
		f.write("		</Placemark>\n")		
		
		f.write("		<Placemark>\n")
		linea = "			<name> UBICACION 2 </name>\n".format(nombre ciudad 1)"
		f.write(linea)
		f.write("			<Point>\n")
		f.write("				<coordinates> COORDENADAS-UBICACION-2 </coordinates\n")
		f.write("			</Point>\n")
		f.write("		</Placemark>\n")		
		
		f.write("	<Placemark>\n")
		f.write("		<LineString>\n<coordinates>-58.36795, -34.61763 -58.39644, -34.58850</coordinates>") #COORDENADAS DESDE UN PUNTO A OTRO (REVISAR PDF PARA MAS INFO)
		f.write("		</LineString>\n")
		f.write("	</Placemark>\n")


		f.write("</Document>\n")
		f.write("</kml>\n")	
		f.close()
	'''
