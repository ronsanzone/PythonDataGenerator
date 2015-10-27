import DataGenerator


def main():
    data_generator = DataGenerator('C:\Temp\DataScripts\\')
    data_generator.create_entity_insert_statements("ProviderDirectory", 1000)


if __name__ == '__main__':
    main()
