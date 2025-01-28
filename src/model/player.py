class Player:
    def __init__(self, name, element,position,fp,tp,kick,body,control,guard,speed,stamina,guts):
        self.name = name
        self.element = element
        self.position = position
        self.fp = fp
        self.tp = tp
        self.kick = kick
        self.body = body
        self.control = control
        self.guard = guard
        self.speed = speed
        self.stamina = stamina
        self.guts = guts
        self.team = None

    def set_team(self, team):
        self.team = team.name

    def get_team(self):
        return self.team

    def __str__(self):
        return f'{self.name} - {self.position} - {self.element}'

    def __repr__(self):
        return f'{self.name} - {self.position} - {self.element}'