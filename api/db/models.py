from globals.globals import db


class Snail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(80), index=True, unique=False)
    # TODO: ID_TRAINER FOREIGN KEY

    def __repr__(self):
        return "<Name: {}>".format(self.name)

    def get_snail(self, id):
        snail = self.query.filter_by(id=id).first()
        return snail
