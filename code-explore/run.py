import pickle
import sys
import timeit
from util.BiDirectionalMap import BiDirectionalMap

def simple_compress_with_pickle(file):
    with open(file, "r") as read_file:
        text = read_file.readlines()

    with open(file + ".compress_pickle", "wb") as pickle_output:
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

# method returns two output:
# (1) a BiDirectional map with the values of the word
# (2) the compressed form of the word
def compress_bimap(file):
    bi_map = BiDirectionalMap()
    output = []
    with open(file, "r") as f:
        text = f.readlines()
        for line in text:
            for word in line:
                bi_map.put(word)    
        
        for line in text:
            curr_line = ""
            for word in line:
                curr_line += str(bi_map.get_value(word)) + " "
            output.append(curr_line)
    
    # print(output)
    with open(file+".compress_bimap", "wb") as f:
        pickle.dump(output, f)
    with open (file +".bimap", "wb") as f:
        pickle.dump(bi_map, f)
    

def decompress_bimap(encoded_file, bi_map_file):

    bi_map = None
    encoded_text = None
    with open(bi_map_file, "rb") as f:
        bi_map = pickle.load(f)
    
    with open(encoded_file, "rb") as f:
        encoded_text = pickle.load(f).readlines()
        print(encoded_text)



### Utility methods
def time_method(lambda_expression, num_times=5):
    time = timeit.timeit(lambda_expression, number=num_times) 
    print(f"Compression took {time} seconds")



file = "text-file-full-size"

# time_method(lambda: simple_compress_with_pickle(file))

print("ENCODING USING BIMAP")
time_method(lambda: compress_bimap(file), num_times=1)

# bi_map_file = ""
# encoded_bimap_file = ""
# print("DECODING USING BIMAP")
# time_method(lambda: decompres_bimpa(encoded_bimap_file, bi_map_file))