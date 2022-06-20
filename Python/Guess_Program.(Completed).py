
i=0
tries=0
import time
import random
limit=input ("set a limit on the number of tries (0 for infinite): ")
key=input ("Give the desired keyword(from letters A,B,C,D,E): ")
# Θα ηθελα να μπορω να βαζω ονομα στο Key αλλα εαν το κανω ααυτο τα γραμματα οι
#(random.choice) θα πρεπει να περιεχουν ολα τα γραμματα (A,Z) και δεν προκειτε
#να τελειωνε το προγραμμα ποτε μεχρι να τα βρει στην σειρα
#εκτος εαν εκανα κατι που δεν ξερω πως να το κανω το οποιο ειναι να βαζω στις
#random τα γραμματα που εδωσε ο χρηστης σαν Key αντι για (A,B,C,D,E)    
if  limit == str(0): # Οταν δεν υπαρχει οριο(Limit)-----------------------------
    while i != 1:
        if len(key) == 1: #Οταν η λεξη εχει (1) γραμμα
             time.sleep(0.5)
             a=(random.choice(["a","b","c","d","e"]))
             tries+=1
             final=(a)
             print(final)
             if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=3:
                    print ("You are Lucky")
                elif int (tries) >=15:
                    print("Maybe today is not your Lucky day...")     
        elif len(key) == 2: # Οταν η λεξη εχει (2) γραμματα
            time.sleep(0.3)
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a+b)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=5:
                    print ("You are Lucky")
                elif int (tries) >=30:
                    print("Maybe today is not your Lucky day...")
        elif len(key) == 3: #Οταν η λεξη εχει (3) γραμματα
            time.sleep(0.05)
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            c=(random.choice(["a","b","c","d","e"]))
            final=(a+b+c)
            print(final)
            tries+=1
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=15:
                    print ("You are Lucky")
                elif int (tries) >=70:
                    print("Maybe today is not your Lucky day...")
        elif len(key) == 4: #Οταν η λεξη εχει (4) γραμματα
            time.sleep(0.02)
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            c=(random.choice(["a","b","c","d","e"]))
            d=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a+b+c+d)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=20:
                    print ("You are Lucky")
                elif int (tries) >=200:
                    print("Maybe today is not your Lucky day...")
        elif len(key) == 5: #Οταν η λεξη εχει (5) γραμματα
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            c=(random.choice(["a","b","c","d","e"]))
            d=(random.choice(["a","b","c","d","e"]))
            e=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a+b+c+d+e)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=30:
                    print ("You are Lucky")
                elif int (tries) >=1000:
                    print("Maybe today is not your Lucky day...")
elif limit != 0:# ------------Οταν υπαρχει Οριο(Limit)-------------
    while int(tries) <= int(limit) and i!= 1:
        if len(key) == 1:
            time.sleep(0.5)
            a=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=3:
                    print ("You are Lucky")
                elif int (tries) >=15:
                    print("Maybe today is not your Lucky day...")
        elif len(key) == 2:
            time.sleep(0.3)
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a+b)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=5:
                    print ("You are Lucky")
                elif int (tries) >=30:
                    print("Maybe today is not your Lucky day...")
        elif len(key) == 3:
            time.sleep(0.05)
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            c=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a+b+c)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=10:
                    print ("You are Lucky")
                elif int (tries) >=70:
                    print("Maybe today is not your Lucky day...")
        elif len(key) == 4:
            time.sleep(0.02)
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            c=(random.choice(["a","b","c","d","e"]))
            d=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a+b+c+d)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=15:
                     print ("You are Lucky")
                elif int (tries) >=200:
                    print("Maybe today is not your Lucky day...")

        elif len(key) == 5:
            a=(random.choice(["a","b","c","d","e"]))
            b=(random.choice(["a","b","c","d","e"]))
            c=(random.choice(["a","b","c","d","e"]))
            d=(random.choice(["a","b","c","d","e"]))
            e=(random.choice(["a","b","c","d","e"]))
            tries+=1
            final=(a+b+c+d+e)
            print(final)
            if final == key:
                i=1
                print ("------->There is the Keyword<-------\n | \n v")
                print (final)
                print ("Keyword found in",tries,"tries")
                print ("The program has ended successfully")
                if int(tries)<=30:
                    print ("You are Lucky")
                elif int (tries) >=1000:
                    print("Maybe today is not your Lucky day...")
        
    if final != key:
        print("Sadly, the CPU hasn't completed the task in",limit,"tries. (Try reducing the Keywords ammount of letters or add more tries.)")  # Οταν δεν βρεθει το Key μεσα στο Οριο(Limit)   
        
            
    
                
            
    
