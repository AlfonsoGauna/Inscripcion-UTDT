""" 
	los datos de acceso deben ser strings 

	Ejemplo:
		usuario = '45123789'
		clave = '010101789'
"""

usuario = ''
clave = ''


""" 
	los datos horarios deben ser cargados como numeros y segun formato de
	24 horas 

	Ejemplo:
		anio = 2020 
		mes = 2 
		dia = 19
		hora = 15
		minutos = 30
"""

anio = 2020
mes = 1
dia = 1
hora = 12
minutos = 54


"""
	las materias deben ser cargadas con su respectiva comision dentro de una 
	tupple, como se ve en el ejemplo.
	
	ACLARACIÓN: el nombre de las materia debe estar escrito igual que en 
				sigedu.

		materias = [('Expresión Oral y Escrita','2'),  
					('Comercio Internacional','1'),
					('Economía Matemática II','1'), 
					('Historia del Pensamiento Económico','2'), 
					('Econometría','1')]
"""	


materias = [('',''),
			('',''),
			('',''),
			('','')]

"""
	cambiar el PATH (absolute path) del chromedriver, para no tener problemas
	con los distintos interpretadores.
	
	Ejemplo:
		chromedriverpath = users/usuario/inscripcion-utdt/chromedriver
"""

chromedriverpath = './chromedriver'


