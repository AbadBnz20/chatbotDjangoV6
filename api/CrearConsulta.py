import re
def convertiradolar(amount):
    # Primero, eliminamos todos los espacios en blanco
    amount = amount.replace(" ", "")
    # Utilizamos expresiones regulares para buscar el patrón deseado
    match = re.search(r"\d+(\.\d+)?mil?|\d+(\.\d+)?", amount)
    if match:
        # Si se encuentra el patrón, extraemos el valor
        value = match.group()
        # Si el valor contiene la palabra "mill" y no está precedido por un número mayor a 9,
        # multiplicamos por mil; de lo contrario, multiplicamos por un millón.
        if "mil" in value:
            index = value.index("mil")
            if index > 1 and value[index-2:index].isdigit() and int(value[index-2:index]) > 9:
                value = float(value.replace("mil", "")) * 1000
            else:
                value = float(value.replace("mil", "")) * 1000
        else:
            value = float(value)
        # Devolvemos el valor con formato de dos decimales
        return f"{round(value)}"
    else:
        # Si no se encuentra el patrón, devolvemos None
        return None

def convertirnumero(num):
    num.replace(".", "")
    if 'bs' in num.lower() or 'bolivianos' in num.lower() :
        numero = re.sub("[^0-9]", "", num)
        # print(round(int(numero)/6.96))
        return round(int(numero)/6.96)
    else:
        numero = re.sub("[^0-9]", "", num)
        # print(numero)
        return numero
    

def crearConsulta(lista):
    servivios=True
    cambio=False
    propiedad=True
    query='INFO/IP/SELECT pr.idpropiedad,pr.descripcion,pr.tipo,pr.area,pr.metroscuadrados,pr.estadopropiedad,pr.precio FROM propiedad as pr inner join ubicacion as ub on pr.idpropiedad=ub.idpropiedad  '
    for index in lista:
        if(index =='lote' or index=='lotes' or index=='terreno' or index=='terrenos' or index=='propiedades'):
            if(propiedad):
                query+= "where pr.tipo='Terreno'"
                propiedad=False
        elif("$" in index.lower() or "dolares" in index.lower() or "bs" in index.lower() or "bolivianos" in index.lower()):
           
            if("bs" in index.lower() or "bolivianos" in index.lower()):
                cambio=True
            indice=lista.index(index)
            if(lista[indice-1]=='menor' or lista[indice-1]=='menores'  or lista[indice-1]=='maximo'):
                numero=convertirnumero(lista[indice])
                if(int(numero)<1000):
                    sifra=convertiradolar(f"{index}")
                    if(cambio):
                        sifra=round(int(sifra)/6.96)
                    query+=f" and pr.precio{'<'}{sifra}"
                else:
                    query+=f" and pr.precio{'<'}{numero}"           
            elif(lista[indice-1]=='mayor' or lista[indice-1]=='mayores' or lista[indice-1]=='minimo'):
                numero=convertirnumero(lista[indice])
                if(int(numero)<1000):
                    sifra=convertiradolar(f"{index}")
                    if(cambio):
                        sifra=round(int(sifra)/6.96)
                    query+=f" and pr.precio{'>'}{sifra}"
                else:
                    query+=f" and pr.precio{'>'}{numero}"  
            elif(lista[indice-1]=='de'):
                numero=convertirnumero(lista[indice])
                if(int(numero)<1000):
                    
                    sifra=convertiradolar(f"{index}")
                    if(cambio):
                        sifra=round(int(sifra)/6.96)
                    query+=f" and pr.precio{'='}{sifra}"
                else:
                    query+=f" and pr.precio{'='}{numero}" 
    
        elif("m2" in index.lower() or "metros" in index.lower()):
            indice=lista.index(index)
            if(lista[indice-1]=='menor' or lista[indice-1]=='minimo' or lista[indice-1]=='maximo'):
                numero = re.findall(r'\d+', index)
                query+=f" and pr.metroscuadrados{'<'}{numero[0]}"
            elif(lista[indice-1]=='mayor' or lista[indice-1]=='mayores' or lista[indice-1]=='minimo'):
                numero = re.findall(r'\d+', index)
                query+=f" and pr.metroscuadrados{'>'}{numero[0]}"
            elif(lista[indice-1]=="de"):
                numero = re.findall(r'\d+', index)
                query+=f" and pr.metroscuadrados{'='}{numero[0]}"
        elif("tarija" in index.lower() or "paz" in index.lower() or "potosi" in index.lower() or "oruro" in index.lower() or "sucre" in index.lower() or "cochabamba" in index.lower() or "cruz" in index.lower() or "beni" in index.lower() or "pando" in index.lower() ):
            query+=f" and LOWER(ub.departamento) LIKE '%{index.lower()}%'"
        elif( index.lower()=="en" or "barrio" in index.lower() or "bario" in index.lower() or "varrio" in index.lower() or "zona" in index.lower() or "sona" in index.lower()):
            indice=lista.index(index)
            cadena=lista[indice+1]
            print(cadena)
            if (cadena not in ["barrio", "zona","bario","varrio","sona","tarija","paz","potosi","oruro","sucre","cochabamba","cruz","beni","pando","en","central","centrica","centro"]):
                if cadena == "de": 
                    if(lista[indice+2] not in  ["tarija","paz","potosi","oruro","sucre","cochabamba","cruz","beni","pando"]):
                        query+=f" and LOWER(ub.barrio) LIKE '%{lista[indice+2].lower()}%'"
                else:
                    query+=f" and LOWER(ub.barrio) LIKE '%{cadena.lower()}%'"
                                                                                                                                                                                                                                                                                                                      
        elif("servicios" in index.lower() or "servicio" in index.lower() or "servisio" in index.lower() or "serbisio" in index.lower()   or "agua" in index.lower() or "luz" in index.lower() or "electricidad" in index.lower() or "gas" in index.lower()):
            if servivios:
                query+=" and (select count(sb.tipo) from propiedad as prs inner join propiedadservicio as ps ON prs.idpropiedad = ps.idpropiedad inner join serviciobasico as sb on ps.idservicio = sb.idservicio where prs.idpropiedad=pr.idpropiedad) >=2 "
                servivios=False
        elif(index.lower() in ["económico","económicos","economico","economicos"]):
            query+=" and pr.precio <=22000 "
        elif("central" in index.lower() or "centrica" in index.lower() or "centro" in index.lower()):
            query+=" and LOWER(ub.barrio) LIKE '%Narciso Campero%' or LOWER(ub.barrio) LIKE '%senac%' or LOWER(ub.barrio) LIKE '%las panosas%' or LOWER(ub.barrio) LIKE '%constructor%' or LOWER(ub.barrio) LIKE '%las panosas%' or LOWER(ub.barrio) LIKE '%morros blancos%' "

    return query
    
