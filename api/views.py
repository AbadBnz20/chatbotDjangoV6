from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
import json
import spacy
from spacy.matcher import Matcher
from api import CrearConsulta
from rest_framework.decorators import api_view

from django.http import HttpResponseServerError
# Create your views here.

@api_view(['POST'])
def generarConsulta(request):
    if request.method == 'POST':
        mi_cadena = request.body.decode('utf-8')
        mi_diccionario = json.loads(mi_cadena)
        print(mi_diccionario['cadena'])
        nlp = spacy.load('es_core_news_sm')
        matcher = Matcher(nlp.vocab)
       

        patterns = [
        [{"LOWER": {"IN": ["terreno", "terrenos","lote","lotes"]}}],
        # [{"LOWER":  {"IN": ["departamento", "provincia","barrio","bario","varrio","zona","sona"]}}, {}],
        [{"LOWER":  {"IN": ["departamento", "provincia","barrio","bario","varrio","zona","sona","en"]}}],

        # patrones de barrios
        [{"LOWER": "el"}, {"LOWER": "molino"}],
        [{"LOWER": "las"}, {"LOWER": "panosas"}],
        [{"LOWER": "san"}, {"LOWER": "roque"}],
        [{"LOWER": "la"}, {"LOWER": "pampa"}],
        [{"LOWER": "virgen"}, {"LOWER": "de"}, {"LOWER": "fátima"}],
        [{"LOWER": "la"}, {"LOWER": "loma"}, {"LOWER": "de"}, {"LOWER": "san"}, {"LOWER": "juan"}],
        [{"LOWER": "la"}, {"LOWER": "loma"}],
        [{"LOWER": "narciso"}, {"LOWER": "campero"}],
        [{"LOWER": "aranjuez"}],
        [{"LOWER": "miraflores"}],
        [{"LOWER": "el"}, {"LOWER": "tejar"}],
        [{"LOWER": "san"}, {"LOWER": "gerónimo"}],
        [{"LOWER": "petrolero"}],
        [{"LOWER": "san"}, {"LOWER": "blas"}],
        [{"LOWER": "san"}, {"LOWER": "juan"}],
        [{"LOWER": "la"}, {"LOWER": "banda"}],
        [{"LOWER": "villa"}, {"LOWER": "germán"}, {"LOWER": "busch"}],
        [ {"LOWER": "german"}, {"LOWER": "busch"}],
        [{"LOWER": "el"}, {"LOWER": "gallinazo"}],
        [{"LOWER": "rosedal"}],
        [{"LOWER": "juan"}, {"LOWER": "23"}],
        [{"LOWER": "san"}, {"LOWER": "martín"}],
        [{"LOWER": "san"}, {"LOWER": "martin"}],
        [{"LOWER": "fabril"}],
        [{"LOWER": "juan"}, {"LOWER": "nicolay"}],
        [{"LOWER": "4"}, {"LOWER": "de"}, {"LOWER": "julio"}],
        [{"LOWER": "central"}],
        [{"LOWER": "maría"}, {"LOWER": "de"}, {"LOWER": "los"}, {"LOWER": "ángeles"}],
        [{"LOWER": "maria"}, {"LOWER": "de"}, {"LOWER": "los"}, {"LOWER": "angeles"}],
        [{"LOWER": "chapacos"}],
        [{"LOWER": "3"}, {"LOWER": "de"}, {"LOWER": "mayo"}],
        [{"LOWER": "luis"}, {"LOWER": "de"}, {"LOWER": "fuentes"}],
        [{"LOWER": "urbanización"}, {"LOWER": "catedral"}],
        [{"LOWER": "catedral"}],
        [{"LOWER": "andalucía"}],
        [{"LOWER": "andalucia"}],
        [{"LOWER": "virgen"}, {"LOWER": "de"}, {"LOWER": "chaguaya"}],
        [{"LOWER": "san"}, {"LOWER": "jorge"}, {"LOWER": "2"}],
        [{"LOWER": "libertad"}],
        [{"LOWER": "2"}, {"LOWER": "de"}, {"LOWER": "mayo"}],
        [{"LOWER": "senac"}],
        [{"LOWER": "alto"}, {"LOWER": "senac"}],
        [{"LOWER": "tabladita"}],
        [{"LOWER": "tabladita"}, {"LOWER": "2"}],
        [{"LOWER": "san"}, {"LOWER": "antonio"}],
        [{"LOWER": "barrio"}, {"LOWER": "magisterio"}],
        [{"LOWER": "las"}, {"LOWER": "palmas"}],
        [{"LOWER": "méndez"}, {"LOWER": "arcos"}],
        [{"LOWER": "30"}, {"LOWER": "de"}, {"LOWER": "septiembre"}],
        [{"LOWER": "pedro"}, {"LOWER": "antonio"}, {"LOWER": "flores"}],
        [{"LOWER": "aniceto"}, {"LOWER": "arce"}],
        [{"LOWER": "palmarcito"}],
        [{"LOWER": "panamericano"}],
        [{"LOWER": "san"}, {"LOWER": "bernardo"}],
        [{"LOWER": "1"}, {"LOWER": "de"}, {"LOWER": "mayo"}],
        [{"LOWER": "méndez"}, {"LOWER": "arcos"}],
        [{"LOWER": "barrio"}, {"LOWER": "aeropuerto"}],
        [{"LOWER": "lourdes"}],
        [{"LOWER": "bartolinas"}],
        [{"LOWER": "los"}, {"LOWER": "álamos"}],
        [{"LOWER": "los"}, {"LOWER": "alamos"}],
        [{"LOWER": "las"}, {"LOWER": "velas"}],
        [{"LOWER": "luis"}, {"LOWER": "espinal"}],
        [{"LOWER": "las"}, {"LOWER": "pascuas"}],
        [{"LOWER": "morros"}, {"LOWER": "blancos"}],
        [{"LOWER": "simón"}, {"LOWER": "bolívar"}],
        [{"LOWER": "simon"}, {"LOWER": "bolivar"}],
        [{"LOWER": "torrecillas"}],
        [{"LOWER": "san"}, {"LOWER": "roque"}],
        [{"LOWER": "villa"}, {"LOWER": "abaroa"}],
        [{"LOWER": "villa"}, {"LOWER": "avaroa"}],
        [{"LOWER": "moto"}, {"LOWER": "méndez"}],
        [{"LOWER": "moto"}, {"LOWER": "mendez"}],
        [{"LOWER": "6"}, {"LOWER": "de"}, {"LOWER": "agosto"}],
        [{"LOWER": "salamanca"}],
        [{"LOWER": "san"}, {"LOWER": "josé"}],
        [{"LOWER": "san"}, {"LOWER": "jose"}],
        [{"LOWER": "san"}, {"LOWER": "luis"}],
        [{"LOWER": "la"}, {"LOWER": "florida"}],
        [{"LOWER": "villa"}, {"LOWER": "fátima"}],
        [{"LOWER": "villa"}, {"LOWER": "fatima"}],
        [{"LOWER": "santa"}, {"LOWER": "rosa"}],
        [{"LOWER": "oscar"}, {"LOWER": "zamora"}],
        [{"LOWER": "san"}, {"LOWER": "salvador"}],
        [{"LOWER": "simón"}, {"LOWER": "bolívar"}],
        [{"LOWER": "simon"}, {"LOWER": "bolivar"}],
        [{"LOWER": "las"}, {"LOWER": "retamas"}],
        [{"LOWER": "independencia"}],
        [{"LOWER": "jesús"}, {"LOWER": "de"}, {"LOWER": "nazaret"}],
        [{"LOWER": "jesus"}, {"LOWER": "de"}, {"LOWER": "nazaret"}],
        [{"LOWER": "26"}, {"LOWER": "de"}, {"LOWER": "agosto"}],
        [{"LOWER": "el"}, {"LOWER": "trigal"}],
        [{"LOWER": "tarija"}, {"LOWER": "linda"}],
        [{"LOWER": "27"}, {"LOWER": "de"}, {"LOWER": "mayo"}],
        [{"LOWER": "nueva"}, {"LOWER": "jerusalén"}],
        [{"LOWER": "nueva"}, {"LOWER": "jerusalen"}],
        [{"LOWER": "fray"}, {"LOWER": "quebracho"}],
        [{"LOWER": "las"}, {"LOWER": "laureles"}],
        [{"LOWER": "los"}, {"LOWER": "laureles"}],
        [{"LOWER": "laureles"}],
        [{"LOWER": "chapacos"}, {"LOWER": "2"}],
        [{"LOWER": "20"}, {"LOWER": "de"}, {"LOWER": "enero"}],
        [{"LOWER": "15"}, {"LOWER": "de"}, {"LOWER": "junio"}],
        [{"LOWER": "santa"}, {"LOWER": "fe"}],
        [{"LOWER": "la"}, {"LOWER": "cañada"}],
        [{"LOWER": "la"}, {"LOWER": "union"}],
        [{"LOWER": "guadalquivir"}],
        [{"LOWER": "tarijeños"}, {"LOWER": "en"}, {"LOWER": "progreso"}],
        [{"LOWER": "che"}, {"LOWER": "guevara"}],
        [{"LOWER": "temporal"}],
        [{"LOWER": "san"}, {"LOWER": "jorge"}, {"LOWER": "1"}],
        [{"LOWER": "las"}, {"LOWER": "retamas"}],
        [{"LOWER": "14"}, {"LOWER": "de"}, {"LOWER": "enero"}],
        [{"LOWER": "juan"}, {"LOWER": "pablo"}],
        [{"LOWER": "aeropuerto"}],
        [{"LOWER": "amalia"}, {"LOWER": "medinaceli"}],
        [{"LOWER": "la"}, {"LOWER": "huerta"}],
        [{"LOWER": "el"}, {"LOWER": "chañar"}],
        [{"LOWER": "monte"}, {"LOWER": "centro"}],
        [{"LOWER": "monte"}, {"LOWER": "sud"}],
        [{"LOWER": "eucaliptos"}],
        [{"LOWER": "corazón"}, {"LOWER": "de"}, {"LOWER": "jesus"}],
        [{"LOWER": "corazon"}, {"LOWER": "de"}, {"LOWER": "jesus"}],
        [{"LOWER": "la"}, {"LOWER": "torre"}],
        [{"LOWER": "universo"}],
        [{"LOWER": "artesanal"}],
        [{"LOWER": "baizal"}],
        [{"LOWER": "jardín"}, {"LOWER": "portillo"}],
        [{"LOWER": "6"}, {"LOWER": "de"}, {"LOWER": "abril"}],
        [{"LOWER": "japón"}],
        [{"LOWER": "1"}, {"LOWER": "de"}, {"LOWER": "abril"}],
        [{"LOWER": "san"}, {"LOWER": "pedro"}],
        [{"LOWER": "los"}, {"LOWER": "tajibos"}],
        [{"LOWER": "mirador"}, {"LOWER": "los"}, {"LOWER": "pinos"}],
        [{"LOWER": "28"}, {"LOWER": "de"}, {"LOWER": "enero"}],
        [{"LOWER": "manantial"}],
        [{"LOWER": "constructor"}],
        [{"LOWER": "victoria"}],
        [{"LOWER": "isaac"}, {"LOWER": "attie"}],
        [{"LOWER": "nueva"}, {"LOWER": "andalucía"}],
        [{"LOWER": "15"}, {"LOWER": "de"}, {"LOWER": "agosto"}],
        [{"LOWER": "el"}, {"LOWER": "rosal"}],
        [{"LOWER": "7"}, {"LOWER": "de"}, {"LOWER": "octubre"}],
        [{"LOWER": "loma"}, {"LOWER": "de"}, {"LOWER": "tomatitas"}],
        [{"LOWER": "luis"}, {"LOWER": "espinal"}],
        [{"LOWER": "nueva"}, {"LOWER": "terminal"}],
        [{"LOWER": "ex"}, {"LOWER": "terminal"}],
        [{"LOWER": "nuevo"}, {"LOWER": "amanecer"}],
        [{"LOWER": "san"}, {"LOWER": "cristobal"}],
        [{"LOWER": "san"}, {"LOWER": "mateo"}],
        [{"LOWER": "villa"}, {"LOWER": "olimpica"}],
        [{"LOWER": "exterminal"}],
        [{"LOWER": "santiago"}],
        [{"LOWER":  {"IN": ["tarija", "paz","oruro","potosi","sucre","cochabamba","cruz","beni","pando"]}}],
        [{"LOWER": {"IN": ["precio", "presio"]}}],
        [{"LOWER": {"IN": ["mayor", "menor","maximo","minimo","mayores","menores"]}}],
        [{"LOWER":"de"}],
        [{"TEXT": {"REGEX": r"\d+(?:\.\d+)?m2?"}}],
        [{"LOWER": {"REGEX": r"\d+(?:\.\d+)?bs?"}}],
        [{"LOWER": {"REGEX": r"\d+(?:\.\d+)?\$us"}}],      
        [{"TEXT": {"REGEX": r"\d+(?:\.\d+)?.000?"}},{"LOWER":  {"IN": ["m2", "metros","$","sus","dolares","bs","bolivianos","BOB"]}}],
        [{"IS_DIGIT": True},{"LOWER":  {"IN": ["m2", "metros","$","sus","dolares","bs","bolivianos","","BOB"]}}],
        [{"IS_DIGIT": True},{},{"LOWER":  {"IN": ["m2", "metros","$","sus","dolares","bs","bolivianos","BOB"]}}],
        [{"LOWER":  {"IN": ["agua", "electricidad","luz","servicios","servicio" ,"servisio" ,"serbisio","servisios" ,"serbisios" ]}}],
        [{"LOWER":  {"IN": ["económico","economico","economicos","económicos"]}}],
        [{"LOWER":  {"IN": ["central","centrica","centro"]}}],
        ]
        matcher.add("TEST_PATTERNS", patterns)
        doc = nlp(mi_diccionario['cadena'])
        matches=matcher(doc)
        lista=[]
        for match_id,start,end in matches:
            matched_span=doc[start:end]
            # print(matched_span.text)
            lista.append(matched_span.text)
        
        for index in lista:
            print(index)
        try:
            query= CrearConsulta.crearConsulta(lista)
            return JsonResponse({'status':200,'cadena': query})
        except Exception as e:
    
           return JsonResponse({'status':500,'cadena': ""})
    else:
        return HttpResponse(status=405)



