
# lst=["kongu","sevvai","janet","dharani","rid","kuttan"]
# # 
#  for num in lst:
#    print(num)

# for num in range(len(lst)):
#     # _is allowed in for loop
#     current_num=num
#     previous_num=num-1
#     next_num=num+1

#     if len(lst) > num+1:
#         next_num=num + 1
#     else:
#         next_num = 0
#     print(lst[next_num])
# while
# while some_exp:
# process'
# breaking_condition
# while loop only runs if the expression is true and it breaks if the condition is false
# count=0

# while True:
#     print(f"Value of count is {count}")
#     print("hi")
#     if count==10:
#         break
#     count+=1


# count = 10
# while count>=10:
#     print(f"value of count is {count}")
#     print("janet sevvai")
#     if count==20:
#      break
#     count+=1



# Functions
# def function_name(positional_arguments, keyword_arguments):
# logics
# return


def hello_print(name,profession=None,*args,**kwargs):
   formatted_name= f"my name is {name} and i identify myself as {profession}"
   if name=="rid":
     print("i am janet husband")
   else:
      print("i am hers")

   return formatted_name

fs=hello_print(profession=" janet vetukaaran",name="sevvai")
print(fs)
