from EntityBase import Entity
import random


class ProviderDirectoryEntity(Entity):
    def __init__(self, **kwargs):
        super(**kwargs).__init__(**kwargs)
        self.tableName = "ProviderDirectory"
        self["Column1"] = self.quoted_str(self.fake.name())
        self["Column2"] = str(random.randrange(1, 10))
        self["Column3"] = self.quoted_str(self.fake.zipcode_plus4())
        self["Column4"] = self.quoted_str(self.fake.longitude())
        self["Column5"] = self.quoted_str(self.fake.ean(length=13))
        self["Column6"] = self.quoted_str(self.fake.company())
        self["Column7"] = self.quoted_str(self.fake.date_time_this_decade())



