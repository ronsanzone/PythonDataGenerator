import random
from faker import Factory


class Entity(dict):
    """
    General Entity class using random and Faker to generate data.
    Use http://fake-factory.readthedocs.org/en/master/locales/en_US.html for faker providers
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tableName = ""
        self.fake = Factory.create()

    def quoted_str(self, value):
        str_value = str(value).replace("'", "")
        return "'" + str_value + "'"

    def generate_insert(self):
        return \
            "INSERT " + self.tableName + " (" + ", ".join(self.keys()) + ") VALUES (" + ", ".join(self.values()) + ")"


class EntityFactory(object):

    def factory(entity_type):
        if entity_type == "ProviderDirectory":
            return ProviderDirectoryEntity()
        assert 0, "Bad Entity Creation: " + entity_type
    factory = staticmethod(factory)


class ProviderDirectoryEntity(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tableName = "ProviderDirectory"
        self["Column1"] = self.quoted_str(self.fake.name())
        self["Column2"] = str(random.randrange(1, 10))
        self["Column3"] = self.quoted_str(self.fake.zipcode_plus4())
        self["Column4"] = self.quoted_str(self.fake.longitude())
        self["Column5"] = self.quoted_str(self.fake.ean(length=13))
        self["Column6"] = self.quoted_str(self.fake.company())
        self["Column7"] = self.quoted_str(self.fake.date_time_this_decade())



