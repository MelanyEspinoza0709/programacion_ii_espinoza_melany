#operadores
#son los simbolos que nos permiten realizar operaciones matematicas y logicas con los valores de nuestras variables
"""
operadores aritméticos
+ suma
- resta
* multiplicación
/ división
// división entera
% módulo (residuo de la división :3)
** potencia
"""

valor1=10
valor2=3
suma=valor1+valor2
resta=valor1-valor2
multiplicacion=valor1*valor2
division=valor1/valor2
division_entera=valor1//valor2
modulo=valor1%valor2
potencia=valor1**valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Potencia:", potencia)   

print("tabla de multiplicar del 5:")
print("5 x 1 =", 5*1)
print("5 x 2 =", 5*2)
print("5 x 3 =", 5*3)
print("5 x 4 =", 5*4)
print("5 x 5 =", 5*5)


print("tabla de multiplicar del 7:")
multiplicador=7
print(multiplicador, "x 1 =", multiplicador*1)
print(multiplicador, "x 2 =", multiplicador*2)
print(multiplicador, "x 3 =", multiplicador*3)
print(multiplicador, "x 4 =", multiplicador*4)
print(multiplicador, "x 5 =", multiplicador*5)

print("area de un triangulo con base 5 y altura 10:", (5*10)/2)

#OPERADORES DE COMPARACION :3
#son los que nos permiten comparar dos valores y obtener un resultado booleano (True o False)

"""
- == igual que
- != diferente que significa que no es igual osea que es distinto uwu
- > mayor que
- < menor que
- >= mayor o igual que
- <= menor o igual que    
"""

velocidad_anakin=950
velocidad_sebulba=900

print("¿Anakin es más rápido que Sebulba?", velocidad_anakin>velocidad_sebulba)
print("¿Anakin es más lento que Sebulba?", velocidad_anakin<velocidad_sebulba)
print("¿Anakin es igual de rápido que Sebulba?", velocidad_anakin==velocidad_sebulba)
print("¿Anakin es diferente de Sebulba?", velocidad_anakin!=velocidad_sebulba)
print("¿Anakin es más rápido o igual que Sebulba?", velocidad_anakin>=velocidad_sebulba)
print("¿Anakin es más lento o igual que Sebulba?", velocidad_anakin<=velocidad_sebulba)

#OPEREADORES LOGICOOS JEJEJE
#son los que nos permiten combinar varias condiciones y obtener un resultado booleano (True o False)    

"""
- and (y)
- or (o)
- not (no)
"""

motores_funcionando=True
escudos_funcionando=False
combustible=80

print("todos los sistemas funcionando?", motores_funcionando and escudos_funcionando)
print("al menos un sistema funcionando?", motores_funcionando or escudos_funcionando)
print("sistema de motores no funcionando?", not motores_funcionando)

cantidad_motores=2
cantidad_alas=4
combustible=80

print("¿La nave tiene al menos 2 motores y 4 alas?")
print(cantidad_motores>=2 and cantidad_alas>=4 and combustible>50)
print("¿La nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores>=2 or cantidad_alas>=4 or combustible>50)
print("¿La nave no tiene al menos 2 motores?")
print(not cantidad_motores>=2 and combustible>=50 and cantidad_alas>=4)

#Operadores de asignación
#son los que nos permiten asignar un valor a una variable y realizar operaciones matemáticas con
#ese valor de manera más sencilla

"""
- = asignación
- += suma y asignación
- -= resta y asignación
- *= multiplicación y asignación
- /= división y asignación
- //= división entera y asignación
- %= módulo y asignación
- **= potencia y asignación
"""

velocidad=100
print("Velocidad inicial:", velocidad)
velocidad+=50
print("Velocidad después de acelerar:", velocidad)
velocidad-=30
print("Velocidad después de frenar:", velocidad)
multiplicador=2
velocidad*=multiplicador
print("Velocidad después de multiplicar por", multiplicador, ":", velocidad)
divisor=4
velocidad/=divisor
print("Velocidad después de dividir por", divisor, ":", velocidad)
modulo=7
velocidad%=modulo
print("Velocidad después de aplicar módulo", modulo, ":", velocidad)
velocidad**=2
print("Velocidad después de elevar al cuadrado:", velocidad)

#PRECEDENCIA DE OPERADORES
#es el orden en el que se ejecutan las operaciones matemáticas y lógicas en una expresión, de acuerdo a las reglas de la matemática y la lógica. 
"""
1. paréntesis ()
2. exponenciación **
3. multiplicación *, división /, división entera //, módulo %
4. suma +, resta -
5. operadores de comparación ==, !=, >, <, >=, <=
"""
resultado_1=10+5*2
print("resultado 1:", resultado_1)
resultado_2=(10+5)*2
print("resultado 2:", resultado_2)
resultado_3=10+5*2**2
print("resultado 3:", resultado_3)



