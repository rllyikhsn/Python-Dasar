def latihan():									#function
	print ("Hello World")
	myWorld = 'Hay,'							#deklarasi variabel myWorld dengan value 'hay'
	myVar = input ("Masukkan Nama saya : ")		#variabel dipisahkan dengan tanda =
	myUmr = input ("Umur anda : ")
	print (myWorld,myVar,"Umur",myUmr)			#Mencetak variabel myWorld dan output umur
	
	if (myVar == "Rully" and myUmr == 20):		#eksekusi and, or , == , !=
		print ("Nama anda",myVar)
	elif (myVar == "Clie"):
		print ("Nama Julukan",myVar)
	else:
		print ("You're Stupid")
		
latihan()
	
	