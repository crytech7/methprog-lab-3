import time
from sortedcontainers import SortedDict

SIMPLE_HASH_COLLISIONS = 0
COMPLEX_HASH_COLLISIONS = 0
SIMPLE_CLUBS = 0
COMPLEX_CLUBS = 0


class Object:
    """Объект требуемый в задании"""

    def simpleHashString(self, string=''):
        '''Простая хеш-функция - сумма ascii кодов первых двух символов'''
        hash = 0
        hash += ord(string[0]) + ord(string[1])
        return hash % (10 ** 8)

    def complexHashString(self, string=''):
        '''Сложная хеш-функция'''
        hash = 0
        for i in range(len(string)):
            # hash += (((ord(string[i]) ** i) % (2 ** 64) - ord(string[i]) ** 2) ** (ord(string[i]) ** ord(string[i]))) % (2 ** 64)
            hash += (((ord(string[i]) ** (i * i * ord(string[i])) % (2 ** 64)) - ord(string[i]) ** 2 // ord(
                string[i])) ** (ord(string[i])))
        return hash % (10 ** 128)

    def __init__(self, Country, Club_Name, City, Year, Coach_Name, Points, hashtype="simple"):
        """Конструктор"""
        self.Country = Country
        self.Club_Name = Club_Name
        if hashtype == "simple":  # Если хеширование "простое"
            self.Club_NameHash = self.simpleHashString(self.Club_Name)
        elif hashtype == "complex":  # Если хеширование "сложное"
            self.Club_NameHash = self.complexHashString(self.Club_Name)
        self.City = City
        self.Year = Year
        self.Coach_Name = Coach_Name
        self.Points = Points

    def __gt__(self, other):
        """operator > overloading"""

        if self.Year > other.Year:
            return True
        elif self.Year < other.Year:
            return False
        elif self.Year == other.Year:
            if self.Country > other.Country:
                return True
            elif self.Country < other.Country:
                return False
            elif self.Country == other.Country:
                if self.Points > other.Points:
                    return True
                elif self.Points < other.Points:
                    return False
                elif self.Points == other.Points:
                    if self.Club_Name > other.Club_Name:
                        return True
                    elif self.Club_Name < other.Club_Name:
                        return False
                    elif self.Club_Name == other.Club_Name:
                        return False

    def __lt__(self, other):
        """operator < overloading"""

        return other > self

    def __ge__(self, other):
        """operator >= overloading"""

        if self.Year > other.Year:
            return True
        elif self.Year < other.Year:
            return False
        elif self.Year == other.Year:
            if self.Country > other.Country:
                return True
            elif self.Country < other.Country:
                return False
            elif self.Country == other.Country:
                if self.Points > other.Points:
                    return True
                elif self.Points < other.Points:
                    return False
                elif self.Points == other.Points:
                    if self.Club_Name > other.Club_Name:
                        return True
                    elif self.Club_Name < other.Club_Name:
                        return False
                    elif self.Club_Name == other.Club_Name:
                        return True

    def __le__(self, other):
        """operator <= overloading"""

        return other >= self

    def __eq__(self, other):
        """operator == overloading"""
        # Country,Club_Name,City,Year,Coach_Name,Points
        return self.Year == other.Year and self.Country == other.Country and \
            self.Points == other.Points and self.Club_Name == other.Club_Name and \
            self.City == other.City and self.Coach_Name == other.Coach_Name


def complexHashString(string):
    '''Функция для хеширования чуть более сложным хешем'''
    hash = 0
    for i in range(len(string)):
        # hash += (((ord(string[i]) ** i) % (2 ** 64) - ord(string[i]) ** 2) ** (ord(string[i]) ** ord(string[i]))) % (2 ** 64)
        hash += (((ord(string[i]) ** (i * i * ord(string[i])) % (2 ** 64)) - ord(string[i]) ** 2 // ord(string[i])) ** (
            ord(string[i])))
    return hash % (10 ** 128)


def simpleHashString(string):
    '''Функция для хеширования простым хешем'''
    hash = 0
    hash += ord(string[0]) + ord(string[1])
    return hash % (10 ** 8)


def hashTable(objectsArray, type="simple"):
    '''Делаем из списка объектов хэш-таблицу'''
    map = SortedDict()
    for i in objectsArray:
        if i.Club_NameHash not in map.keys():
            map[i.Club_NameHash] = [i]
        else:  # Если произошла коллизия
            map[i.Club_NameHash].append(i)
    return map


