from random import choice

wordList = (
    "rosa",
    "rojo",
    "verde",
    "azul",
    "amarillo",
    "naranja",
    "morado",
    "humo",
    "gris",
    "huye",
    "correr",
    "bota",
    "malas",
    "perro",
    "gato",
    "casa",
    "mesa",
    "luz",
    "hojas",
    "arbol",
    "jugar",
    "piedra",
    "hojas",
    "arbol",
    "jugar",
    "piedra",
    "mundo",
    "mujer",
    "hombre",
    "hola",
    "caer",
    "calle",
    "cama",
    "cambiar",
    "cambio",
    "caminar",
    "camino",
    "campana",
    "malos",
    "preso",
    "presos",
    "presion",
    "presidente",
    "presidir",
    "prestar",
    "prestigio",
    "presumir",
    "presunto",
    "presupuesto",
    "ganar",
    "ganarse",
    "gancho",
    "ganga",
    "ganso",
    "garaje",
    "garantia",
    "garantizar",
    "garbanzo",
    "tomar",
    "tomarse",
    "tonelada",
    "garra",
    "gas",
    "gasa",
    "gastar",
    "gasto",
    "gata",
    "raya",
    "hoyo",
    "asar",
    "pollo",
    "papa",
    "alas",
    "alba",
    "pato",
    "pesa",
    "palo",
    "abajo",
    "oler",
    "arar",
    "mito",
    "pero",
    "sala",
    "sano",
    "toma",
    "vino",
    "voto",
    "yoga",
    "moto",
    "pato",
    "raso",
    "saco",
    "abandonar",
    "irse",
    "abrir",
    "absoluta",
    "absoluto",
    "abuelo",
    "acabar",
    "acaso",
    "acciones",
    "accion",
    "aceptar",
    "acercar",
    "acompanar",
    "acordar",
    "actitud",
    "actividad",
    "acto",
    "actual",
    "actuar",
    "acudir",
    "acuerdo",
    "adelante",
    "ademas",
    "adquirir",
    "advertir",
    "afectar",
    "afirmar",
    "agua",
    "ahora",
    "ahi",
    "aire",
    "al",
    "alcanzar",
    "alejar",
    "alemana",
    "aleman",
    "algo",
    "alguien",
    "alguna",
    "alguno",
    "algun",
    "alla",
    "alli",
    "alma",
    "alta",
    "alto",
    "altura",
    "amar",
    "ambas",
    "ambos",
    "americana",
    "americano",
    "amiga",
    "amigo",
    "amor",
    "amplia",
    "amplio",
    "andar",
    "animal",
    "ante",
    "anterior",
    "antigua",
    "antiguo",
    "anunciar",
    "analisis",
    "aparecer",
    "apenas",
    "aplicar",
    "apoyar",
    "aprender",
    "aprovechar",
    "aquel",
    "aquella",
    "aquello",
    "aqui",
    "arma",
    "arriba",
    "arte",
    "asegurar",
    "aspecto",
    "asunto",
    "asi",
    "atenciones",
    "atencion",
    "atreverse",
    "atras",
    "aumentar",
    "aun",
    "aunque",
    "autor",
    "autora",
    "autoridad",
    "autentica",
    "autentico",
    "avanzar",
    "ayer",
    "ayuda",
    "ayudar",
    "azul",
    "anadir",
    "ano",
    "aun",
    "baja",
    "bajar",
    "barrio",
    "base",
    "bastante",
    "bastar",
    "beber",
    "bien",
    "blanca",
    "blanco",
    "boca",
    "brazo",
    "buen",
    "buscar",
    "caballo",
    "caber",
    "cabeza",
    "cabo",
    "cada",
    "cadena",
    "caer",
    "calle",
    "cama",
    "cambiar",
    "cambio",
    "caminar",
    "camino",
    "campana",
    "campo",
    "cantar",
    "cantidad",
    "capaces",
    "capacidad",
    "capaz",
    "capital",
    "cara",
    "caracteres",
    "carne",
    "carrera",
    "carta",
    "caracter",
    "casa",
    "casar",
    "casi",
    "caso",
    "catalan",
    "causa",
    "celebrar",
    "central",
    "centro",
    "cerebro",
    "cerrar",
    "chica",
    "chico",
    "cielo",
    "ciencia",
    "ciento",
    "cientifica",
    "cientifico",
    "cierta",
    "cierto",
    "cinco",
    "cine",
    "circunstancia",
    "ciudad",
    "ciudadana",
    "ciudadano",
    "civil",
    "clara",
    "claro",
    "clase",
    "coche",
    "coger",
    "colocar",
    "color",
    "comentar",
    "comenzar",
    "comer",
    "como",
    "companera",
    "companero",
    "compania",
    "completo",
    "comprar",
    "comprender",
    "comprobar",
    "comunes",
    "comunicaciones",
    "comunicacion",
    "comun",
    "con",
    "concepto",
    "conciencia",
    "concreto",
    "condicion",
    "condisiones",
    "conducir",
    "conjunto",
    "conocer",
    "conocimiento",
    "consecuencia",
    "conseguir",
    "conservar",
    "considerar",
    "consistir",
    "constante",
    "constituir",
    "construir",
    "contacto",
    "contar",
    "contemplar",
    "contener",
    "contestar",
    "continuar",
    "contra",
    "contrario",
    "control",
    "controlar",
    "convencer",
    "conversacion",
    "convertir",
    "corazon",
    "correr",
    "corresponder",
    "corriente",
    "cortar",
    "cosa",
    "costumbre",
    "crear",
    "crecer",
    "creer",
    "crisis",
    "cruzar",
    "cuadro",
    "cual",
    "cualquier",
    "cuando",
    "cuanto",
    "cuarta",
    "cuarto",
    "cuatro",
    "cubrir",
    "cuenta",
    "cuerpo",
    "cuestiones",
    "cuestion",
    "cultura",
    "cultural",
    "cumplir",
    "cuya",
    "cuyo",
    "cual",
    "cuanto",
    "celula",
    "como",
    "dar",
    "dato",
    "de",
    "deber",
    "decidir",
    "decir",
    "decision",
    "declarar",
    "dedicar",
    "dedo",
    "defender",
    "defensa",
    "definir",
    "definitivo",
    "dejar",
    "del",
    "demasiado",
    "democracia",
    "demostrar",
    "demas",
    "depender",
    "derecha",
    "derecho",
    "desaparecer",
    "desarrollar",
    "desarrollo",
    "desconocer",
    "descubrir",
    "desde",
    "desear",
    "deseo",
    "despertar",
    "despues",
    "destino",
    "detener",
    "determinar",
    "diaria",
    "diario",
    "diez",
    "diferencia",
    "diferente",
    "dificultad",
    "dificil",
    "dinero",
    "dios",
    "diosa",
    "direccion",
    "directo",
    "director",
    "directora",
    "dirigir",
    "disponer",
    "distancia",
    "distinto",
    "diverso",
    "doble",
    "doctor",
    "doctora",
    "dolor",
    "don",
    "donde",
    "dormir",
    "dos",
    "duda",
    "durante",
    "duro",
    "dia",
    "donde",
    "e",
    "echar",
    "economico",
    "edad",
    "efecto",
    "ejemplo",
    "ejercito",
    "el",
    "eleccion",
    "elegir",
    "elemento",
    "elevar",
    "ella",
    "empezar",
    "empresa",
    "en",
    "encender",
    "encima",
    "encontrar",
    "encuentro",
    "energia",
    "enfermedad",
    "enfermo",
    "enorme",
    "ensenar",
    "entender",
    "enterar",
    "entonces",
    "entrada",
    "entrar",
    "entre",
    "entregar",
    "enviar",
    "equipo",
    "error",
    "esa",
    "escapar",
    "escribir",
    "escritor",
    "escritora",
    "escuchar",
    "ese",
    "esfuerzo",
    "eso",
    "espacio",
    "espalda",
    "espana",
    "espanol",
    "espanola",
    "especial",
    "especie",
    "esperanza",
    "esperar",
    "espiritu",
    "esta",
    "establecer",
    "estado",
    "estar",
    "este",
    "esto",
    "estrella",
    "estructura",
    "estudiar",
    "estudio",
    "etapa",
    "europa",
    "europea",
    "europeo",
    "evidente",
    "evitar",
    "exacta",
    "exacto",
    "exigir",
    "existencia",
    "existir",
    "experiencia",
    "explicar",
    "expresion",
    "extender",
    "exterior",
    "extranjera",
    "extranjero",
    "extrano",
    "extremo",
    "falta",
    "faltar",
    "familia",
    "familiar",
    "famoso",
    "fenomeno",
    "fiesta",
    "figura",
    "fijar",
    "fin",
    "final",
    "flor",
    "fondo",
    "forma",
    "formar",
    "francesa",
    "francia",
    "frances",
    "frase",
    "frecuencia",
    "frente",
    "fria",
    "frio",
    "fuego",
    "fuente",
    "fuerte",
    "fuerza",
    "funcionar",
    "funcion",
    "fundamental",
    "futuro",
    "facil",
    "fisico",
    "futbol",
    "ganar",
    "general",
    "gente",
    "gesto",
    "gobierno",
    "golpe",
    "gracia",
    "gran",
    "grande",
    "grave",
    "gritar",
    "grupo",
    "guardar",
    "guerra",
    "gustar",
    "gusto",
    "haber",
    "habitacion",
    "habitual",
    "hablar",
    "hacer",
    "hacia",
    "hallar",
    "hasta",
    "hecha",
    "hecho",
    "hermana",
    "hermano",
    "hermosa",
    "hermoso",
    "hija",
    "hijo",
    "historia",
    "historico",
    "hombre",
    "hombro",
    "hora",
    "hoy",
    "humana",
    "humano",
    "idea",
    "iglesia",
    "igual",
    "imagen",
    "imaginar",
    "impedir",
    "imponer",
    "importancia",
    "importante",
    "importar",
    "imposible",
    "imagenes",
    "incluir",
    "incluso",
    "indicar",
    "individuo",
    "informaciones",
    "informacion",
    "informar",
    "inglesa",
    "ingles",
    "iniciar",
    "inmediata",
    "inmediato",
    "insistir",
    "instante",
    "intentar",
    "interesar",
    "intereses",
    "interior",
    "internacional",
    "interes",
    "introducir",
    "ir",
    "izquierda",
    "jamas",
    "jefa",
    "jefe",
    "joven",
    "juego",
    "jugador",
    "jugar",
    "juicio",
    "junto",
    "justo",
    "labio",
    "lado",
    "lanzar",
    "largo",
    "lector",
    "lectora",
    "leer",
    "lengua",
    "lenguaje",
    "lento",
    "levantar",
    "ley",
    "libertad",
    "libre",
    "libro",
    "limitar",
    "literatura",
    "llamar",
    "llegar",
    "llenar",
    "lleno",
    "llevar",
    "llorar",
    "lo",
    "loca",
    "loco",
    "lograr",
    "lucha",
    "luego",
    "lugar",
    "luz",
    "linea",
    "madre",
    "mal",
    "mala",
    "malo",
    "mandar",
    "manera",
    "manifestar",
    "mano",
    "mantener",
    "mar",
    "marcar",
    "marcha",
    "marchar",
    "marido",
    "mas",
    "masa",
    "matar",
    "materia",
    "material",
    "mayor",
    "mayoria",
    "mata",
    "matar",
    "materia",
    "material",
    "manana",
    "media",
    "mediante",
    "medida",
    "medio",
    "mejor",
    "memoria",
    "menor",
    "menos",
    "menudo",
    "mercado",
    "merecer",
    "mes",
    "mesa",
    "meter",
    "metro",
    "mi",
    "miedo",
    "miembro",
    "mientras",
    "mil",
    "militar",
    "millon",
    "ministra",
    "ministro",
    "minuto",
    "mirada",
    "mirar",
    "mis",
    "mismo",
    "mitad",
    "modelo",
    "moderna",
    "moderno",
    "modo",
    "mayo",
    "mecanica",
    "mito",
    "mecanico",
    "momento",
    "loma",
    "manana",
    "media",
    "mediante",
    "medida",
    "medio",
    "mejor",
    "memoria",
    "menor",
    "menos",
    "menudo",
    "mercado",
    "merecer",
    "mes",
    "mesa",
    "meter",
    "metro",
    "mi",
    "miedo",
    "miembro",
    "mientras",
    "mil",
    "militar",
    "millon",
    "ministra",
    "ministro",
    "minuto",
    "mirada",
    "mirar",
    "mis",
    "mismo",
    "mitad",
    "modelo",
    "moderna",
    "moderno",
    "modo",
    "momento",
    "moral",
    "morir",
    "mostrar",
    "motivo",
    "mover",
    "movimiento",
    "muchacha",
    "muchacho",
    "mucho",
    "muerte",
    "mujer",
    "mujeres",
    "mundial",
    "mundo",
    "muy",
    "maquina",
    "mas",
    "maximo",
    "medica",
    "medico",
    "metodo",
    "mi",
    "mia",
    "minima",
    "minimo",
    "mio",
    "musica",
    "nacer",
    "nacional",
    "nada",
    "nadie",
    "natural",
    "naturaleza",
    "necesaria",
    "necesario",
    "necesidad",
    "necesitar",
    "negar",
    "negocio",
    "negra",
    "negro",
    "ni",
    "ninguna",
    "ninguno",
    "ningun",
    "nivel",
    "nina",
    "nino",
    "no",
    "noche",
    "nombre",
    "normal",
    "norteamericana",
    "norteamericano",
    "notar",
    "noticia",
    "novela",
    "nuestra",
    "nuestro",
    "nueva",
    "nuevo",
    "nunca",
    "numero",
    "o",
    "objetivo",
    "objeto",
    "obligar",
    "obra",
    "observar",
    "obtener",
    "ocasiones",
    "ocasion",
    "ocho",
    "ocupar",
    "ocurrir",
    "oficial",
    "ofrecer",
    "ojo",
    "olvidar",
    "operacion",
    "opinion",
    "origen",
    "oro",
    "origenes",
    "oscura",
    "oscuro",
    "otra",
    "otro",
    "oir",
    "paciente",
    "pala",
    "pare",
    "peto",
    "piso",
    "pago",
    "padre",
    "pagar",
    "palabra",
    "papel",
    "par",
    "para",
    "parar",
    "parecer",
    "pared",
    "pareja",
    "parte",
    "participar",
    "particular",
    "partido",
    "partir",
    "pasa",
    "pasado",
    "pasar",
    "paso",
    "paz",
    "pais",
    "paises",
    "pecho",
    "pedir",
    "peligro",
    "pelo",
    "pelicula",
    "pena",
    "pensamiento",
    "pensar",
    "peor",
    "pequena",
    "pequeno",
    "hola",
    "caer",
    "calle",
    "cama",
    "cambiar",
    "cambio",
    "caminar",
    "camino",
    "campana",
    "campo",
    "cantar",
    "cantidad",
    "capaces",
    "capacidad",
    "capaz",
    "capital",
    "cara",
    "caracteres",
    "carne",
    "carrera",
    "carta",
    "caracter",
    "casa",
    "casar",
    "casi",
    "caso",
    "catalan",
    "causa",
    "celebrar",
    "central",
    "centro",
    "cerebro",
    "cerrar",
    "chica",
    "chico",
    "cielo",
    "ciencia",
    "ciento",
    "cientifica",
    "cientifico",
    "cierta",
    "cierto",
    "cinco",
    "cine",
    "circunstancia",
    "ciudad",
    "ciudadana",
    "ciudadano",
    "civil",
    "clara",
    "claro",
    "clase",
    "coche",
    "coger",
    "colocar",
    "color",
    "comentar",
    "comenzar",
    "comer",
    "como",
    "companera",
    "companero",
    "compania",
    "completo",
    "comprar",
    "comprender",
    "comprobar",
    "comunes",
    "comunicaciones",
    "comunicacion",
    "comun",
    "con",
    "concepto",
    "conciencia",
    "concreto",
    "condicion",
    "condisiones",
    "conducir",
    "conjunto",
    "conocer",
    "conocimiento",
    "consecuencia",
    "conseguir",
    "conservar",
    "considerar",
    "consistir",
    "constante",
    "constituir",
    "construir",
    "contacto",
    "contar",
    "contemplar",
    "contener",
    "contestar",
    "continuar",
    "contra",
    "contrario",
    "control",
    "controlar",
    "convencer",
    "conversacion",
    "convertir",
    "corazon",
    "correr",
    "corresponder",
    "corriente",
    "cortar",
    "cosa",
    "costumbre",
    "crear",
    "crecer",
    "creer",
    "crisis",
    "cruzar",
    "cuadro",
    "cual",
    "cualquier",
    "cuando",
    "cuanto",
    "cuarta",
    "cuarto",
    "cuatro",
    "cubrir",
    "cuenta",
    "cuerpo",
    "cuestiones",
    "cuestion",
    "cultura",
    "cultural",
    "cumplir",
    "cuya",
    "cuyo",
    "cual",
    "cuanto",
    "celula",
    "comer",
    "comernos",
    "como",
    "dar",
    "dato",
    "de",
    "deber",
    "decidir",
    "decir",
    "decision",
    "declarar",
    "dedicar",
    "dedo",
    "defender",
    "defensa",
    "definir",
    "definitivo",
    "dejar",
    "del",
    "demasiado",
    "democracia",
    "demostrar",
    "demas",
    "depender",
    "derecha",
    "derecho",
    "desaparecer",
    "desarrollar",
    "desarrollo",
    "desconocer",
    "descubrir",
    "desde",
    "desear",
    "deseo",
    "despertar",
    "despues",
    "destino",
    "detener",
    "determinar",
    "diaria",
    "diario",
    "diez",
    "diferencia",
    "diferente",
    "dificultad",
    "dificil",
    "dinero",
    "dios",
    "diosa",
    "direccion",
    "directo",
    "director",
    "directora",
    "dirigir",
    "disponer",
    "distancia",
    "distinto",
    "diverso",
    "doble",
    "doctor",
    "doctora",
    "dolor",
    "don",
    "donde",
    "dormir",
    "dos",
    "duda",
    "durante",
    "duro",
    "dia",
    "donde",
    "e",
    "echar",
    "economico",
    "edad",
    "efecto",
    "ejemplo",
    "ejercito",
    "el",
    "eleccion",
    "elegir",
    "elemento",
    "elevar",
    "ella",
    "empezar",
    "empresa",
    "en",
    "encender",
    "encima",
    "encontrar",
    "encuentro",
    "energia",
    "enfermedad",
    "enfermo",
    "enorme",
    "ensenar",
    "entender",
    "enterar",
    "entonces",
    "entrada",
    "entrar",
    "entre",
    "entregar",
    "enviar",
    "equipo",
    "error",
    "esa",
    "escapar",
    "escribir",
    "escritor",
    "escritora",
    "escuchar",
    "ese",
    "esfuerzo",
    "eso",
    "espacio",
    "espalda",
    "espana",
    "espanol",
    "espanola",
    "especial",
    "especie",
    "esperanza",
    "esperar",
    "espiritu",
    "esta",
    "establecer",
    "estado",
    "estar",
    "este",
    "esto",
    "estrella",
    "estructura",
    "estudiar",
    "estudio",
    "etapa",
    "europa",
    "europea",
    "europeo",
    "evidente",
    "evitar",
    "exacta",
    "exacto",
    "exigir",
    "existencia",
    "existir",
    "experiencia",
    "explicar",
    "expresion",
    "extender",
    "exterior",
    "extranjera",
    "extranjero",
    "extrano",
    "extremo",
    "falta",
    "faltar",
    "familia",
    "familiar",
    "famoso",
    "fenomeno",
    "fiesta",
    "figura",
    "fijar",
    "fin",
    "final",
    "flor",
    "fondo",
    "forma",
    "formar",
    "francesa",
    "francia",
    "frances",
    "frase",
    "frecuencia",
    "frente",
    "fria",
    "frio",
    "fuego",
    "fuente",
    "fuerte",
    "fuerza",
    "funcionar",
    "funcion",
    "fundamental",
    "futuro",
    "facil",
    "fisico",
    "futbol",
    "ganar",
    "general",
    "gente",
    "gesto",
    "gobierno",
    "golpe",
    "gracia",
    "gran",
    "grande",
    "grave",
    "gritar",
    "grupo",
    "guardar",
    "guerra",
    "gustar",
    "gusto",
    "haber",
    "habitacion",
    "habitual",
    "hablar",
    "hacer",
    "hacia",
    "hallar",
    "hasta",
    "hecha",
    "hecho",
    "hermana",
    "hermano",
    "hermosa",
    "hermoso",
    "hija",
    "hijo",
    "historia",
    "historico",
    "hombre",
    "hombro",
    "hora",
    "hoy",
    "humana",
    "humano",
    "idea",
    "iglesia",
    "igual",
    "imagen",
    "imaginar",
    "impedir",
    "imponer",
    "importancia",
    "importante",
    "importar",
    "imposible",
    "imagenes",
    "incluir",
    "incluso",
    "indicar",
    "individuo",
    "informaciones",
    "informacion",
    "informar",
    "inglesa",
    "ingles",
    "iniciar",
    "inmediata",
    "inmediato",
    "insistir",
    "instante",
    "intentar",
    "interesar",
    "intereses",
    "interior",
    "internacional",
    "interes",
    "introducir",
    "ir",
    "izquierda",
    "jamas",
    "jefa",
    "jefe",
    "joven",
    "juego",
    "jugador",
    "jugar",
    "juicio",
    "junto",
    "justo",
    "labio",
    "lado",
    "lanzar",
    "largo",
    "lector",
    "lectora",
    "leer",
    "lengua",
    "lenguaje",
    "lento",
    "levantar",
    "ley",
    "libertad",
    "libre",
    "libro",
    "limitar",
    "literatura",
    "llamar",
    "llegar",
    "llenar",
    "lleno",
    "llevar",
    "llorar",
    "lo",
    "loca",
    "loco",
    "lograr",
    "lucha",
    "luego",
    "lugar",
    "luz",
    "linea",
    "madre",
    "mal",
    "mala",
    "malo",
    "mandar",
    "manera",
    "manifestar",
    "mano",
    "mantener",
    "mar",
    "marcar",
    "marcha",
    "marchar",
    "marido",
    "mas",
    "masa",
    "matar",
    "materia",
    "material",
    "mayor",
    "mayoria",
    "manana",
    "media",
    "mediante",
    "medida",
    "medio",
    "mejor",
    "memoria",
    "menor",
    "menos",
    "menudo",
    "mercado",
    "merecer",
    "mes",
    "mesa",
    "meter",
    "metro",
    "mi",
    "miedo",
    "miembro",
    "mientras",
    "mil",
    "militar",
    "millon",
    "ministra",
    "ministro",
    "minuto",
    "mirada",
    "mirar",
    "mis",
    "mismo",
    "mitad",
    "modelo",
    "moderna",
    "moderno",
    "modo",
    "momento",
    "moral",
    "morir",
    "mostrar",
    "motivo",
    "mover",
    "movimiento",
    "muchacha",
    "muchacho",
    "mucho",
    "muerte",
    "mujer",
    "mujeres",
    "mundial",
    "mundo",
    "muy",
    "mucama",
    "maquina",
    "mas",
    "maximo",
    "medica",
    "medico",
    "metodo",
    "mi",
    "mia",
    "minima",
    "minimo",
    "mio",
    "musica",
    "nacer",
    "nacional",
    "nada",
    "nadie",
    "natural",
    "naturaleza",
    "necesaria",
    "necesario",
    "necesidad",
    "necesitar",
    "negar",
    "negocio",
    "negra",
    "negro",
    "ni",
    "ninguna",
    "ninguno",
    "ningun",
    "nivel",
    "nina",
    "nino",
    "no",
    "noche",
    "nombre",
    "normal",
    "norteamericana",
    "norteamericano",
    "notar",
    "noticia",
    "novela",
    "nuestra",
    "nuestro",
    "nueva",
    "nuevo",
    "nunca",
    "numero",
    "o",
    "objetivo",
    "objeto",
    "obligar",
    "obra",
    "observar",
    "obtener",
    "ocasiones",
    "ocasion",
    "ocho",
    "ocupar",
    "ocurrir",
    "oficial",
    "ofrecer",
    "ojo",
    "olvidar",
    "operacion",
    "opinion",
    "origen",
    "oro",
    "origenes",
    "oscura",
    "oscuro",
    "otra",
    "otro",
    "oir",
    "paciente",
    "padre",
    "pagar",
    "palabra",
    "papel",
    "par",
    "para",
    "parar",
    "parecer",
    "pared",
    "pareja",
    "parte",
    "participar",
    "particular",
    "partido",
    "partir",
    "pasa",
    "pasado",
    "pasar",
    "paso",
    "paz",
    "pais",
    "paises",
    "pecho",
    "pedir",
    "peligro",
    "pelo",
    "pelicula",
    "pena",
    "pensamiento",
    "pensar",
    "peor",
    "pequena",
    "pequeno",
    "paisajes",
    "palabra",
    "palabras",
    "papel",
    "papeles",
    "par",
    "para",
    "parada",
    "parado",
    "parados",
    "parar",
    "parecer",
    "pared",
    "paredes",
    "pareja",
)


