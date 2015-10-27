from DataGeneratorEntities import Entities

class DataGenerator(object):

    def __init__(self, output_dir):
        self.output_dir = output_dir

    def create_entity_insert_statements(self, entity_name, num_statements):
        data = [Entities.EntityFactory.factory(entity_name) for i in range(num_statements)]
        with open(self.output_dir + entity_name + '.sql', mode='wt', encoding='utf-8') as file:
            for entity in data:
                file.write(entity.generate_insert())
                file.write('\n')
