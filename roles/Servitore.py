from .Role import Role
from .SignoreDelCaos import SignoreDelCaos
import strings as s

class Servitore(Role):
    """The Chaos minion is the Chaos Lord's underling.The Chaos minion is the Chaos Lord's underling.
If there are no Chaos Lords in the game, he becomes the Chaos Lord.If there are no Chaos Lords in the game, he becomes the Chaos Lord."""
    team = 'Chaos'
    name = s.chaos_servant_name
    powerdesc = s.Chaos_Servant_power_description

    def __repr__(self) -> str:
        return "<Role: Servant of Chaos>"

    def onendday(self):
        for chaoslord in self.player.game.playersinrole["SignoreDelCaos"]:
            if chaoslord.alive:
                break
        else:
            self.player.game.changerole(self.player, SignoreDelCaos)
            self.player.game.message(s.chaos_servant_inherited)