# instances of class Letter
class First:
    def __init__(self, Super):
        self.Super = Super
        self.words_li = []

    def Run(self, first):
        pas_letter = False
        if first == "a":
            letter = "á"
        elif first == "e":
            letter = "é"
        elif first == "i":
            letter = "í"
        elif first == "o":
            letter = "ó"
        elif first == "u":
            letter = "ú"
        else:
            letter = None
        for i in wordList:
            if i[0] == first or i[0] == letter:
                pas_letter = True
                self.words_li.append(i)
            elif pas_letter == True:
                break
        try:
            if (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_Word_By"
            ):
                return choice(self.words_li)
            elif (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_List_By"
            ):
                return self.words_li
        except:
            raise Exception("Error")


class Last:
    def __init__(self, Super):
        self.Super = Super
        self.words_li = []

    def Run(self, last):
        if last == "a":
            letter = "á"
        elif last == "e":
            letter = "é"
        elif last == "i":
            letter = "í"
        elif last == "o":
            letter = "ó"
        elif last == "u":
            letter = "ú"
        else:
            letter = None
        for i in wordList:
            if i[len(i) - 1] == last or i[len(i) - 1] == None:
                self.words_li.append(i)
        try:
            if (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_Word_By"
            ):
                return choice(self.words_li)
            elif (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_List_By"
            ):
                return self.words_li
        except:
            error = True
        if error:
            raise Exception(f"Have not find word with '{last}' on the last letter.")


