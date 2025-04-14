def check_numbers(num):
    if num < 0 :
        print("Negetive Numbers")
    else:
        print("Positive Number")

def even_or_odd(num):
    if num % 2 == 0:
        print("Event Number")
    else :
        print("Odd Number") 

def check_ovel(st):
    ovel = str("aeiou")
    if st in ovel:
        print("ovel")
    else :
        print("Not Ovel")

    
num = 10
st = 'c'
check_numbers(num)
even_or_odd(num)
check_ovel(st)