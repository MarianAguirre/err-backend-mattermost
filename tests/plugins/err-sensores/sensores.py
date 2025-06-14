from backendSping import get
from errbot import BotPlugin, botcmd


class Sensores(BotPlugin):
    """
    Plugin con los comandos de los sensores
    """
    
    @botcmd
    def stats(self, msg, args):
        """
        Mustra las estadisticas como
        el total, condensacion
        y temperatura
        """
        return get.stats()
    
    @botcmd
    def all(self, msg, args):
        """
        Mustra las estadisticas como
        el total, condensacion
        y temperatura
        """
        return get.all()

    @botcmd
    def nodo(self, msg, args):
        """
        Muestra las estadísticas del nodo. Uso: !nodo <id>
        """
        if not args:
            return "Por favor, proporciona un ID de nodo. Ej: !nodo 123"
        try:
            id_nodo = args
        except ValueError:
            return "El ID debe ser un número entero."

        return get.nodoId(id_nodo)
    
    @botcmd
    def nodosensor(self, msg, args):
        """
        Muestra los datos de un sensor en un nodo específico.
        Uso: !nodosensor <idNodo> <idSensor>
        """
        if not args:
            return "Uso incorrecto. Ejemplo: !nodosensor 123 456"

        parts = args.strip().split()

        if len(parts) != 2:
            return "Debes proporcionar exactamente 2 parámetros: ID del nodo y ID del sensor."

        try:
            id_nodo = parts[0]
            id_sensor = int(parts[1])
        except ValueError:
            return "Ambos parámetros deben ser números enteros."

        return get.nodoSensor(id_nodo, id_sensor)
    
    # @botcmd  
    # def cristo(self, msg, args): 
    #     """
    #     Amen hermanos
    #     """
    #     return "ya jala"  
    # @botcmd  
    # def temperatura(self, msg, args): 
    #     """
    #     Mustra la temperatura
    #     """
    #     return "Ta caliente tu"  
    # @botcmd  
    # def humedad(self, msg, args): 
    #     """
    #     Muestra la humedad
    #     """
    #     return "Ta mojao tu"  
