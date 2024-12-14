from .Role import Role
from .SignoreDelCaos import SignoreDelCaos
import strings as s

class Servitore(Role):
    """The Chaos minion is the Chaos Lord's underling.The Chaos minion is the Chaos Lord's underling.
If there are no Chaos Lords in the game, he becomes the Chaos Lord.If there are no Chaos Lords in the game, he becomes the Chaos Lord."""
    icon = s.chaos_servant_icon
    team = 'Chaos'
    name = s.chaos_servant_name
    powerdesc = s.chaos_servant_power_description

    def __repr__(self) -> str:
        return "<Role: Servitore del Caos>"

    def onendday(self):
        for chaoslord in self.player.game.playersinrole["SignoreDelCaos"]:
            if chaoslord.alive:
                break
        else:
            self.player.game.changerole(self.player, SignoreDelCaos)
            self.player.game.message(s.chaos_servant_inherited)
