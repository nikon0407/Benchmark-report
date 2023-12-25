import sqlite3
import time
import random
from sortedcontainers import SortedDict
import unittest
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
    
class TestVersions(unittest.TestCase):
    def tearDown(self):
        pass

    def test_unordered_array_version(self):
        self._test_version(unordered_array_version, "Unordered Array")

    def test_linked_list_version(self):
        self._test_version(linked_list_version, "Linked List")

    def test_hash_table_version(self):
        self._test_version(hash_table_version, "Hash Table")

    def test_balanced_tree_version(self):
        self._test_version(balanced_tree_version, "Balanced Tree")

    def _test_version(self, version_function, version_name):
        start_time = time.time()
        version_function(fake_data)
        end_time = time.time()
        elapsed_time = end_time - start_time

        self.assertTrue(self._verify_version(fake_data), f"{version_name} failed to maintain data integrity.")
        print(f"{version_name} version took {elapsed_time:.6f} seconds.")

    def _verify_version(self, data):
        if isinstance(data, list):
            return all(data[i][0] <= data[i + 1][0] for i in range(len(data) - 1))
        elif isinstance(data, SortedDict):
            current = data.head
            while current.next:
                if current.key > current.next.key:
                    return False
                current = current.next
            return True
        elif isinstance(data, dict):
            required_keys = [1, 2, 3]
            return all(key in data for key in required_keys)
        elif isinstance(data, SortedDict):
            return all(data.peekitem(i)[0] <= data.peekitem(i + 1)[0] for i in range(len(data) - 1))
        else:
            return False

if __name__ == '__main__':
    print("\nResults:")
    measure_performance(unordered_array_version, "Unordered Array")
    measure_performance(linked_list_version, "Linked List")
    measure_performance(hash_table_version, "Hash Table")
    measure_performance(balanced_tree_version, "Balanced Tree")
    print("\nTest:")
    unittest.main()