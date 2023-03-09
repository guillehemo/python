blocks = int(input("Introduce el número de bloques: "))
 
height = 0
 
inlayer = 1
 
while inlayer <= blocks:
 
    height += 1
    blocks -= inlayer       
    inlayer += 1
 
print("La altura de la pirámide es: ", height)