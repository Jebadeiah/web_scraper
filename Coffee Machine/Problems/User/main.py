class User:
    n_active = 0
    users = []

    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name
        self.n_active += 1
        self.users.append(user_name)
