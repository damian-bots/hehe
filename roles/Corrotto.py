from .Role import Role
import strings as s

class Corrotto(Role):
    """The Corrupt One is an investigator who works for the Mifia."""
    team = 'Evil'
    name = s.corrupt_name
    powerdesc = s.Corrupt_power_description
    refillpoweruses = 1

    def __init__(self, player):
        super().__init__(player)
        self.poweruses = self.refillpoweruses

    def __repr__(self) -> str:
        return "<Role: Corrupt, {uses} uses left>".format(uses=self.poweruses)

    def power(self, arg):
        # Indaga sul vero ruolo di una persona, se sono ancora disponibili usi del potere.
        if self.poweruses <= 0:
            # Non hai abbastanza cariche!
            self.player.message(s.error_no_uses)
            return
        target = self.player.game.findplayerbyusername(arg)
        if target is None:
            # Username non valido
            self.player.message(s.error_username)
            return
        # Utilizza il potere su quella persona
        self.poweruses -= 1
        self.player.message(s.detective_discovery.format(target_score=100, target=target.tusername, icon=target.role.icon, role=target.role.name))

    def onendday(self):
        # Ripristina il potere
        self.poweruses = self.refillpoweruses
