from calc_func import do_addition,do_subtraction,do_division
from multiply import do_multiply
from area import calculate_area_rectangle
def main():
    print('welcome to the calculator App')
    print("""
          \n Selectthe function from the give options
          1.Add
          2.subtration
          3.multiply
          4.Division
          """)
if __name__=="__main__":
    main()
    
user_input=input("select the function")
a=int(input("value of A"))
b=int(input("value of B"))

if user_input=="1":
    result=do_addition(a,b)
elif user_input=="2":
    result=do_subtraction(a,b)
elif user_input=="3":
    result=do_multiply(a,b)
elif user_input=="4":
    result=do_division(a,b)    

print('Result :',result)


