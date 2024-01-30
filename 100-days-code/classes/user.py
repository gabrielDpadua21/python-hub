class User:

    name: str
    email: str
    age: int

    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age



user = User("Frajola", "fraj@gmail.com", 12)


print(user.name)
print(user.email)
print(type(user.age))