@api_view(['POST'])
def validarContacto(request):
    mi_cadena = request.body.decode('utf-8')
    mi_diccionario = json.loads(mi_cadena)
    print(mi_diccionario['consulta'])
    nlp = spacy.load('es_core_news_sm')
    matcher = Matcher(nlp.vocab)
    patterns = [
    [{"LOWER": {"IN": ["pondra"]}}],
     [{"LOWER": {"IN": ["contacto"]}}],
     [{"LOWER": {"IN": ["agente"]}}],
     [{"LOWER": {"IN": ["enseguida"]}}],

    ]
    matcher.add("TEST_PATTERNS", patterns)
    doc = nlp(mi_diccionario['consulta'])
    matches=matcher(doc)
    lista=[]
    for match_id,start,end in matches:
        matched_span=doc[start:end]
        lista.append(matched_span.text)
    print(len(lista))
    
    if len(lista)>=3:
        return JsonResponse({'status':200,'responde': True})
    else:
        return JsonResponse({'status':200,'responde': False})



@api_view(['POST'])
def validarConsulta(request):
    mi_cadena = request.body.decode('utf-8')
    mi_diccionario = json.loads(mi_cadena)
    print(mi_diccionario['consulta'])
    nlp = spacy.load('es_core_news_sm')
    matcher = Matcher(nlp.vocab)
    patterns = [
    [{"LOWER": {"IN": ["busco","buscando","interesa","mostrarme","gustaria","Necesito","Quiero","consulta","informacion","proporcionarme","precio","presio","detalles","detalle","solicitar"]}}],
    [{"LOWER": {"IN": ["terreno","lotes","lote","barrio","terrenos"]}}],
    [{"LOWER": {"IN": ["oferta","ofertas"]}}],
    [{"TEXT": {"REGEX": r"\d+(?:\.\d+)?m2?"}}],
    [{"LOWER": {"REGEX": r"\d+(?:\.\d+)?bs?"}}],
    [{"LOWER": {"REGEX": r"\d+(?:\.\d+)?\$us"}}],      
    [{"TEXT": {"REGEX": r"\d+(?:\.\d+)?.000?"}},{"LOWER":  {"IN": ["m2", "metros","$","sus","dolares","bs","bolivianos","BOB"]}}],
    ]
    matcher.add("TEST_PATTERNS", patterns)
    doc = nlp(mi_diccionario['consulta'])
    matches=matcher(doc)
    lista=[]
    for match_id,start,end in matches:
        matched_span=doc[start:end]
        lista.append(matched_span.text)
    print(len(lista))
    
    if len(lista)>=2:
        return JsonResponse({'status':200,'responde': True})
    else:
        return JsonResponse({'status':200,'responde': False})
    


    


