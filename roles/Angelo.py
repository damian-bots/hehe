from .Role import Role
import strings as s

class Angelo(Role):
    """The angel can protect one person per day from Mifia.The angel can protect one person per day from Mifia.
If he succeeds in protecting, his role will be revealed to everyone.If he succeeds in protecting, his role will be revealed to everyone."""
    icon = s.angel_icon
    team = 'Good'
    name = s.angel_name
    powerdesc = s.angel_power_description

    def __init__(self, player):
        super().__init__(player)
        self.protecting = None  # La persona che questo angelo sta proteggendo

    def __repr__(self) -> str:
        if self.protecting is None:
            return "<Role: Angel>"
        else:
            return "<Role: Angel, protecting {target}>".format(target=self.protecting.tusername)

    def power(self, arg):
        # Imposta qualcuno come protetto
        selected = self.player.game.findplayerbyusername(arg)
        if selected is None:
            self.player.message(s.error_username)
            return

        # Controlla che l'angelo stia provando a proteggere sè stesso
        if selected is not self.player:
            # Togli la protezione a quello che stavi proteggendo prima
            if self.protecting is not None:
                self.protecting.protectedby = None
            # Aggiungi la protezione al nuovo giocatore selezionato
            selected.protectedby = self.player
            self.protecting = selected
            self.player.message(s.angel_target_selected.format(target=self.protecting.tusername))
        else:
            self.player.message(s.error_no_selfpower)

    def onendday(self):
        # Resetta la protezione
        if self.protecting is not None:
            self.protecting.protectedby = None
        self.protecting = None

    def ondeath(self):
        # Resetta la protezione
        if self.protecting is not None:
            self.protecting.protectedby = None
        self.protecting = None
