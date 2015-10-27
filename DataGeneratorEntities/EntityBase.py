from faker import Factory


class Entity(dict):
    """
    General Entity class using random and Faker to generate data.
    Use http://fake-factory.readthedocs.org/en/master/locales/en_US.html for faker providers
    """
    def __init__(self, **kwargs):
        super(**kwargs).__init__(**kwargs)
        self.tableName = ""
        self.fake = Factory.create()

    def quoted_str(self, value):
        str_value = str(value).replace("'", "")
        return "'" + str_value + "'"

    def generate_insert(self):
        return \
            "INSERT " + self.tableName + " (" + ", ".join(self.keys()) + ") VALUES (" + ", ".join(self.values()) + ")"
