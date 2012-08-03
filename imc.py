if __name__ == '__main__':

         print("Calculo de imc")
         print("Digite Su Peso"),

         n = int(raw_input())

	 print("Digite Su Estatura"),

	 k =float(raw_input())
         

         masa=n/(k**2)
             

         print('IMC=',masa)

	 if masa <= 18.50:
		solucion = "En Infrapeso"
	 elif masa < 25:
		solucion = "Normal"
	 elif masa >= 25:
		solucion = "En Sobre Peso"
	 else:
		solucion = "Obeso"

	 print "Usted esta %s" % (solucion)
         print("Gracias.")

         raw_input()
