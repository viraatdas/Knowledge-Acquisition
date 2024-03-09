import pickle
import sys
import timeit
from 

def simple_compress_with_pickle(file):
    with open(file, "r") as read_file:
        text = read_file.readlines()

    with open(file + ".simple_compress_with_pickle", "wb") as pickle_output:
        pickle.dump(text, pickle_output)        


def size_analysis(file):
    total_number_of_bytes = 0
    num_elements = 0
    with open(file, "r") as f:
        text = f.readlines()
        for el in text:
            total_number_of_bytes += sys.getsizeof(el)
            num_elements+=1
    print(f"Number of lines: {num_elements}")
    print(f"Total: {total_number_of_bytes} bytes")
    print(f"On average each line contains: {total_number_of_bytes/num_elements} bytes")

def compress_build_dictionary_for_words(file):
    word_dict = dict()
    with open(file, "r") as f:
        for line in f.readlines():
            for word in line:
                if word not in word_dict



### Utility methods
def time_method(lambda_expression, num_times=5):
    time = timeit.timeit(lambda: simple_compress_with_pickle(file), number=num_times) 
    print(f"Compression took {time} seconds")

def decode(file):
    pass


file = "text-file-full-size"

# time_method(lambda: simple_compress_with_pickle(file))
compress_build_dictionary_for_words(file)

