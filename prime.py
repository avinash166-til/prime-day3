limit=int(input("tell us limit of prime numbers:"))
for each in range(2,limit):
     if each==2 or each==3 or each==5 or each==7 or each%2!=0 and each%3!=0 and each%5!=0 and each%7!=0:
          print(each)
