from application import db
from templates.models import Food


db.create_all()
#
# food1 = Food(name="salatka Lisnera", exp_date="2020-05-16")
# db.session.add(food1)
# db.session.commit()
#
print(Food.query.all())


# db.drop_all()