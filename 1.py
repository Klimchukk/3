import random
print("Enter 1 if the numbers are filled randomly")
print("Enter 2 if from the keyboard")
a = int(input())
if(a==1):
    def Min(a1, a2, a3, a4,a5):
        Min = min(a1, a2, a3, a4, a5)
        return Min
    random_numb = [random.randint(1, 100) for _ in range(5)]
    print("Random numbers:", random_numb)
    print("Minimum number:", Min(*random_numb))
elif(a==2):
    b=int(input("Enter 1 number:"))
    c=int(input("Enter 2 number:"))
    d=int(input("Enter 3 number: "))
    f=int(input("Enter 4 number: "))
    g=int(input("Enter 5 number: "))
    def Min(a1, a2, a3, a4,a5):
        Min = min(a1, a2, a3, a4, a5)
        return Min
    print("Min number",Min(b,c,d,f,g))
else:
    print("Try again")

