class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        if self.name not in Person.people:
            Person.people.update({
                self.name: self
            })


def create_person_list(people: list) -> list:
    instances = []
    for person in people:
        instance = Person(person["name"], person["age"])
        if "wife" in person:
            instance.wife = person["wife"]
        if "husband" in person:
            instance.husband = person["husband"]
        instances.append(instance)

    for instance in instances:
        if (instance.wife and instance.wife is not None or instance.husband
                and instance.husband is not None):
            for partner in instances:
                if instance.wife == partner.name:
                    instance.wife = partner
                    break
                if instance.husband == partner.name:
                    instance.husband = partner
                    break
        else:
            del instance.wife
            del instance.husband

    return instances
