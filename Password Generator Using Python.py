uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','-',',','.']
lowercase =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
import random
passlen=int(input("Enter the desired length of password : "))
capans=str(input("Are CAPITAL Alphabets allowed ? (Y/N) : "))
smallans=str(input("Are lowercase Alphabets allowed ? (Y/N) : "))
numbers=str(input("Are Digits allowed ? (Y/N) : "))
spans=str(input("Are Special Charecters allowed ? (Y/N) : "))
print("Way 1 is meant for Minimal Resource Usage and Way 2 for more secure generation.")
rep=input("Way 1 or Way 2 ? (1/2) : ")
capans,smallans,numbers,spans=capans.title(),smallans.title(),numbers.title(),spans.title()
if capans=='Y':
     if smallans=='Y':
          if numbers=='Y':
               if spans=='Y':
                    comblis=uppercase+numbers+symbols+lowercase 
               else:
                    comblis=uppercase+numbers+lowercase 
          else :
               if spans=='Y':
                    comblis=uppercase+symbols+lowercase 
               else:
                    comblis=uppercase+lowercase 
     else:
          if numbers=='Y':
               if spans=='Y':
                    comblis=uppercase+numbers+symbols
               else:
                    comblis=uppercase+numbers
          else :
               if spans=='Y':
                    comblis=uppercase+symbols
               else:
                    comblis=uppercase
else :
     if smallans=='Y':
          if numbers=='Y':
               if spans=='Y':
                    comblis=numbers+symbols+lowercase 
               else:
                    comblis=numbers+lowercase 
          else :
               if spans=='Y':
                    comblis=symbols+lowercase 
               else:
                    comblis=lowercase 
     else:
          if numbers=='Y':
               if spans=='Y':
                    comblis=numbers+symbols
               else:
                    comblis=numbers
          else :
               if spans=='Y':
                    comblis=ar+symbols
               else:
                    print("Error, You denied the usage of all possible charecters")
                    quit()

password=""
if rep=='1':
     for i in range(passlen):
          password+=comblis[random.randint(0,len(comblis)-1)]
          
else:
     random.shuffle(comblis)
     for i in range(passlen):
          q=random.choice(comblis)
          random.shuffle(comblis)
          password=password+q
print("\nGenerated Password is : ",password)
print()
