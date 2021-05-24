import json


class Quartier:
    def __init__(self, _id, label):
        self.id = _id
        self.label = label

    def __repr__(self):
        return f"Quartier({self.id};{self.label}"

    def fileString(self):
        return f"{self.id}:{self.label}"


class Arrondissement:
    def __init__(self, _id, label):
        self.id = _id
        self.label = label
        self.quartiers = []

    def add_quartier(self, quartier):
        self.quartiers.append(quartier)

    def __repr__(self):
        return f"Arrond({self.id};{self.label}"


class Commune:
    def __init__(self, _id, label):
        self.id = _id
        self.label = label
        self.arronds = []

    def add_arrond(self, commune):
        self.arronds.append(commune)

    def __repr__(self):
        return f"Com({self.id};{self.label}"


class Departement:
    def __init__(self, _id, label):
        self.id = _id
        self.label = label
        self.communes = []

    def add_commune(self, commune):
        self.communes.append(commune)

    def __repr__(self):
        return f"Dep({self.id};{self.label}"


class District:
    def __init__(self, _id, label):
        self.id = _id
        self.name = label
        self.enabled = True

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'enabled': True
        }

    def __repr__(self):
        return f"Dist({self.id};{self.label}"
class City:
    def __init__(self, _id, label):
        self.id = _id
        self.name = label
        self.districts = []

    def add_district(self, district: District):
        self.districts.append(district)

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'enabled': True,
            'districts': [d.toJSON() for d in self.districts]
        }

    def __repr__(self):
        return f"Com({self.id};{self.label}"

departements = []
quartiers = []
cities = []
with open('benin.json') as f:
    data = json.load(f)
    for _departement in data:
        departement = Departement(
            _departement["id_dep"], _departement["lib_dep"])
        for _commune in _departement["communes"]:
            commune = Commune(_commune["id_com"], _commune["lib_com"])
            city = City(_commune["id_com"], _commune["lib_com"])
            for _arrond in _commune["arrondissements"]:
                arrondissement = Arrondissement(
                    _arrond['id_arrond'], _arrond['lib_arrond'])
                for _quartier in _arrond["quartiers"]:
                    quartier = Quartier(
                        _quartier['id_quart'], _quartier['lib_quart'])
                    district = District(
                        _quartier['id_quart'], _quartier['lib_quart'])
                    city.add_district(district)
                    arrondissement.add_quartier(quartier)
                    if commune.id == 48:
                        quartiers.append(quartier)
                commune.add_arrond(arrondissement)
            departement.add_commune(commune)
            cities.append(city.toJSON())
        departements.append(departement)

with open('cities.json', 'w') as f:
    json.dump(cities, f)