class These:
    def __init__(self, Super):
        self.Super = Super
        self.words_li = []

    def Run(self, these):
        for word in wordList:
            for char in these:
                if char not in word:
                    pas_letter = False
                    if char == "a":
                        char = "á"
                    elif char == "e":
                        char = "é"
                    elif char == "i":
                        char = "í"
                    elif char == "o":
                        char = "ó"
                    elif char == "u":
                        char = "ú"
                    if char not in word:
                        pas_letter = False
                        break
                    else:
                        pas_letter = True
                    if not pas_letter:
                        break
                else:
                    pas_letter = True
            if pas_letter == True:
                self.words_li.append(word)
        try:
            if (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_Word_By"
            ):
                return choice(self.words_li)
            elif (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_List_By"
            ):
                return self.words_li
        except:
            error = True
        if error:
            raise Exception(
                f"Have not find word that contains the next letters '{these}'"
            )


class Times:
    def __init__(self, Super):
        self.Super = Super
        self.words_li = []

    def Run(self, char, **kw):
        error = None
        Udieresis = " "
        if char == "a":
            letter = "á"
        elif char == "e":
            letter = "é"
        elif char == "i":
            letter = "í"
        elif char == "o":
            letter = "ó"
        elif char == "u":
            letter = "ú"
            Udieresis = "ü"
        else:
            letter = " "
        if len(kw) == 1:
            if "exact" in kw:
                condit = "exact"
            elif "max" in kw:
                condit = "max"
            elif "min" in kw:
                condit = "min"
            else:
                error = "bad_args"
        elif len(kw) == 2:
            if "max" in kw and "min" in kw:
                condit = "max-min"
            else:
                error = "bad_args"
        else:
            error = "bad_args"
        if error == "bad_args":
            raise Exception(
                'Arguments must be "exact" or "min" or "max" or ("min" and "max")'
            )
        if condit == "max-min":
            if kw["max"] < kw["min"]:
                raise Exception('"min" must be less than "max"')
        for word in wordList:
            if condit == "exact":
                if (
                    word.count(char) + word.count(letter) + word.count(Udieresis)
                ) == kw["exact"]:
                    self.words_li.append(word)
            elif condit == "min":
                if (
                    word.count(char) + word.count(letter) + word.count(Udieresis)
                ) >= kw["min"]:
                    self.words_li.append(word)
            elif condit == "max":
                if (
                    word.count(char) + word.count(letter) + word.count(Udieresis)
                ) <= kw["max"]:
                    self.words_li.append(word)
            elif condit == "max-min":
                if (
                    (word.count(char) + word.count(letter) + word.count(Udieresis))
                    >= kw["min"]
                ) and (
                    word.count(char) + word.count(letter) + word.count(Udieresis)
                ) <= kw[
                    "max"
                ]:
                    self.words_li.append(word)
        try:
            if (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_Word_By"
            ):
                return choice(self.words_li)
            elif (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_List_By"
            ):
                return self.words_li
        except:
            Index_error = True
        if Index_error:
            if condit == "exact":
                raise Exception(
                    f"Have not find word that contains exactly {kw['exact']} times the letter '{char}'"
                )
            elif condit == "max-min":
                raise Exception(
                    f"Have not find word that contains between {kw['min']} and {kw['max']} times the letter '{char}'"
                )
            else:
                raise Exception(
                    f"Have not find word that contains {condit}imum {kw[condit]} times the letter '{char}'"
                )


