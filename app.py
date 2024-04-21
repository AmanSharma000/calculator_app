from calc_func import do_addition,do_subtraction
def main():
    print('welcome to the calculator App')
    print("""
          \n Selectthe function from the give options
          1.Add
          2.subtration
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

print('Result :',result)


