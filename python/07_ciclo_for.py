#ciclo for

naves=[
    "Caza N-1", "Nave real de Nabbo", "Transporte"
]

for nave in naves:
    print("isnpeccionando",nave)
print("inspeccion realizada")

droides=range(1,17,3)
print("tipo de droides:", type(droides))
for droide in droides:
    print(f"reparar:droide B1- {droide}")
    print(f"tipo de dato droide: {type(droide)}")
    
print("*****************************************")

planetas=[
    "Naboo, tatooine, coruscant"
]

recorrido=enumerate(planetas,start=5)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipos de dato {type(posicion)}:{type(planeta)}")

print("*****************************************")

paises=["Ecuador", "venezuela", "chile","colombia ","brasil", "estados unidos"]

for pais in paises:
    if pais =="chile":
        continue
    if pais=="brasil":
        break
    print(f"pais visitado:{pais}")
    
print("*****************************************")

jedi={}
jedi_activo={
    "nombre":"obiwan",
    "fuerza":"120",
    "estilo_pelea":"samurai",
    "misiones": ["guerra alderan","secuestro palpatine", "escola de leia"],
    "descripción":
        {"estatura":1.80,
        "especie": "humana"
    }
}

print(jedi_activo)
nave=dict(nombre="AZ-1",capacidad=8, turbo_laser=2)
print(nave)

print("*****************************************")

jedi["nombre"] = "luck"
jedi["fuerza"]=150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave}: {valor}")