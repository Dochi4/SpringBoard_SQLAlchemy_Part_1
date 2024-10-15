from models import User,db
from app import app


with app.app_context():
    # drop and create table's info
    db.drop_all()
    db.create_all()

    # if table is not empty it then it will empty
    User.query.delete()

    # Test Users 
    whis = User(first_name='Whis',last_name='Dogman')
    vamp = User(first_name='Vamp',last_name='Dogman')
    tiggy = User(first_name='Tiggy',last_name='Tigerson', image_url='https://w0.peakpx.com/wallpaper/1002/951/HD-wallpaper-jujutsu-kaisen-op-strong-anime-gojo-satoru-love.jpg')

    # add test Users
    db.session.add(whis)
    db.session.add(vamp)
    db.session.add(tiggy)

    # commit test User
    db.session.commit()

    print("Database seeded!")