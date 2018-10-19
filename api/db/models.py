from globals.globals import db


class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return "<Trainer\nid: {}\n name: {}>".format(self.id, self.name)

    def get_trainer(self, id):
        return self.query.filter_by(id=id).first()


class Snail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))

    def __repr__(self):
        return "<Snail\nid: {}\n name: {}\n trainer_id: {}>".format(self.id, self.name, self.trainer_id)

    def get_snail(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_snails(self):
        return self.query.all()


class RaceParticipants(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    id_snail = db.Column(db.Integer(), db.ForeignKey("snail.id"))
    id_race = db.Column(db.Integer(), db.ForeignKey("race.id"))

    def __repr__(self):
        return "<Race Participants\nid: {}\n snail_id: {}\n race_id: {}>".format(self.id, self.id_snail, self.id_race)

    def get_race_participant(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_race_participants(self):
        return self.query.all()

    def get_race_participants_race_id(self, id_race):
        return self.query.filter_by(id_race=id_race).all()

    def get_race_results(self):
        return db.session.query(RaceParticipants, RaceResult).join(
            RaceResult,
            RaceParticipants.id == RaceResult.id_race_participants
        ).join(
            Race,
            Race.id == RaceParticipants.id_race
        ).all()


class Race(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    id_round = db.Column(db.Integer(), db.ForeignKey("round.id"))

    def __repr__(self):
        return "<Race\nid: {}\n date: {}\n status: {}\n round_id: {}>".format(self.id, self.date, self.status,
                                                                              self.id_round)

    def get_race(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_races(self):
        return self.query.all()

    def get_round_race_ids(self, id_round):
        return db.session.query(Race.id).filter_by(id_round=id_round).all()


class Round(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(12), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return "<Round\nid: {}\n name: {}\n start_date: {}>".format(self.id, self.name, self.start_date)

    def get_round(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_rounds(self):
        return self.query.all()


class RaceResult(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    position = db.Column(db.Integer(), nullable=False)

    time_to_finish = db.Column(db.Integer(), nullable=False)
    did_not_finish = db.Column(db.Boolean(), nullable=False)
    id_race_participants = db.Column(
        db.Integer(), db.ForeignKey("race_participants.id"))

    def __repr__(self):
        return "<Race Result\nid: {}\n position: {}\n time_to_finish: {}\n did_not_finish: {}\n race_participants_id: {}>".format(
            self.id, self.position, self.time_to_finish, self.did_not_finish, self.id_race_participants)

    def get_race_result(self, id):
        return self.query.order_by(RaceResult.position).filter_by(id_race_participants=id).first()

    def get_all_race_results(self):
        return self.query.all()


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return "<User\nid: {}\n username: {}\n email: {}\n password: {}>".format(
            self.id, self.username, self.email, self.password)

    def get_user(self, id):
        return self.query.filter_by(id=id).first()

    def get_users(self):
        return self.query.all()

    def get_user_by_username(self, username):
        return self.query.filter_by(username=username).first()

    def get_user_by_email(self, email):
        return self.query.filter_by(email=email).first()
