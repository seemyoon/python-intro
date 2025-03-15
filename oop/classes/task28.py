# create own array, like in js
class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)

    def __len__(self):
        return len(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, key):
        return self.__arr[key]

    def __delitem__(self, key):
        del self.__arr[key]

    def push(self, value):
        self.__arr.append(value)

    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])

    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])


arr = Array(1, 22, 12, 21, 3, 13)
arr.push(2)
del arr[3]
print(arr)

arr_map = arr.map(lambda x: x * 2)
arr_filter = arr.filter(lambda x: x < 5)
print(arr_map)
print(arr_filter)
