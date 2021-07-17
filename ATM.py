print('Welcome to atm services')
amount=1000
print('1.Check Balance')
print('2.Withdraw Cash')
print('3.Deposit Cash')
print('4.Quit')
op=int(input('Choose your option: '))
def blnc():
    result=amount
    print('Your balance is Rupees '+str(amount))
def witdrw():
    withdraw=int(input('Please enter the amount: '))
    if withdraw<100:
        print('Please enter the amount in multiple of 100!')
    elif withdraw>amount:
        print('Insufficient balance!')
    else:
        result=amount-withdraw
        print('The balance is Rupees '+str(result))
def dpst():
    deposit=int(input('Please enter the amount: '))
    result=amount+deposit
    print('Your balance is Rupees '+str(result))
    
def  qit():
    print("Thankyou for using ATM")

if op==1:
    blnc()
elif op==2:
    witdrw()
elif op==3:
    dpst()
elif op==4:
    qit()
else:
    print("Invalid option")