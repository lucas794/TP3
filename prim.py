import sys

def main():
	''' creamos un grafo ejemplo 
	     2    3
      (0)--(1)--(2)
       |   / \   |
      6| 8/   \5 |7
       | /     \ |
      (3)-------(4)
            9          '''

	''' Prim resuelto: 0 a 1 ; 1 a 2 ; 0 a 3 y 1 a 4 '''
	
	# Matriz de adyacencias
	'''grafo = [ [ 0, 2, 0 , 6 , 0 ],
			  [ 2, 0, 3 , 8 , 5 ],
			  [ 0, 3, 0 , 0 , 7 ],
			  [ 6, 8, 0 , 0 , 9 ],
			  [ 0, 3, 7 , 9 , 0 ] 
			]'''

	grafo = [ [ 0, 7, 0, 5 , 0],
		  [ 7, 0, 8, 9, 7],
		  [ 0, 8, 0, 0, 5],
                  [ 5, 9, 0, 0, 15],
		  [ 0, 7, 5, 15, 0] ]

	cantidad_vertices = len( grafo[ 0 ] )

	padre = resolver_prim( grafo, cantidad_vertices )

	print "Conexion\t Peso\n"
	for i in range(1, cantidad_vertices):
		print " {} - {}\t\t  {}\n".format( padre[i], i, grafo[ i ][ padre[ i ] ] )

def resolver_prim( grafo, cantidad_vertices ):

	valores = [  sys.maxint for i in range(cantidad_vertices) ]
	visitados = [ False for i in range(cantidad_vertices) ]
	padres = [ -1 for i in range(cantidad_vertices) ]
	
	valores[ 0 ] = 0
	padres[ 0 ] = -1

	for vertices in ( range( cantidad_vertices - 1 )  ):
		
		v_min = vertice_minimo(valores, visitados, cantidad_vertices)

		visitados[ vertices ] = True

		for adyacentes in range( cantidad_vertices ):
			if grafo[ v_min ][ adyacentes ] and not visitados[ adyacentes ] and  grafo[ v_min ][ adyacentes ] < valores[ adyacentes ]:
				padres[adyacentes] = v_min
				print padres
				valores[ adyacentes ] = grafo[ v_min ][ adyacentes ]

	return padres

def vertice_minimo( valores, set_visitados, cantidad_vertices ):
	minimo = sys.maxint
	min_index = -1

	for i in range(cantidad_vertices):
		if set_visitados[ i ] == False and valores[ i ] < minimo :
			minimo = valores[ i ]
			index_minimo = i

	return index_minimo

main()
