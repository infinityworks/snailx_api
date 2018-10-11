import sys
sys.path.insert(0, '/vagrant/repos/snailx_api/api')
from db.models import Trainer


def generate_data():
    trainer = Trainer()
    # snail = Snail()
    # race_participants = RaceParticipants()
    # race = Race()
    # round = Round()
    # race_result = RaceResult()

    trainer_names = ["Mike", "Junaid", "Sandeep", "Malik", "Matt"]

    for x, name in trainer_names:
        trainer.add_trainer(x + 1, name)


if __name__ == '__main__':
    generate_data()