def find(string, hashTable, hashtype="simple"):
    global SIMPLE_HASH_COLLISIONS
    global COMPLEX_HASH_COLLISIONS
    global SIMPLE_CLUBS
    global COMPLEX_CLUBS

    try:
        if hashtype == "simple":  # пример для простого алгоритма хеширования
            result = hashTable[simpleHashString(string)]
            if len(result) == 1:  # Если коллизий нет
                return result[0]
            elif len(result) > 1:  # Если коллизии есть
                SIMPLE_CLUBS.append(string)
                for i in result:
                    if i.Club_Name not in SIMPLE_CLUBS:
                        SIMPLE_HASH_COLLISIONS += 1
                    if i.Club_Name == string:
                        return i
        elif hashtype == "complex":
            result = hashTable[complexHashString(string)]  # пример для чуть более сложного алгоритма хеширования
            if len(result) == 1:  # Если коллизий нет
                return result[0]
            elif len(result) > 1:  # Если коллизии есть
                COMPLEX_CLUBS.append(string)
                for i in result:
                    if i.Club_Name not in COMPLEX_CLUBS:
                        COMPLEX_HASH_COLLISIONS += 1
                    if i.Club_Name == string:
                        return i
    except KeyError:
        return -1


size = [10, 100, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
EXPERIMENTS_AMOUNT = 1

if __name__ == "__main__":
    simple_hash_times = []
    complex_hash_times = []
    meta_simple_hash_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    meta_complex_hash_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    meta_complex_collisions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    meta_simple_collisions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for times in range(EXPERIMENTS_AMOUNT):
        simple_hash_times = []
        complex_hash_times = []
        simple_collisions = []
        complex_collisions = []
        for i in range(len(size)):
            """Сортируем нагенеренное"""
            f = open("ds_" + str(size[i]) + ".csv", 'r')
            arr = []
            print("STARTING SIZE", size[i])
            for j in f.readlines():
                temp = j.split(",")
                arr.append(Object(temp[0], temp[1], temp[2], int(temp[3]), temp[4], int(temp[5]), hashtype="simple"))
            f.close()

            hashTableUnit1 = hashTable(arr, type="simple")
            # print(hashTableUnit1)
            time1 = time.time()
            item = find("Atletico Madrid", hashTableUnit1, hashtype="simple")
            time2 = time.time() - time1
            simple_collisions.append(SIMPLE_HASH_COLLISIONS)
            SIMPLE_HASH_COLLISIONS = 0
            SIMPLE_CLUBS = []
            simple_hash_times.append(time2)
            print("simple hash, size", size[i], ":", time2, )

        for i in range(len(size)):
            """Сортируем нагенеренное"""
            f = open("ds_" + str(size[i]) + ".csv", 'r')
            arr = []
            print("STARTING SIZE", size[i])
            for j in f.readlines():
                temp = j.split(",")
                arr.append(Object(temp[0], temp[1], temp[2], int(temp[3]), temp[4], int(temp[5]), hashtype="complex"))
            f.close()

            hashTableUnit2 = hashTable(arr, type="complex")
            # print(hashTableUnit2)
            time1 = time.time()
            item = find("Atletico Madrid", hashTableUnit2, hashtype="complex")
            time2 = time.time() - time1
            complex_collisions.append(COMPLEX_HASH_COLLISIONS)
            COMPLEX_HASH_COLLISIONS = 0
            COMPLEX_CLUBS = []
            complex_hash_times.append(time2)
            print("complex hash, size", size[i], ":", time2)

        print(simple_hash_times)
        print(complex_hash_times)
        for amount in range(len(simple_hash_times)):
            meta_simple_hash_times[amount] += simple_hash_times[amount]
            meta_complex_hash_times[amount] += complex_hash_times[amount]
            meta_simple_collisions[amount] += simple_collisions[amount]
            meta_complex_collisions[amount] += complex_collisions[amount]

    for i in range(len(meta_simple_hash_times)):
        meta_simple_hash_times[i] /= EXPERIMENTS_AMOUNT
        meta_complex_hash_times[i] /= EXPERIMENTS_AMOUNT
        meta_complex_collisions[i] //= EXPERIMENTS_AMOUNT
        meta_simple_collisions[i] //= EXPERIMENTS_AMOUNT
    print("meta_simple_hash_times =", meta_simple_hash_times)
    print("meta_complex_hash_times =", meta_complex_hash_times)
    print("meta_simple_collisions =", meta_simple_collisions)
    print("meta_complex_collisions =", meta_complex_collisions)
 
