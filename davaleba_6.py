class Heart:
    def __init__(self):
        self.state = "high blood pressure" if self.is_high_blood_pressure() else "feeling good"

    def is_high_blood_pressure(self):
        cardiac_output = 75
        return cardiac_output > 70


class Brain:
    def __init__(self):
        self.state = "tired" if self.is_tired() else "rested"

    def is_tired(self):
        load = 95
        return load > 90


class Person:
    def __init__(self):
        self.heart = Heart()
        self.brain = Brain()


class Leg:
    def __init__(self, person):
        self.person = person

    def run(self):
        print("The person's heart state is:", self.person.heart.state)
        print("The person's brain state is:", self.person.brain.state)
        print("The person is running with their legs")

person = Person()
leg = Leg(person)
leg.run()
