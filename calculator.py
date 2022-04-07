
def main():
	#write your code here
	
	firstNumber = input("Enter the first number:")
	secondNumber = input("Enter the second number:")
	
	if firstNumber.isdigit() and secondNumber.isdigit():
		operation = input("choose: (+,-,/,*)")
		if operation == "+":
			answer = int(firstNumber) + int(secondNumber)
			print("The Answer is: ", answer)
		elif operation == "-":
			answer = int(firstNumber) - int(secondNumber)
			print("The Answer is: ", answer)
		elif operation == "/":
			answer = int(firstNumber) / int(secondNumber)
			print("The Answer is: ", answer)
		elif operation == "*":
			answer = int(firstNumber) * int(secondNumber)
			print("The Answer is: ", answer)
		else:
			print("You should use a valid operation")
		
	else:
		print("You should enter numbers only")



if __name__ == '__main__':
	main()
