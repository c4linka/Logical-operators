"""oneToTen = set("1", "2", "3","4" ,"5" ,"6","7","8","9","10".split)
a = input("Wybierz liczbę")
if a == oneToTen:
    print("Liczba zawiera się w przedziale od 1 do 10") 
    #my overthining ideas, fcors didnt work ;)


setA = int
A = int(input("Choose number, I will check if it is form one to ten "))

if (A >= 1):
    if (A <= 10):
        print("Number is in set from one to two.")"""

a = int(input("Choose number, I will check if it is form one to ten "))

if (a  >= 1 and a <= 10):
    print("Number is in set from one to two.")

elif (not(a  >= 1 and a <= 10)):
      print("Number is not in set from one to two.")
              
              

