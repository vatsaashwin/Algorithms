#implementation of stack

class Stack():
	def __init__(self):
		self.items =[]

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

def checkPrecedence(op):
	if op == '-' or op =='+':
		return 1
	elif op == '*':
		return 2
	elif op == '/':
		return 3
	elif op == '^':
		return 4
	else:
		return print("Invalid operator in the string")


def infixToPostfix(a):
	n= len(a)
	postfix = []
	for i in range(n):
		print(i)
		if ((a[i]>='a' and a[i]<='z' ) or (a[i]>='A' and a[i]<='Z')):
			postfix.append(a[i])
			print("added alphabet:", a[i])
		
		elif (a[i]!="(" or a[i] !=")"):
			if (s.isEmpty() or checkPrecedence(s.peek())>=checkPrecedence(a[i])):
				s.push(a[i])
				print("pushed char:", a[i])

			elif (checkPrecedence(s.peek())>checkPrecedence(a[i])):
				

				
			else:
				print("check condiions, going out of loop")	

		else:
			print("check condiions, going out of loop")	

	return postfix

s= Stack()
a= "a^c-d"
# a= "a+b*(c^d-e)^(f+g*h)-i"
print(infixToPostfix(a))



