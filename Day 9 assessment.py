from typing import Self
import os,sys

if sys.platform=="win32":
    clear = lambda:os.system("cls")

else:
    clear = lambda:os.system("clear")


class Calculator:
    final:int = 0

    def add(self,num: float)-> Self:
        self.final += num
        return self
    

    def sub(self,num:float)-> Self:
        self.final -= num
        return self

    def mul(self,num:float) -> Self:
        self.final *= num
        return self

    def div(self,num:float )-> Self:
        self.final /= num
        return self
    
    def result(self):
        return self.final
    
    
def validate_input(inp,_type=int):
    try:
        return _type(inp)
    except Exception:
        return None


def main():
    clear()
    calc = Calculator()

    print("Calculator".center(50))

    while True:
         
         num_1 = input("Number(Type 'exit' for exiting):  ")
        #  breaking condition
         if not num_1 or num_1 in ("x","exit","quit","q"):
             break
         v_num1 = validate_input(num_1,float)
         operator = input("Operator:  ")
         

         op = None
         if operator in("+","add"):
            op = "add"

         elif operator in("-","sub"):
            op = "sub"

         elif operator in("*","mul"):
            op = "mul"

         elif operator in("/","div"):
            op = "div"

         else:
             print("Invalid Operator")
             continue
         

         method_mapping={
            "add":calc.add,
            "sub":calc.sub,
            "mul":calc.mul,
            "div":calc.div
        }
         method = method_mapping[op]
         if not v_num1:
             continue
    
         method(v_num1)




             
    print(f"Result:{calc.result():.2f}")


if __name__ == "__main__":
  main()
    

    
    

    

 