from selenium import webdriver
from datetime import datetime
import datos


### PATH DEL DRIVER DE GOOGLE
chormedriver= datos.chromedriverpath


### URL DE SIGEDU
url = 'https://sigedu.utdt.edu/WebJSP/principal/login.jsp'


### DATOS DE LA INSCRIPCION

user = datos.usuario
contra = datos.clave

hora_de_inscripcion = datetime(datos.anio, datos.mes, datos.dia, datos.hora, datos.minutos)

materias = datos.materias


### LOG IN EN SIGEDU
driver = webdriver.Chrome(chormedriver)
driver.get(url)
driver.find_element_by_xpath('\
	/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[3]/input[2]'\
	).send_keys(user)
driver.find_element_by_xpath('\
	/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[3]/input'\
	).send_keys(contra)
driver.find_element_by_xpath('\
	/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[3]/td/input[1]'\
	).click()
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/div[2]/table\
	/tbody/tr/td/table[1]/tbody/tr/td/a').click()

SIGEDU = driver.current_window_handle


### SELECCIONAR MATERIA
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
	table[1]/tbody/tr[2]/td/table[3]/tbody/tr[1]/td[2]/a').click()

DATOS = driver.window_handles[1]
driver.switch_to.window(DATOS)

driver.find_element_by_xpath('/html/body/form/input[8]'\
	).send_keys(materias[0][0])
driver.find_element_by_xpath('/html/body/form/input[9]').click()
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/\
	tbody/tr[1]/td/a').click()

driver.switch_to.window(SIGEDU)


### SELECCIONAR COMISION
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
	table[1]/tbody/tr[2]/td/table[3]/tbody/tr[2]/td[2]/a').click()

DATOS = driver.window_handles[1]
driver.switch_to.window(DATOS)

driver.switch_to.window(DATOS)

driver.find_element_by_xpath('/html/body/form/input[8]'\
	).send_keys(materias[0][1])
driver.find_element_by_xpath('/html/body/form/input[9]').click()
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/\
	tbody/tr/td/a').click()

driver.switch_to.window(SIGEDU)

driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
	table[2]/tbody/tr/td/input[1]').click()


### CONDICION DEL HORARIO PARA LA INSCRIPCION E INSCRIPCION
while hora_de_inscripcion > datetime.now():
	pass
else:
	""" inscripcion a la materia """
	driver.refresh()
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
		table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td/a'\
		).click()
	confirmation = driver.switch_to_alert()
	confirmation.accept()

for i in range(len(materias)-1):
	### SELECCIONAR MATERIA
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
		table[1]/tbody/tr[2]/td/table[3]/tbody/tr[1]/td[2]/a').click()

	DATOS = driver.window_handles[1]
	driver.switch_to.window(DATOS)

	driver.find_element_by_xpath('/html/body/form/input[8]'\
		).send_keys(materias[i+1][0])
	driver.find_element_by_xpath('/html/body/form/input[9]').click()
	driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/\
		tbody/tr[1]/td/a').click()

	driver.switch_to.window(SIGEDU)


	### SELECCIONAR COMISION
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
		table[1]/tbody/tr[2]/td/table[3]/tbody/tr[2]/td[2]/a').click()

	DATOS = driver.window_handles[1]
	driver.switch_to.window(DATOS)

	driver.switch_to.window(DATOS)

	driver.find_element_by_xpath('/html/body/form/input[8]'\
		).send_keys(materias[i+1][1])
	driver.find_element_by_xpath('/html/body/form/input[9]').click()
	driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/\
		tbody/tr/td/a').click()

	driver.switch_to.window(SIGEDU)

	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
		table[2]/tbody/tr/td/input[1]').click()
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/\
		table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td/a'\
		).click()
	confirmation = driver.switch_to_alert()
	confirmation.accept()
