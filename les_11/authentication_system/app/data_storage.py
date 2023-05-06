import os
import json
from copy import deepcopy


class JsonDataStorage:
    initial_data = '[]'

    @property
    def data(self):
        data = deepcopy(self.__data)
        return data

    def __init__(self, path_to_file):
        self.path = path_to_file
        self.__data = self.__get_data_or_create_json_file()

    def update(self, input_data=None):
        if input_data:
            self.__data.append(input_data)

        with open(self.path, 'w') as jf:
            json.dump(self.__data, jf)

    def remove(self, input_data):
        self.__data.remove(input_data)
        self.update()

    def __get_data_or_create_json_file(self):
        if not os.path.isfile(self.path):
            with open(self.path, 'w') as f:
                f.write(self.initial_data)

        with open(self.path, 'r') as f:
            return json.load(f)