class Most_Rep:
    def __init__(self, Super):
        self.Super = Super
        self.words_li = []

    def Run(self, mostRep):
        count_letter_li = []
        Udieresis = " "
        if mostRep == "a":
            letter = "á"
        elif mostRep == "e":
            letter = "é"
        elif mostRep == "i":
            letter = "í"
        elif mostRep == "o":
            letter = "ó"
        elif mostRep == "u":
            letter = "ú"
            Udieresis = "ü"
        else:
            letter = " "
        for word in wordList:
            count_letter_li.append(
                word.count(mostRep) + word.count(letter) + word.count(Udieresis)
            )
        count_max = sorted(count_letter_li)[-1]
        words_count = wordList.count(count_max)
        for i in range(len(count_letter_li)):
            if count_letter_li[i] == count_max and count_max != 0:
                self.words_li.append(wordList[i])
        try:
            if (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_Word_By"
            ):
                return (choice(self.words_li), count_max)
            elif (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_List_By"
            ):
                return self.words_li
        except:
            error = True
        if error:
            raise Exception(f"Have not find word that contains the letter '{mostRep}'")


# instances of class Find_Word_By and Find_List_By
class Letter:
    def __init__(self, Super):
        self.First = lambda: First(Super)
        self.Last = lambda: Last(Super)
        self.These = lambda: These(Super)
        self.Times = lambda: Times(Super)
        self.Most_Rep = lambda: Most_Rep(Super)


