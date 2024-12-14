from .Role import Role
import strings as s
import random

class Investigatore(Role):
    """The investigator can investigate a person's true role once per day."""
    team = 'Good'
    name = s.detective_name
    powerdesc = s.detective_power_descition

    def __init__(self, player):
        super().__init__(player)
        self.power_was_used = False

    def __repr__(self) -> str:
        return "<Role: Investigator>"

    def power(self, arg):
        # Indaga sul vero ruolo di una persona, se sono ancora disponibili usi del potere.
        if self.power_was_used:
            # Non hai abbastanza cariche!
            self.player.message(s.error_no_uses)
            return
        target = self.player.game.findplayerbyusername(arg)
        if target is None:
            # Username non valido
            self.player.message(s.error_username)
            return
        # Utilizza il potere su quella persona
        self.power_was_used = True
        # Tira per investigare
        target_score = random.randrange(0, 25) + 1
        score = random.randrange(0, 100) + 1
        if score > target_score:
            role = target.role
        else:
            role = self.player.game.getrandomrole()
        self.player.message(s.detective_discovery.format(target_score=100-target_score, target=target.tusername, icon=role.icon, role=role.name))

    def onendday(self):
        # Ripristina il potere
        self.power_was_used = False
