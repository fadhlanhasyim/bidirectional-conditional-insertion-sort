import random

class DatasetGenerator:
    __SMALL_N = 500
    __MEDIUM_N = 5_000
    __LARGE_N = 50_000

    def write(filename, list_data):
        with open('dataset' + filename, 'w') as file:
            for item in list_data:
                file.write(str(item) + '\n')

    @classmethod
    def __generate_random_list(self, num_items):
        random_list = [random.randint(0, 10_000) for _ in range(num_items)]
        return random_list

    @classmethod
    def __generate_sorted_list(self, num_items):
        random_list = self.__generate_random_list(num_items)
        sorted_list = sorted(random_list)
        return sorted_list

    @classmethod
    def __generate_reversed_list(self, num_items):
        random_list = self.__generate_random_list(num_items)
        reversed_list = sorted(random_list, reverse=True)
        return reversed_list
    
    # RANDOM
    @classmethod
    def generate_small_random_list(self):
        small_random_list = self.__generate_random_list(self.__SMALL_N)
        return small_random_list
    
    @classmethod
    def generate_medium_random_list(self):
        medium_random_list = self.__generate_random_list(self.__MEDIUM_N)
        return medium_random_list
    
    @classmethod
    def generate_large_random_list(self):
        large_random_list = self.__generate_random_list(self.__LARGE_N)
        return large_random_list
    
    #  SORTED
    @classmethod
    def generate_small_sorted_list(self):
        small_sorted_list = self.__generate_sorted_list(self.__SMALL_N)
        return small_sorted_list
    
    @classmethod
    def generate_medium_sorted_list(self):
        medium_sorted_list = self.__generate_sorted_list(self.__MEDIUM_N)
        return medium_sorted_list
    
    @classmethod
    def generate_large_sorted_list(self):
        large_sorted_list = self.__generate_sorted_list(self.__LARGE_N)
        return large_sorted_list
    
    # REVERSED LIST
    @classmethod
    def generate_small_reversed_list(self):
        small_reversed_list = self.__generate_reversed_list(self.__SMALL_N)
        return small_reversed_list
    
    @classmethod
    def generate_medium_reversed_list(self):
        medium_reversed_list = self.__generate_reversed_list(self.__MEDIUM_N)
        return medium_reversed_list
    
    @classmethod
    def generate_large_reversed_list(self):
        large_reversed_list = self.__generate_reversed_list(self.__LARGE_N)
        return large_reversed_list
