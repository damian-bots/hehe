from .Role import Role
import strings as s

class SignoreDelCaos(Role):
    """The Lord of Chaos is a Derek in the last seconds before death.The Lord of Chaos is a Derek in the last seconds before death.
He can change other people's lives... Even if he can't decide what."""
    team = 'Chaos'
    name = s.Chaos_lord_name
    powerdesc = s.chaos_lord_power_descition

    def __init__(self, player):
        super().__init__(player)
        self.target = None

    def __repr__(self) -> str:
        return "<Role: Lord of Chaos>"

    def power(self, arg):
        selected = self.player.game.findplayerbyusername(arg)
        if selected is not None and selected is not self.player and selected.alive:
            self.target = selected
            self.player.message(s.chaos_lord_target_selected.format(target=self.target.tusername))
        else:
            self.player.message(s.error_no_username)

    def onendday(self):
        if self.target is not None:
            if self.target.alive and self.player.alive:
                if not isinstance(self.target.role, SignoreDelCaos):
                    randomrole = self.player.game.getrandomrole()
                    self.player.game.changerole(self.target, randomrole)
                    self.player.game.message(s.chaos_lord_randomized)
                else:
                    self.player.game.message(s.chaos_lord_failed)
