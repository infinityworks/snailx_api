from globals.globals import db


class Snail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(80), index=True, unique=False)
    # TODO: ID_TRAINER FOREIGN KEY

    def __repr__(self):
        return "<Name: {}>".format(self.name)

    def get_snail(self, id):
        return self.query.filter_by(id=id).first()


class RaceParticipants(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    id_snail = db.Column(db.Integer(), db.ForeignKey("snail.id"), nullable=False)
    id_race = db.Column(db.Integer(), db.ForeignKey("race.id"), nullable=False)
    
    def __repr__(self):
        return "<Race Participants\nid: {}\n snail_id: {}\n race_id: {}>".format(self.id, self.snail_id, self.race_id)

    def get_race_participants(self, id):
        return self.query.filter_by(id=id).first()


class Race(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    id_round = db.Column(db.Integer(), db.ForeignKey("round.id"), nullable=False)

    def __repr__(self):
        return "<Race\nid: {}\n date: {}\n status: {}\n round_id: {}>".format(self.id, self.date, self.status, self.round_id)

    def get_race(self, id):
        return self.query.filter_by(id=id).first()


class Round(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(12), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return "<Round\nid: {}\n name: {}\n start_date: {}>".format(self.id, self.name, self.start_date)


    def get_round(self, id):
        return self.query.filter_by(id=id).first()


class RaceResult(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    position = db.Column(db.Integer(), nullable=False)
    time_to_finish = db.Column(db.DateTime(), nullable=False)
    did_not_finish = db.Column(db.String(3))
    id_race_participants = db.Column(db.Integer(), db.ForeignKey("race_participants.id"), nullable=False)

    def __repr__(self):
        return "<Race Result\nid: {}\n position: {}\n time_to_finish: {}\n did_not_finish: {}\n race_participants_id: {}>".format(self.id, self.position, self.time_to_finish, self.did_not_finish, self.race_participants_id)

    def get_race_result(self, id):
        return self.query.filter_by(id=id).first()
