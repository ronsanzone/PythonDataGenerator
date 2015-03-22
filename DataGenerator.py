from DataGeneratorEntities import Entities


def create_entity_insert_statements(entity_name, num_statements):
    data = [Entities.EntityFactory.factory(entity_name) for i in range(num_statements)]
    with open('C:\Temp\DataScripts\\' + entity_name + '.sql', mode='wt', encoding='utf-8') as file:
        for entity in data:
            file.write(entity.generate_insert())
            file.write('\n')

create_entity_insert_statements("ProviderDirectory", 1000)