import requests
import json


class wanted_interpol:
    def __init__(self):
        self.api = 'https://ws-public.interpol.int/notices/v1/red?ageMax=120&ageMin=18&sexId=F&page=1&resultPerPage=200'
        self.attrs = ['forename', 'date_of_birth', 'entity_id', 'nationalities', 'name', '_links']

    def process_data(self, data):
        processed_data = []
        if 'items' in data:
            items = data['items']
            for item in items:
                processed_item = {}
                for attr in self.attrs:
                    processed_item[attr] = item.get(attr)
                processed_data.append(processed_item)
        return processed_data

    def import_data(self):
        response = requests.get(self.api)
        if response.status_code == 200:
            data = json.loads(response.content)
            processed_data = self.process_data(data)

            # Salvar os dados JSON em um arquivo
            with open('dados-interpol.json', 'w') as json_file:
                json.dump(processed_data, json_file, indent=4)

            print("Dados importados com sucesso para o arquivo 'dados-interpol.json'.")
        else:
            print("Falha na requisição.")


wanted = wanted_interpol()
wanted.import_data()
