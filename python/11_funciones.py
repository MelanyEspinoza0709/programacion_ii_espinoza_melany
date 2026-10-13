#FUNCIONES

def activar_sistema():
    print("**sistema de naboo**")
    print("sistema de control activado")

activar_sistema()

#funciones con parametro

def saludar_jedi(nombre):
    print(f"que la fuerza te acompañe: {nombre}")
saludar_jedi("quin-gon jim")
saludar_jedi("obi-wan kenobi")

def mostrar_nave(nombre, combustible):
    print(f"nave: {nombre}")
    print(f"cantidad combustible: {combustible}")
    
mostrar_nave("Caza N-1", 80)

#funciones que devuelven dato o informacion
#return

def calcular_combustible(inicial, consumo):
    restante=inicial - consumo
    return restante

def calcular_combustible2(inicial, consumo):
    return inicial - consumo

resultado=calcular_combustible(100,25)
print(f"combustible: {resultado}")

resultado=calcular_combustible2(100,25)
print(f"combustible: {resultado}")
print(f"combustible:{calcular_combustible2(100,15)}")
