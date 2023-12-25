import sqlite3
import time
import random
from sortedcontainers import SortedDict
from sqllite1 import fake_data

conn = sqlite3.connect('data_structures.db')
cursor = conn.cursor()
results = {}

def unordered_array_version(data):
    array_data = list(data.items())

    new_key = max(data.keys()) + 1
    new_value = random.randint(1, 100)
    array_data.append((new_key, new_value))

    search_key = random.choice(list(data.keys()))
    found_value = next((value for key, value in array_data if key == search_key), None)

    delete_key = random.choice(list(data.keys()))
    array_data = [(key, value) for key, value in array_data if key != delete_key]

def linked_list_version(data):
    sorted_data = sorted(data.items(), key=lambda x: x[0])

    new_key = max(data.keys()) + 1
    new_value = random.randint(1, 100)
    sorted_data.append((new_key, new_value))

    search_key = random.choice(list(data.keys()))
    found_value = next((value for key, value in sorted_data if key == search_key), None)

    delete_key = random.choice(list(data.keys()))
    sorted_data = [(key, value) for key, value in sorted_data if key != delete_key]

def hash_table_version(data):
    new_key = max(data.keys()) + 1
    new_value = random.randint(1, 100)
    data[new_key] = new_value

    search_key = random.choice(list(data.keys()))
    found_value = data.get(search_key, None)

    delete_key = random.choice(list(data.keys()))
    data.pop(delete_key, None)

def balanced_tree_version(data):
    sorted_data = SortedDict(data)

    new_key = max(data.keys()) + 1
    new_value = random.randint(1, 100)
    sorted_data[new_key] = new_value

    search_key = random.choice(list(data.keys()))
    found_value = sorted_data.get(search_key, None)

    delete_key = random.choice(list(data.keys()))
    sorted_data.pop(delete_key, None)

def measure_performance(func, version):
    start_time = time.time()
    func(fake_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    results[version] = elapsed_time
    print(f"{version} version took {elapsed_time:.6f} seconds.")

if __name__ == "__main__":
    print("\nResults:")
    measure_performance(unordered_array_version, "Unordered Array")
    measure_performance(linked_list_version, "Linked List")
    measure_performance(hash_table_version, "Hash Table")
    measure_performance(balanced_tree_version, "Balanced Tree")