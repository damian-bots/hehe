from .Role import Role
import strings as s

class Terrorista(Role):
    """The terrorist is a mifioso who can kill in only one way: by getting killed by the Royals.The terrorist is a mifioso who can kill in only one way: by getting killed by the Royals.
If he succeeds, he wins the game and kills everyone who voted for him."""
    icon = s.terrorist_icon
    team = "Evil"
    name = s.terrorist_name
    powerdesc = s.terrorist_power_description

    def __repr__(self) -> str:
        return "<Role: Terrorista>"

    def ondeath(self):
        # Se è stato ucciso da una votazione, attiva il suo potere
        if self.player == self.player.game.lastlynch:
            self.player.game.message(s.terrorist_kaboom)
            for selectedplayer in self.player.game.players:
                # Elimina ogni giocatore che sta votando per sè stesso
                if selectedplayer.votingfor == self.player and selectedplayer.alive and selectedplayer is not self.player:
                    self.player.game.message(s.terrorist_target_killed.format(target=selectedplayer.tusername, icon=selectedplayer.role.icon, role=selectedplayer.role.name))
                    selectedplayer.kill()
