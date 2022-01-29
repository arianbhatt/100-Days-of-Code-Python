# Calculator

logo='''
< Welcome to my calculator >
 --------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||

'''
print(logo)

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={
        '+':add,
        '-':sub,
        '*':mult,
        '/':div
    }
num1=float(input("Enter the First Number "))

while(True):
    for i in operations:
        print(i)
    operation_symbol=input("Choose operation you want to operate: ") 
    num2=float(input("Enter the Next Number "))
    calculation_function=operations[operation_symbol]
    answer=calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    num1=num2
    yn=input("Do you want to continue? Enter 'yes' to continue, 'no' to exit\n ")
    if(yn=='no'):
        break
    elif(yn!='yes'):
        print("not a valid choice quiting")
        break

