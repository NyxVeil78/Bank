import time

#A list of all users
users=["nyx","wit","luna","iron","echo"]
#Dictonaries to store user credit,password
credits={
        users[0]:100,
        users[1]:100,
        users[2]:90,
        users[3]:85,
        users[4]:70
}
passwords={
        users[0]:'078',
        users[1]:'077',
        users[2]:'076',
        users[3]:'075',
        users[4]:'074'
}

#A function of Bank
def bank(name):
    bank_open=True
    while bank_open:
        print("\tBank Of Viels")
        print("1.Deposit Credits")
        print("2.Withdraw Credits")
        print("3.Balance Check")
        print("4.Leave")
        user=int(input("What You Want(1-4): "))
        if user==1:
            credit=float(input("Credits:"))
            print("Securing Your Credits....")
            time.sleep(3)
            print("Secured!")
            credits[name]+=credit#in this line whoever name is entered credits will be credited
            print("*************************************")
        elif user==2:
            credit=float(input("Credits:"))
            if credits[name]>=credit:
                print("Taking Out Your Credits Securely....")
                time.sleep(3)
                print("Enjoy Your Credits!")
                credits[name]-=credit#in this line whoever name is entered credits will be debited
                print("*************************************")
            elif credits[name]<credit:
                print("Taking Out Your Credits Securely....")
                time.sleep(3)
                print("Error!\nInsufficient Balance!")
                print("*************************************")
        elif user==3:
            print("Checking Your Credits....")
            time.sleep(3)
            print("Your Credits Are:",credits[name])
            print("*************************************")
        elif user==4:
            print("Closing Everything....")
            time.sleep(3)
            print("Everything Closed")
            print("Bye Bye!")
            bank_open=False
            print("*************************************")




print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("*************************************")
name=input("\tYour Name:").lower()

#Here all things stop when there is no any name entered by user
if name not in users:
    print("\tYou are not a Veil")
    print("*************************************")
    
else:
    password=input("\tGive Password:")
    print("*************************************")
    #Here it is if name is in dictionary but password is not equal to the respective user name
    if name in users and password!=passwords[name]:
        print("\tWrong Password\n\tTry Again")
        print("*************************************")
        #Here if everything is fine then this will work
    if password==passwords[name] and name in users:
        bank(name)