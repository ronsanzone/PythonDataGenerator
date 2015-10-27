from Entities import *


class EntityFactory(object):

    def factory(entity_type):
        if entity_type == "ProviderDirectory":
            return ProviderDirectoryEntity()
        assert 0, "Bad Entity Creation: " + entity_type
    factory = staticmethod(factory)
