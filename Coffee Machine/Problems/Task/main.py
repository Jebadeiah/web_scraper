class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, other):
        descrip = f"{self.description}\n{other.description}"
        tm = f"{self.team}, {other.team}"
        return Task(descrip, tm)
