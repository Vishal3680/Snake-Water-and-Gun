import random
def youWin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
         return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="s":
         return True
        elif you=="g":
            return False
    elif comp=="g":
        if you=="w":
         return True
        elif you=="s":
            return False
print("comp turn :computer will choose snake(s) ,water(w) and gun(g)")
randNo=random.randint(1, 3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'    
else:
    comp='g'  
you=input("Your turn :choose snake(s) ,water(w) and gun(g)?\n")
a=youWin(comp,you)    
if a==None:
    print("The match is tie")
elif a:
    print("You win!")    
else:
    print("You loose!")    
