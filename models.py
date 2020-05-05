from application import db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    exp_date = db.Column(db.DateTime, nullable=False)
    picture = db.Column(db.String(20), nullable=False, default='deffood.jpg')

    def __repr__(self):
        return f"Food('{self.name}','{self.exp_date}', '{self.picture}')"

    def calculate_days_left(self, today):
        days_left = self.exp_date.date() - today
        return days_left.days


class BarFood(db.Model):
    barcode = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    image_code = db.Column(db.String(20), nullable=False, default='deffood.jpg')

    def __repr__(self):
        return f"BarFood('{self.barcode}','{self.name}','{self.image_code}')"


class NewFood(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    barcode = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    food_picture = db.Column(db.String(20), nullable=False, default='deffood.jpg')
    exp_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"NewFood('{self.barcode}','{self.name}','{self.food_picture}','{self.exp_date}')"
