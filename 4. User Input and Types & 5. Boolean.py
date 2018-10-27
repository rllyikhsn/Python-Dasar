def add	(no1,no2):			#Funcion program/class
	return no1 + no2		#mengembalikan nilai no1 + no2

def sub (no1,no2):
	return no1 - no2
	
def mul (no1,no2):
	return no1 * no2
	
def div (no1,no2):
	return no1 / no2
	
def main():											#fungsi utama program
	no1 = int(input ("Masukkan angka 1 : "))		#menginput kedalam variabel no1
	no2 = int(input ("Masukkan angka 2 : "))
	pilihan	= input ("Masukkan Operasi (add,sub,mul,div) ?")
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

main()												#memanggil fungsi main, wajib dipanggil agar menghasilkan output
	