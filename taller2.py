#ejercicio1 

'''
num1 = float(input("ingrese un numero: "))
num2 = float(input("ingrese segundo numero: "))

if  num1 > num2 : 
    print("primer numero es mayor que", num2)
elif num2 > num1: 
    print("segundo numero  es mayor que", num1)


'''
#ejercicio4
'''

tiempo = float(input("cuanto tiempo duro la llamada: "))
if tiempo <= 3:
    print("valor a pagar es 200 pesos")
else: 
    minadd = tiempo - 3
    valtotal = (minadd * 100) + 200
    print(f"el valor a pagar es {valtotal} pesos")

'''
    #ejercicio5
'''
n = int(input("los conejos que hay en la granja son: "))
bl = int(input("la cantidad de conejos blancos: "))
ne = int(input("la cantidad de conejos negros: "))
if (bl+ne)>n: 
    print("error 1 la cantidad de conejos blancos y negros no coinciden con el total")
elif (bl+ne)<n:
    print("error 2 en la cantidad de conejos negros y blancos no coinciden con el total")
else:
    
    x = int(input("cantidad de conejos blancos vendida; "))
    if x>bl:
        print("la cantidad de conejos blancos vendido no puede ser mayor que la cantidad de conejos negros total")
    else:
        y = int(input("cantidad de conejos negros vendida: "))
        if y>ne:
            print("la cantidad de conejos negos vendido no puede ser mayor que el numero de conejos blancos totales")
        else: 
            p1 = int(input("precio de conejos blancos: "))
            p2 = int(input("precio de conejos negros: "))
            cnv = x+y
            print(f"la cantidad de conejos vendida es: {cnv}")
            mvbl = x*p1
            print(f"monto venta total conejos blancos: {mvbl}")
            mvne = y*p2
            print(f"monto venta total de conejos negros es: {mvne}")
            mv = y*p2+x*p1
            print(f"monto de venta es: {mv}")
        

            if x > y:
                print("se vendieron mas conejos negros")
            elif y > x: 
                print("se vendieron mas conejos blancos")

'''


#ejercicio6
np1 = float(input("nota previo numero 1 es: ")) 
np2 = float(input("nota previo numero 2 es: "))
np3 = float(input("nota previo numero 3 es: "))
npd = np1+np2+np3
print(f"nota previos definitiva es: {npd}")

nt1 = float(input("nota trabajo numero 1 es: "))
nt2 = float(input("nota trabajo numero 2 es: "))
nt3 = float(input("nota trabajo numero 3 es: "))
ntd = nt1+nt2+nt3
print(f"nota definitiva trabajos es: {ntd}")