from application import db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    exp_date = db.Column(db.DateTime, nullable=False)
    picture = db.Column(db.String(20), nullable=False, default='deffood.jpg')

    def __repr__(self):
        return f"Food('{self.name}','{self.exp_date}', '{self.picture}')"

    def calculate_days_left(self, today):
        days_left = today - self.exp_date
        return days_left
