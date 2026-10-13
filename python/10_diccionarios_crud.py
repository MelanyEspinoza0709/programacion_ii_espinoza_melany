from pickle import FALSE


droides=[
    {
        "codigo":"B1-001",
        "modelo":"B1",
        "energia":90,
        "activo":True   
    },
    {
        "codigo":"B1-002",
        "modelo":"B1",
        "energia":40,
        "activo":True   
    },
    {
        "codigo":"DRO-001",
        "modelo":"droideka",
        "energia":80,
        "activo":True   
    }
]

print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")

cantidad_droides=len(droides)
print(cantidad_droides)
nuevo_droide={
        "codigo":"B1-004",
        "modelo":"B1",
        "energia":100,
        "activo":True   
    }
#................CRUD................
#CREATE
droides.append(nuevo_droide)
print(len(droides))
print(droides)

print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")

#READ
droide=droides[2]
print(f"codigo: {droide["codigo"]}")
print(f"modelo: {droide["modelo"]}")
print(f"energia: {droide["energia"]}")
print(f"activo: {droide["activo"]}")

print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")

#UPDATE
droide=droides[2]
droide["codigo"]="DRO-002"
droide["cenergia"]=85
droide["activo"]=FALSE
print(f"droides:{droides}")

print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")

#DELETE

eliminado=droides.pop(2)
print(f"droides:{droides}")