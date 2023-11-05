from bcis import bcis
from counting_sort import counting_sort
from dataset_generator import DatasetGenerator

def main():
    small_random_list = DatasetGenerator.generate_large_reversed_list()
    arr_bcis = small_random_list.copy()
    arr_cs = small_random_list.copy()
    bcis(arr_bcis)
    # print()
    # counting_sort(arr_cs)

if __name__ == '__main__':
    main()