class Substring:
    def __init__(self, Super):
        self.Super = Super
        self.words_li = []

    def Run(self, substr):
        error = None
        for word in wordList:
            if substr in word:
                self.words_li.append(word)
        try:
            if (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_Word_By"
            ):
                return choice(self.words_li)
            elif (
                str(self.Super.__class__)[
                    str(self.Super.__class__).rindex(".") + 1 : -2
                ]
                == "Find_List_By"
            ):
                return self.words_li
        except:
            error = True
        if error:
            raise Exception(
                f"Have not find word that contains the next substring '{substr}'"
            )


class Len:
    def __init__(self, Super):
        self.Super = Super
        self.words_li = []

    def Run(self, **kw):
        error = None
        if (
            str(self.Super.__class__)[str(self.Super.__class__).rindex(".") + 1 : -2]
            == "Find_List_By"
        ):
            try:
                while kw["exact"] > 0:
                    self.words_li.append(choice(wordList))
                    kw["exact"] -= 1
                return self.words_li
            except KeyError:
                raise KeyError(
                    f"For {self.Super.__class__}.Len().Run() argument must be 'exact'"
                )
        if (
            str(self.Super.__class__)[str(self.Super.__class__).rindex(".") + 1 : -2]
            == "Find_Word_By"
        ):
            if len(kw) == 1:
                if "exact" in kw:
                    condit = "exact"
                elif "max" in kw:
                    condit = "max"
                elif "min" in kw:
                    condit = "min"
                else:
                    error = "bad_args"
            elif len(kw) == 2:
                if "max" in kw and "min" in kw:
                    condit = "max-min"
                else:
                    error = "bad_args"
            else:
                error = "bad_args"
            if error == "bad_args":
                raise Exception(
                    'Arguments must be "exact" or "min" or "max" or ("min" and "max")'
                )
            if condit == "max-min":
                if kw["max"] < kw["min"]:
                    raise Exception('"min" must be less than "max"')
            for word in wordList:
                if condit == "exact":
                    if len(word) == kw["exact"]:
                        self.words_li.append(word)
                elif condit == "max":
                    if len(word) <= kw["max"]:
                        self.words_li.append(word)
                elif condit == "min":
                    if len(word) >= kw["min"]:
                        self.words_li.append(word)
                elif condit == "max-min":
                    if len(word) >= kw["min"] and len(word) <= kw["max"]:
                        self.words_li.append(word)
            try:
                return choice(self.words_li)
            except:
                Index_error = True
            if Index_error:
                if condit == "exact":
                    raise Exception(
                        f"Have not find word that contains exactly {kw['exact']} letters"
                    )
                elif condit == "max-min":
                    raise Exception(
                        f"Have not find word that contains between {kw['min']} and {kw['max']} letters"
                    )
                else:
                    raise Exception(
                        f"Have not find word that contains {condit}imum {kw[condit]} letters"
                    )


