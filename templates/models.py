from application import db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    exp_date = db.Column(db.String, nullable=False)
    img_file = db.Column(db.String(20), nullable=False, default='deffood.jpg')

    def __repr__(self):
        return f"Food('{self.name}','{self.exp_date}', '{self.img_file}')"
