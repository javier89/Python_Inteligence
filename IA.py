import sys, random

jugadas=[]

def jugar():
	while True:
		try:
			total_humano=int (input ('\nTotal?'))

			n_maquina, total_maquina = predecir(total_humano)
			n_humano=int(input ('cuantas tenias?'))

			print ('\nHumano: ' + str(n_humano))
			print ('Maquina: ' + str(n_maquina))
			if(n_maquina+n_humano)==total_humano:
				print('Ganaste!!')
			elif(n_maquina+n_humano)==total_maquina:
					print ('perdiste!!')
				#para el modulo de IA...
			jugadas.append((n_humano, total_humano))

		except KeyboardInterrupt:
				print ('\nSalienso ....')
				sys.exit(0)

def predecir(total_humano):
	n_maquina=random.randint(0,3)
	total_maquina=random.randint(n_maquina, n_maquina+3)
	print ('La Maquina Predice' + str(total_maquina))
	return n_maquina,total_maquina

jugar()