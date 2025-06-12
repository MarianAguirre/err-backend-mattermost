from errbot import BotPlugin, botcmd


class Sensores(BotPlugin):
    """
    Plugin con los comandos de los sensores
    """
    
    @botcmd  # flags a command
    def cristo(self, msg, args):  # a command callable with !tryme
        """
        Amen hermanos
        """
        return "ya jala"  # This string format is markdown.
    @botcmd  # flags a command
    def temperatura(self, msg, args):  # a command callable with !tryme
        """
        Mustra la temperatura
        """
        return "Ta caliente tu"  # This string format is markdown.
    @botcmd  # flags a command
    def humedad(self, msg, args):  # a command callable with !tryme
        """
        Muestra la humedad
        """
        return "Ta mojao tu"  # This string format is markdown.
