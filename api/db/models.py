from globals.globals import db


class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False)
    #snail = db.relationship('Snail', backref='trainer', lazy=True)

    def __repr__(self):
        return "<id: {}>".format(self.id)
    def get_trainer(self, id):
        trainer = self.query.filter_by(id=id).first()
        return trainer

 
class Snail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))
    #trainer_name = db.relationship("Trainer", foreign_keys=[trainer_id])

    def __repr__(self):
       return "<id: {}>".format(self.id) 
    def get_snail(self, id):
        snail = self.query.filter_by(id=id).first()
        return snail  

"""class RaceParticipants(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    id_Snail = db.Column(db.Integer(), nullable=False, ForeignKey("snail.id"))

    def __repr__(self):
        return "<Title: {}>".format(self.title)

class Race(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    Date = db.Column(db.DateTime(), nullable=False)
    Status = db.Column(db.String(), nullable=False)
    id_Round = db.Column(db.Integer(), nullable=False)
    id_RaceParticipants = db.Column(db.Integer(), nullable=False, ForeignKey("RaceParticipants.id"))

    def __repr__(self):
        return "<Title: {}>".format(self.title)

class Round(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(12), nullable=False)
    NumRaces = db.Column(db.Integer(), nullable=False)
    StartDate = db.Column(db.DateTime(), nullable=False)
    EndDate = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

class RaceResult(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    id_Race = db.Column(db.Integer(), nullable=False, ForeignKey("Race.id"))
    id_FirstPace = db.Column(db.Integer(), nullable=False, ForeignKey("Snail.id"))
    id_SecondPlace = db.Column(db.Integer(), nullable=False, ForeignKey("Snail.id"))
    id_ThirdPlace = db.Column(db.Integer(), nullable=False, ForeignKey("Snail.id"))

    def __repr__(self):
        return "<Title: {}>".format(self.title)

class TrainersSnails(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    id_Snail = db.Column(db.Integer(), nullable=False, ForeignKey("Snail.id")) 

    def __repr__(self):
        return "<Title: {}>".format(self.title)"""

