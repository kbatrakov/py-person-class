class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        if self.name not in Person.people:
            Person.people.update({
                self.name: self
            })
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    instances = []
    for person in people:
        instance = Person(person["name"], person["age"])
        if "wife" in person and person["wife"] is not None:
            instance.wife = person["wife"]
        if "husband" in person and person["husband"] is not None:
            instance.husband = person["husband"]
        instances.append(instance)

    for instance in instances:
        for partner in instances:
            if partner.wife:
                if instance.name == partner.wife:
                    partner.wife = instance
            if partner.husband:
                if instance.name == partner.husband:
                    partner.husband = instance
    return instances
