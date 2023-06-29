import csv
from time import ctime, sleep


def main():
	
	try:
		for i in range(3):
			op = int(input("1- Sum\n2- Subtraction\n3- Division\n4- Multiplication\n\n"))
			if op in range(5):
				break
	except ValueError:
		print("enter a number from 1 to 4 according to the desired operation.")
		return 1
	

	n1 = int(input("Number: "))
	n2 = int(input("Number: "))
	
	if op == 1:
		final = sum(n1, n2)
		op = 'sum'
	elif op == 2:
		final = subtraction(n1 , n2)
		op = 'subraction'
	elif op == 3:
		final = division(n1, n2)
		op = 'division'
	else:
		final = multiplication(n1, n2)
		op = 'multiplication'

	print(f"result: {final:.2f}")
	print("\nwriting the logs in the csv file")
	sleep(1)

	localtime = ctime()

	with open('calcs.csv', mode= 'a', newline='') as csvfile:
		fieldnamess = ['time', 'op', 'number1', 'number2', 'result']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnamess)

		writer.writerow({'time': localtime, 'op' : op , 'number1' : n1, 'number2' : n2, 'result' : final})

	final_message()

def sum(x, y):
	return x + y  

def subtraction(x, y):
	return x - y

def division(x, y):
	return x / y

def multiplication(x, y):
	return x * y

def final_message():
	for i in range(3):
		print(f"{3 - i} sec...")
		sleep(1)
	print("bye")
	

if __name__ == '__main__':
	main()
