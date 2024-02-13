num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
operator = (input("Enter an operator: "))

if operator == "+":
   add = f"{num_1}+{num_2}={num_1+num_2}"
   print(add)

elif operator == "-":
   sub = f"{num_1}-{num_2}={num_1-num_2}"
   print(sub)

elif operator == "*":
   mul = f"{num_1}*{num_2}={num_1*num_2}"
   print(mul)

elif operator == "%":
   mod = f"{num_1}%{num_2}={num_1%num_2}"
   print(mod)

elif operator == "/":
   div = f"{num_1}/{num_2}={num_1/num_2}"
   print((div))
elif operator == "//":
   div = f"{num_1}//{num_2}={num_1//num_2}"
   print((div))
else:
   print("Unknown operation")
    
      
