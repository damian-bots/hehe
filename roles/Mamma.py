from .Role import Role
import strings as s
import random

class Mamma(Role):
    """Mom hears rumors around town and discovers a new role every now and then..."""
    icon = s.mom_icon
    team = 'Good'
    name = s.mom_name
    powerdesc = s.mom_power_description

    def __repr__(self) -> str:
        return "<Role: Mamma>"

    def onstartgame(self):
        # Scegli un bersaglio casuale che non sia il giocatore stesso
        possibletargets = self.player.game.players.copy()
        possibletargets.remove(self.player)
        target = random.sample(possibletargets, 1)[0]
        self.player.message(s.mom_discovery.format(target=target.tusername, icon=target.role.icon, role=target.role.name))

    def onendday(self):
        if random.randrange(0, 10) > 5:
            # Scegli un bersaglio casuale che non sia il giocatore stesso
            possibletargets = self.player.game.players.copy()
            possibletargets.remove(self.player)
            target = random.sample(possibletargets, 1)[0]
            self.player.message(
                s.mom_discovery.format(target=target.tusername, icon=target.role.icon, role=target.role.name))
