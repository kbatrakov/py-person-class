class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        if self.name not in Person.people:
            Person.people.update({
                self.name: self
            })


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
        if "wife" in instance.__dict__:
            for partner in instances:
                if instance.__dict__["wife"] == partner.name:
                    instance.__dict__["wife"] = partner
        if "husband" in instance.__dict__:
            for partner in instances:
                if instance.__dict__["husband"] == partner.name:
                    instance.__dict__["husband"] = partner

    return instances
