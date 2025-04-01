'''
Name: Elizabeth Richardson

How to run: python3 <filename> <input filename>
            ex: python3 truckStats.py input.json

Approach: Use a dictionary to map each year to the number of trucks
          that existed in that year, sort the year keys to find 
          desired output

Limitations: The range is only from 1800-2000, but if the range was
             very large this program would not be efficient

Testing Approach: use various start and end years in the input file

Edge Cases: start and end year are the same, some end years are smaller
            than some start years, some years occurring multiple times, 
            some years not occurring at all

Big-O runtime: O(n)

Big-O memory: O(n) - size of the input

More Time?: If I had more time I would include more error checking like
            making sure all of the input is valid, the command line args
            are valid, the file opens correctly. I would also write the
            program in a way that could efficiently handle very large
            time ranges
'''
import sys
import json


def load_json_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)
    

def build_year_map(truck_data, year_map):
    for truck in truck_data:
        for year in range(truck["start"], truck["end"]+1):
            if year in year_map.keys():
                year_map[year] += 1
            else:
                year_map[year] = 1


def get_most(desc_years, length):
    return desc_years[length-1]


def get_topK(desc_years, length, top_k_list, top_k_value):
    for i in range(top_k_value):
        top_k_list.append(desc_years[length-(1+i)])


def get_least(asc_years):
    return asc_years[0]


def get_leastK(asc_years, least_k_list, least_k_value):
    for i in range(least_k_value):
        least_k_list.append(asc_years[i])


def print_output(most, least, top_k_list, least_k_list, top_k_value, least_k_value):
    print(f"Most: {most}")
    print(f"Least: {least}")
    print(f"Top-{top_k_value}: {top_k_list}")
    print(f"Least-{least_k_value}: {least_k_list}")


def main(arg1, arg2):
    truck_stats = load_json_file(arg2)
    
    truck_data = truck_stats["data"]
    year_map = {}
    build_year_map(truck_data, year_map)

    # sort by ascending values, descending years
    sorted_list = sorted(year_map.items(), key=lambda desc: (desc[1], -desc[0]))
    length = len(sorted_list)
    
    most = get_most(sorted_list, length)
    
    top_k_value = truck_stats["topK"]
    top_k_list = []
    get_topK(sorted_list, length, top_k_list, top_k_value)

    # sort by ascending values, ascending years
    sorted_list = sorted(year_map.items(), key=lambda asc: (asc[1], asc[0]))
    least = get_least(sorted_list)
    
    least_k_value = truck_stats["leastK"]
    least_k_list = []
    get_leastK(sorted_list, least_k_list, least_k_value)

    print_output(most, least, top_k_list, least_k_list, top_k_value, least_k_value)


if __name__ == "__main__":
    if (len(sys.argv) >= 1):
        main(sys.argv[0], sys.argv[1])
    else:
        print("Please include input json file as an argument")  
    
