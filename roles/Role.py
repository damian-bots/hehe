# Base di un ruolo
class Role:
    """Base class of a role. All other roles develop from here."""
    icon = "-"  # Icona del ruolo, da visualizzare di fianco al nome
    team = 'None'  # Squadra: 'None', 'Good', 'Evil', 'Chaos'; conta per le condizioni di vittoria
    name = "UNDEFINED"  # Nome del ruolo, viene visualizzato dall'investigatore e durante l'assegnazione
    powerdesc = None  # Ha un potere? Se sì, queste sono le info su come usarlo in seconda persona.

    def __init__(self, player):
        self.player = player

    def __repr__(self) -> str:
        return "<undefined Role>"

    def __str__(self) -> str:
        return "{} {}".format(self.icon, self.name)

    def power(self, arg):
        """The power of the role. It is activated when the bot receives a /power in private chat."""
        pass

    def onendday(self):
        """Method called at the end of each day."""
        pass

    def ondeath(self):
        """Method called upon player death."""
        pass

    def onstartgame(self):
        """Method called at the start of the game."""
        pass
