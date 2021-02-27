from app import db


class DbSessionModel:
    def stage(self):
        db.session.add(self)

    def commit(self):
        db.session.commit()

    def save(self):
        self.stage()
        self.commit()
