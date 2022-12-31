class Automatas:
    def __init__(self, nombre, alfabeto,simbolosPila,estados,estadoInicial,estadosAceptacion,transiciones):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.simbolosPila = simbolosPila
        self.estados = estados
        self.estadoInicial = estadoInicial
        self.estadosAceptacion = estadosAceptacion
        self.transiciones = transiciones 

    

class Transiciones:
    def __init__(self,estadoOrigen,simboloEntrada,simboloextraPila,estadoDestino,simboloinsertaPila):
        self.estadoOrigen = estadoOrigen
        self.simboloEntrada = simboloEntrada
        self.simboloextraPila = simboloextraPila
        self.estadoDestino = estadoDestino
        self.simboloinsertaPila = simboloinsertaPila