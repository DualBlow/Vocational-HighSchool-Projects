j=0
z=0
x=0
SUMA=[]
GRAM=["Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω"]
epig1=input("Γραψε  την πρωτη επιγραφη σου εδω. : ")
epig2=input("Γραψε  την δευτερη επιγραφη σου εδω. : ")
epig=(epig1+epig2)
for  i  in range (24):
    SUMA.append(0)
for character in epig:
    for z in range (24):
        if character == GRAM[z]:
            SUMA[z]+=1
for x in range (24):
    if SUMA[x]>0:
        print("Παραγγειλε",SUMA[x],"φορες το γραμμα  : ",GRAM[x])
    else:
        j+=1
print("Το πληθος των γραμματων που δεν χρειαζετε να παραγγελθουν ειναι",j)

    
    


