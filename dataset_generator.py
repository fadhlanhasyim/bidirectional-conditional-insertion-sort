import random

class DatasetGenerator:
    __SMALL_N = 500
    __MEDIUM_N = 5_000
    __LARGE_N = 50_000

    @classmethod
    def write_file(self, filename, list_data):
        with open('dataset/' + filename, 'w') as file:
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
        self.write_file('small_random.txt', small_random_list)
        return small_random_list
    
    @classmethod
    def generate_medium_random_list(self):
        medium_random_list = self.__generate_random_list(self.__MEDIUM_N)
        self.write_file('medium_random.txt', medium_random_list)
        return medium_random_list
    
    @classmethod
    def generate_large_random_list(self):
        large_random_list = self.__generate_random_list(self.__LARGE_N)
        self.write_file('large_random.txt', large_random_list)
        return large_random_list
    
    #  SORTED
    @classmethod
    def generate_small_sorted_list(self):
        small_sorted_list = self.__generate_sorted_list(self.__SMALL_N)
        self.write_file('small_sorted.txt', small_sorted_list)
        return small_sorted_list
    
    @classmethod
    def generate_medium_sorted_list(self):
        medium_sorted_list = self.__generate_sorted_list(self.__MEDIUM_N)
        self.write_file('medium_sorted.txt', medium_sorted_list)
        return medium_sorted_list
    
    @classmethod
    def generate_large_sorted_list(self):
        large_sorted_list = self.__generate_sorted_list(self.__LARGE_N)
        self.write_file('large_sorted.txt', large_sorted_list)
        return large_sorted_list
    
    # REVERSED LIST
    @classmethod
    def generate_small_reversed_list(self):
        small_reversed_list = self.__generate_reversed_list(self.__SMALL_N)
        self.write_file('small_reversed.txt', small_reversed_list)
        return small_reversed_list
    
    @classmethod
    def generate_medium_reversed_list(self):
        medium_reversed_list = self.__generate_reversed_list(self.__MEDIUM_N)
        self.write_file('medium_reversed.txt', medium_reversed_list)
        return medium_reversed_list
    
    @classmethod
    def generate_large_reversed_list(self):
        large_reversed_list = self.__generate_reversed_list(self.__LARGE_N)
        self.write_file('large_reversed.txt', large_reversed_list)
        return large_reversed_list
