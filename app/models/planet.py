from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            color=self.color
        )

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"], description=planet_data["description"], color=planet_data["color"])
        return new_planet