# instances of class Word
class Find_Word_By:
    def __init__(self):
        self.Letter = lambda: Letter(self)
        self.Substring = lambda: Substring(self)
        self.Len = lambda: Len(self)


class Find_List_By:
    def __init__(self):
        self.Letter = lambda: Letter(self)
        self.Substring = lambda: Substring(self)
        self.Len = lambda: Len(self)


class Word:
    def __init__(self):
        self.Find_Word_By = lambda: Find_Word_By()
        self.Find_List_By = lambda: Find_List_By()


class Doc:
    def __init__(self, *WordOrList, **kw):
        if kw:
            self.lang = kw["lang"]
        else:
            self.lang = False
        try:
            self.WordOrList = WordOrList[0]
        except:
            self.WordOrList = False

    def __str__(self):
        if self.WordOrList:
            if not self.lang:
                if self.WordOrList.lower() == "word":
                    word_or_list = ""
                    Find_By = f"Word().Find_{self.WordOrList.capitalize()}_By()"
                elif self.WordOrList.lower() == "list":
                    word_or_list = " list"
                    Find_By = f"Word().Find_{self.WordOrList.capitalize()}_By()"
                else:
                    raise Exception('Argument must be "word" or "list"')
                info = {
                    "word": f"-returns one word{word_or_list}\n",
                    "len": f"-returns one word{word_or_list} with the specificated length on exact\n\
				or with a length greater than min and/or less than max\n",
                    "substring": f"-returns one word{word_or_list} that contains the specificated substring\n",
                    "letter": f"-return one word{word_or_list} depending of the specificated letters\n",
                    "first": f"-return one word{word_or_list} that have like first letter the specificated by char\n",
                    "last": f"-return one word{word_or_list} that have like last letter the specificated by char\n",
                    "these": f"-return one word{word_or_list} that have the specificated letters into str\n",
                    "times": f"-return one word{word_or_list} that have the letter specificated on char\n\
					the times specificated on exact or greater than min and/or less than max\n",
                    "mostRep": f"-return one word{word_or_list} that have most times the letter specificated\n",
                }
            if self.lang == "es":
                if self.WordOrList.lower() == "word":
                    word_or_list = " palabra"
                    Find_By = f"Word().Find_{self.WordOrList.capitalize()}_By()"
                elif self.WordOrList.lower() == "list":
                    word_or_list = " lista de palabras"
                    Find_By = f"Word().Find_{self.WordOrList.capitalize()}_By()"
                else:
                    raise Exception('Argument must be "word" or "list"')
                info = {
                    "word": f"-devuelve una{word_or_list}\n",
                    "len": f"-devuelve una{word_or_list} con la longitud especificada en exact\n\
			o con una longitud mayor que min y/o menor que max\n",
                    "substring": f"-deveuelve una{word_or_list} que contenga la cadena especificada\n",
                    "letter": f"-devuelve una{word_or_list} que depende de una o más letras especificadas\n",
                    "first": f"-devuelve una{word_or_list} que tenga como primera letra la especificada por char\n",
                    "last": f"-devuelve una{word_or_list} que tenga como última letra la especificada por char\n",
                    "these": f"-devuelve una{word_or_list} que tenga las letras especificadas por str\n",
                    "times": f"-devuelve una{word_or_list} que tenga la letra especificada por char\n\
				la cantidad de veces especificadas por exact o una mayor que min y/o menor que max\n",
                    "mostRep": f"-devuelve una{word_or_list} que tenga mayor cantidad de veces la letra especificada\n",
                }
            Doc = f"\n\n\
	Word():\n\
	    {Find_By}:\n\
		{info['word']}\n\
			{Find_By}.Len().Run(exact=,[min=,max=])\n\
			{info['len']}\n\
			{Find_By}.Substring().Run(substr)\n\
			{info['substring']}\n\
			{Find_By}.Letter()\n\
			{info['letter']}\n\
				{Find_By}.Letter().First().Run(char)\n\
				{info['first']}\n\
				{Find_By}.Letter().Last().Run(char)\n\
				{info['last']}\n\
				{Find_By}.Letter().These().Run(str)\n\
				{info['these']}\n\
				{Find_By}.Letter().Times().Run(char,exact=,[min=,max=])\n\
				{info['times']}\n\
				{Find_By}.Letter().Most_Rep().Run(char)\n\
				{info['mostRep']}\n"
        else:
            if not self.lang:
                Doc = 'This Library get random words or random word list. Pass "word" or "list" like argument to obtain the respect documentation. lang="es" for Doc in Spanish.'
            if self.lang:
                Doc = 'Esta libreria proporciona palabras o listas de palabras aleatorias. Pase "word" o "list" como argumento para obtener la respectiva documentacion. lang="es" para obtener la documentacion en español'
        return Doc
