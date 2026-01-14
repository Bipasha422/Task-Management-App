try:
 a = int(input("hey,enter a number:"))
 print(a)
 b = int(input("hey,enter another number:"))
 print("Result:",a/b)
except ZeroDivisionError:
 print("cannot divide by zero")
except ValueError:
 print("please enter valid number")