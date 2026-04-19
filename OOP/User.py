class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def show_info(self):
        return f"Username: {self.username}, Email: {self.email}"


class Admin(User):
    def __init__(self, username, email, level):
        super().__init__(username, email)
        self.level = level

    def ban_user(self, target_user):
        if self.level < 3:
            return "Not enough privileges"
        else:
            return f"{self.username}-მა დაბლოკა მომხმარებელი {target_user}"

admin1 = Admin("LukichaX", "luka@mail.com", 3)
print(admin1.show_info())
print(admin1.ban_user("iura"))


