def add	(no1,no2):			#Funcion program/class
	return no1 + no2		#mengembalikan nilai no1 + no2

def sub (no1,no2):
	return no1 - no2
	
def mul (no1,no2):
	return no1 * no2
	
def div (no1,no2):
	try:
		return no1 / no2	#jika 0/2 ? apa yang terjadi?
	except ZeroDivisionError:			#untuk menangani pakai fungsi try exception
		print("Diatasi oleh divbyzero")
		return 0		#mengembalikan nilai no1.no2 yang sudah di imput di fungsi main
	

	
def RunOperation(pilihan,no1,no2):	#fungsi operasi
	#menentukan operasi untuk menjalankan didasarkan pada
	#operasi argumen harus dilemparkan sebagai dan mungkin int
	
#menentukan operasi logika
	if (pilihan == 'add'):							#proses boolean ==, atau percabangan
		print ("Hasil",add(no1,no2))
	elif (pilihan == 'sub'):
		print ("Hasil",sub(no1,no2))
	elif (pilihan == 'mul'):
		print ("Hasil",mul(no1,no2))
	elif (pilihan == 'div'):
		print ("Hasil",div(no1,no2))
	else:
		print ("Pilihan tidak tersedia !")
		main()
	
	
	
def main():											#fungsi utama program
	#for index in range (3):		#index karena di loop akan ada loop terus menerus
		coba=False
		while not coba:  #handling exception
			#mendapatkan inputan user
			try:	#handling exception melakukan percobaan sampai nilai keduanya true
				no1 = int(input ("Masukkan angka 1 : "))		#menginput kedalam variabel no1
				no2 = int(input ("Masukkan angka 2 : "))
				pilihan	= input ("Masukkan Operasi yang ingin anda inginkan , operasi tersedia adalah "
								 "(add,sub,mul,div) ?") # baris imaginer, memudahkan membaca program
				coba=True
			except ValueError:	#exit program dengan blok penerimaan
				print("Operasi salah, Coba lagi")
			except:
				print("operasi tidak dikenal")
		RunOperation(pilihan,no1,no2)		#fungsi menjalankan operasi
		

main()												#memanggil fungsi main, wajib dipanggil agar menghasilkan output