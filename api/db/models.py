from globals.globals import db


class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False)


    def __repr__(self):
        return "<id: {}> \n <name: {}>".format(self.id, self.name)
    def get_trainer(self, id):
        trainer = self.query.filter_by(id=id).first()
        return trainer

 
class Snail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))


    def __repr__(self):
       return "<id: {}> \n <name: {}> \n <trainer_id: {}>".format(self.id, self.name, self.trainer_id)
    def get_snail(self, id):
        snail = self.query.filter_by(id=id).first()
        return snail  

