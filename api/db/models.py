from globals.globals import db


class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return "<id: {}>".format(self.id)
    def get_trainer(self, id):
        trainer = self.query.filter_by(id=id).first()
        return trainer

 
class Snail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))

    def __repr__(self):
       return "<id: {}>".format(self.id) 
    def get_snail(self, id):
        snail = self.query.filter_by(id=id).first()
        return snail  

class RaceParticipants(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    id_snail = db.Column(db.Integer(), db.ForeignKey("snail.id"))
    id_race = db.Column(db.Integer(), db.ForeignKey("race.id"))
    
    def __repr__(self):
        return "<id: {}>".format(self.id)
    def get_race_participants(self, id):
        race_participants = self.query.filter_by(id=id_race).first()
        return race_participants

class Race(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    id_round = db.Column(db.Integer(), db.ForeignKey("round.id"))

    def __repr__(self):
        return "<id: {}>".format(self.id)
    def get_race(self, id):
        race = self.query.filter_by(id=id).first()
        return race

class Round(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(12), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return "<id: {}>".format(self.id)
    def get_round(self, id):
        round = self.query.filter_by(id=id).first()
        return round

class RaceResult(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True, autoincrement=True)
    position = db.Column(db.Integer(), nullable=False)
    time_to_finish = db.Column(db.DateTime(), nullable=False)
    did_not_finish = db.Column(db.String(3))
    id_race_participants = db.Column(db.Integer(), db.ForeignKey("raceparticipants.id"))

    def __repr__(self):
        return "<id: {}>".format(self.id)
    def get_race_result(self, id):
        race_result = self.query.filter_by(id=id).first()


