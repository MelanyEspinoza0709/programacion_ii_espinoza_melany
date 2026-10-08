#condicional if uwu
#son los que nos permiten ejecutar un bloque de código si se cumple una condición, y otro bloque de código si no se cumple la condición.

combustible=10
if combustible>=10:
    print("puedes despegar")
    
print("-----------------------------------------")
    
#condicional if-else
#es el que nos permite ejecutar un bloque de código si se cumple una condición, y otro bloque de código si no se cumple la condición.
creditos=int(input("ingresa la cantidad de creditos que tienes: "))
precio_repuesto=int(input("ingresa el precio del repuesto: "))
if creditos>=precio_repuesto:
    print("puedes comprar el repuesto")
else:
    print("no tienes suficientes créditos para comprar el repuesto")

print("-----------------------------------------")

#if anidado
#es el que nos permite ejecutar un bloque de código si se cumple una condición, y otro bloque de código si no se cumple la condición.

if creditos>=precio_repuesto:
    print("puedes comprar el repuesto")
    if creditos>precio_repuesto:
        print("te sobraran", creditos-precio_repuesto, "creditos")
    else:
        print("no te sobraran creditos")
        
print("-----------------------------------------")

#condicional if-elif-else
#es el que nos permite ejecutar un bloque de código si se cumple una condición, evalua la otra condicion pasa a la otra si no entonces ejecuta el bloque de código del else.

if creditos>=precio_repuesto:
    print("puedes comprar el repuesto")
elif creditos==precio_repuesto:
    print("puedes comprar el repuesto pero no te sobraran creditos")
else:
    print("no tienes suficientes creditos para comprar el repuesto")
    
tipo_repuesto=input("ingresa el tipo de repuesto(motor, ala, escudo): ")
if tipo_repuesto=="motor" and creditos>=precio_repuesto and tipo_repuesto=="ala":
    print("puedes comprar el repuesto")
elif tipo_repuesto=="ala" and creditos>=precio_repuesto:
    print("puedes comprar el repuesto")
elif tipo_repuesto=="escudo" and creditos>=precio_repuesto:
    print("puedes comprar el repuesto")
else:
    print("tipo de repuesto no valido")