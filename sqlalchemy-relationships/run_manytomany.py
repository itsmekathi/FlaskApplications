from manytomany import db, User, Channel
db.drop_all()
db.create_all()

kathiravan = User(name='Kathiravan B')
ramesh = User(name='Ramesh N')

suntv = Channel(channel_name='Sun TV')
ktv = Channel(channel_name='KTV')

kathiravan.channels = [suntv, ktv]
ktv.subscribers.append(ramesh)

db.session.add(kathiravan)
db.session.add(ramesh)
db.session.commit()


# Print the output of the result
print('Print results!!')
print('Channels for which kathiravan has subscribed')
print('Expecting Sun TV and KTV')
kathiravan = User.query.filter_by(name='Kathiravan B').first()
for channel in kathiravan.channels:
    print(channel.channel_name)

print('Users subscribed for channel KTV')
print('Expecting Kathiravan B and Ramesh N')
ktv = Channel.query.filter_by(channel_name='KTV').first()
for subscriber in ktv.subscribers:
    print(subscriber.name)
