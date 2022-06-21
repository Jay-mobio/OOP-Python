class Shark:

    animal_type = "fish"
    location = "ocean"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")


def main():
    sammy = Shark("Sammy", 5)

    print(sammy.name)

    print(sammy.location)

    stevie = Shark("Stevie", 8)

    print(stevie.name)

    stevie.set_followers(77)

    print(stevie.animal_type)

if __name__ == "__main__":
    main()