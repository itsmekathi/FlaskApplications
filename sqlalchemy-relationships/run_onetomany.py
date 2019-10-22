# Script which can be run on python repl
# used to demonstrate the mapping of one to many entities.

from onetomany import db
db.drop_all()
db.create_all()
from onetomany import Person, Pet
kathiravan = Person(name="Kathiravan")
db.session.add(kathiravan)
db.session.commit()
michelle = Person(name="Michelle")
db.session.add(michelle)
db.session.commit()

jhujhu = Pet(name="JhuJhu", owner=kathiravan)
babblu = Pet(name='Bablu', owner=kathiravan)

spot = Pet(name="Spot", owner = michelle)
db.session.commit()

# Print the output of the result
print('Print results!!')
print('Prints pets related to Kathiravan')
print('Expecting JhuJhu and Bablu')
kathiravan = Person.query.filter_by(name='Kathiravan').first()
for pet in kathiravan.pets:
    print(pet.name)

print('Prints pets related to michelle')
print('Expecting result as: Spot')
michelle = Person.query.filter_by(name='Michelle').first()
for pet in michelle.pets:
    print(pet.name)

# Querying from pets
print('Querying for pet: JhuJhu')
jhujhu = Pet.query.filter_by(name='JhuJhu').first()
print(f'Pet Name: {jhujhu.name}, Owner name: {jhujhu.owner.name}')

