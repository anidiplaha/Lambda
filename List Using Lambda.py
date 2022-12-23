animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
lowered_animals = list(map(lambda animal: str.lower(animal), animals))
print(uppered_animals)
print(lowered_animals)
