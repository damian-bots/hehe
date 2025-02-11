from .Role import Role
import strings as s

class Royal(Role):
    """A member of the Royal Games. The main role, has no power other than to vote."""
    team = 'Good'
    name = s.Royal_Name

    def __init__(self, player):
        super().__init__(player)

    def __repr__(self) -> str:
        return "<Role: Royal>"
