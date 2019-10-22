# Script which can be run on python repl
# used to demonstrate the mapping of one to many entities.

from onetoone import db
db.drop_all()
db.create_all()
from onetoone import Parent, Child
kathiravan = Parent(name="Kathiravan")
db.session.add(kathiravan)
db.session.commit()
michelle = Parent(name="Michelle")
db.session.add(michelle)
db.session.commit()

jhujhu = Child(name="JhuJhu")
babblu = Child(name='Bablu')
kutty = Child(name='Kutty')
kathiravan.child = jhujhu
kathiravan.child = babblu
kathiravan.child = kutty

spot = Child(name="Spot")
michelle.child = spot
db.session.commit()

# Print the output of the result
print('Print results!!')
print('Expecting result as: Bablu')
print(kathiravan.child.name)

print('Expecting result as: Spot')
print(michelle.child.name)
