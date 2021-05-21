# se define diccionario "paciente"
paciente = {
    "id_diagnostico": (),
    "diag_ta":(),
    "diag_pa": (),
    "diag_do": (),
    "diag_dg": (),
    "diag_ca": ()
}

# se modifican las variables del diccionario
paciente["id-diagnostico"]= "d-001"
paciente["diag_ta"]= "si"
paciente["diag_pa"]= "no"
paciente["diag_do"]= "no"
paciente["diag_dg"]= "si"
paciente["diag_ca"]= "si"

def diagSintoma(paciente:dict)-> dict:
    id_diagnostico= paciente["id-diagnostico"]
    resultado=""
    estado=""
    
    if paciente["diag_ta"] == "si":
       if paciente["diag_pa"] == "si":
           if paciente["diag_do"] == "si":
               if paciente["diag_dg"] == "si":
                   if paciente["diag_ca"] == "si":
                       resultado= "Malaria"
                   if paciente["diag_ca"] == "no":
                        resultado= "Precencia de Sintomas"
               if paciente["diag_dg"] == "no":
                    resultado= "Precencia de Sintomas"
           if paciente["diag_do"] == "no": 
                resultado= "Precencia de Sintomas"
       if paciente["diag_pa"] == "no":
            if paciente["diag_do"] == "si":
                resultado= "Precencia de Sintomas"
            if paciente["diag_do"] == "no":
                if paciente["diag_dg"] == "si":
                    if paciente["diag_ca"] == "si":
                        resultado= "Gripa"
                    if paciente["diag_ca"] == "no":
                        resultado= "Precencia de Sintomas"    
                if paciente["diag_dg"] == "no":
                    resultado= "Precencia de Sintomas"                
    if paciente["diag_ta"] == "no":
        if paciente["diag_pa"] == "si":
            if paciente["diag_do"] == "si":
                if paciente["diag_dg"] == "si":
                    if paciente["diag_ca"] == "si":                   
                        resultado = "Precencia de Sintomas"
                    if paciente["diag_ca"] == "no":
                        resultado= "Otitis"
                if paciente["diag_dg"] == "no":
                    resultado= "Precencia de Sintomas"
            if paciente["diag_do"] == "no":
                resultado= "Precencia de Sintomas"
        if paciente["diag_pa"] == "no":
            if paciente["diag_do"] == "si" or paciente["diag_dg"] == "si" or paciente["diag_ca"] == "si":
                resultado= "Precencia de Sintomas"
            resultado= "No tiene sintomas"
    if resultado== "Otitis" or resultado=="Gripa" or resultado== "Malaria":
        estado= True
    else:
        estado= False
    return {"id_diagnostico": id_diagnostico, "resultado": resultado, "estado": estado }
print(diagSintoma(paciente))