import getpass
import string
import os
users=['user1','user2','user3']
pins=['1234','2222','3333']
amounts=[1000,2000,3000]
count=0

while True:
    user=input("\nENTER USER NAME:")
    user=user.lower()
    if user in users:
        if user==users[0]:
            n=0
        elif user==users[1]:
            n=1
        else:
            n=2
        break
    else:
        print("--------")
        print("********")
        print("INVALID USERNAME")
        print("********")
        print("--------")
while count<3:
    print("---------")
    print("*********")
    pin=str(getpass.getpass("\n PLEASE ENTER PIN:"))
    print("---------")
    print("*********")
    if pin.isdigit():
            if user=='user1':
              if pin==pins[0]:
                break
              else:
                  count+=1
                  print("-------")
                  print("*******")
                  print("INVALID PIN")
                  print("*******")
                  print("-------")
                  print()
            if user=='user2':
                if pin==pins[1]:
                    break
                else:
                    count+=1
                    print("--------")
                    print("********")
                    print("INVALID PIN")
                    print("********")
                    print("---------")
                    print()
            if user=='user3':
                if pin==pins[2]:
                    break
                else:
                    count+=1
                    print("-------")
                    print("*******")
                    print("INVALID PIN")
                    print("*******")
                    print("-------")
                    print()
        
    else:
                  print("-------")
                  print("*******")
                  print("PIN consists of 4 digits")
                  print("*******")
                  print("-------")
                  count+=1
if count==3:
    print("--------")
    print("********")
    print("3 UNSUCCESSFUL ATTEMPTS EXISTING!!!")
    print("YOUR CARD HAS BEEN DECLINED")
    print("********")
    print("---------")
    exit()

print("---------")
print("*********")
print("---LOGIN SUCCESSFUL---")
print("**********")
print("----------")
print()
print("------------")
print("*************")
print(users[n],"Welcome to ATM")
print("**************")
print("--------------")
print()
print("-----ATM SYSTEM-----")
#Main Menu
while True:
    print("--------")
    print("********")
    response=input("\n Select from the following:\n Statement(s)\n Withdraw(w)\n Lodgment(l)\n Change Pin(p)\n Mobile recharge(r)\n Exit(q):").lower()
    print("********")
    print("---------")
    valid_response=['s','w','l','p','r','q']
    response=response.lower()
    if response=='s':
        print("---------")
        print("**********")
        print("Welcome", users[n],"You have", amounts[n]," EURO in your account")
        print("**********")
        print("----------")
    elif response=='w':
        print("----------")
        print("**********")
        cash_out=int(input("\n Enter the amount you would like to withdraw:"))
        print("**********")
        print("----------")

        if cash_out%10!=0:
            print("--------")
            print("********")
            print("\n YOUR AMOUNT MUST MATCH WITH 10 EURO NOTES!")
            print("*********")
            print("---------")
        elif cash_out>amounts[n]:
            print("------")
            print("*******")
            print("\n You have insufficient balance in your account")
            print("********")
            print("---------")
        else:
            amounts[n]=amounts[n]-cash_out
            print("--------")
            print("********")
            print(" NEW BALANCE is:",amounts[n],"EURO")
            print("********")
            print("--------")
     
    elif response=='l':
        print()
        print("--------")
        print("********")
        cash_in=int(input("\n ENTER THE AMOUNT YOU WANT TO LODGE:"))
        print("********")
        print("---------")
        if cash_in%10!=0:
            print("--------")
            print("********")
            print("\n THE AMOUNT YOU WANT TO LODGE MUST MATCH WITH 10 EURO NOTES!")
            print("*********")
            print("---------")
        else:
            amounts[n]=amounts[n]+cash_in
            print("--------")
            print("********")
            print(" YOUR NEW BALANCE:",amounts[n],"EURO")
            print("*********")
            print("---------")
    elif response=='p':
            print("--------")
            print("********")
            new_pin=str(getpass.getpass("ENTER A NEW PIN:"))
            print("*********")
            print("---------")
            if new_pin.isdigit() and new_pin!=pins[n] and len(new_pin)==4:
                print("--------")
                print("********")
                new_ppin=str(getpass.getpass("CONFIRM NEW PIN:"))
                print("*********")
                print("---------")
                if new_ppin!=new_pin:
                    print("--------")
                    print("********")
                    print("\nPIN MISMATCH")
                    print("*********")
                    print("---------")
                else:
                    pins[n]=new_pin
                    print("NEW PIN SAVED")
            else:
                print("--------")
                print("********")
                print("\n NEW PIN MUST CONSISTS OF 4 DIGITS AND\n SHOULD NOT MATCH WITH THE OLD PIN")
                print("*********")
                print("---------")

    elif response=='r':
            print("--------")
            print("********")
            number=input("\n ENTER YOUR PHONE NUMBER:")
            print("*********")
            print("---------")
            print()
            plan=int(input("\nEnter the amount of your recharge plan:"))
            PIN=str(getpass.getpass("\n Enter your pin :"))
            if number.isdigit() and len(number)==10:
                if PIN==pins[n]:
                    amounts[n]=amounts[n]-plan
                    print("Your number",str(number)," has been successfully recharged with",plan,"recharge pack")
                    print("Your New Balance is:",amounts[n])
                else:
                    print("--------")
                    print("********")
                    print("\nINVALID PIN")
                    print("*********")
                    print("---------")
            else:
                print("--------")
                print("********")
                print("\n YOUR PHONE NUMBER MUST CONSISTS OF 10 DIGITS ONLY!!!")
                print("*********")
                print("---------")

    elif response=='q':
        exit()
else:
            print("--------")
            print("********")
            print("\n RESPONSE IS NOT VALID")
            print("*********")
            print("---------")
    
                    
