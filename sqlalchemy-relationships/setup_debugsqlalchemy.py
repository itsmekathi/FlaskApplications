from debugsqlalchemy import db
from models import Person, Pet
db.drop_all()
db.create_all()
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