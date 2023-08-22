class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n <0:
            raise ValueError("Amount to deposit must be a non-negative integer")
        elif self._size + n > self._capacity:
            raise ValueError("Not enough room in the jar")
        self._size +=n

    def withdraw(self, n):
        if not isinstance(n, int) or n <0:
            raise ValueError("Amount to withdraw must be a non-negative integer")
        elif self._size < n:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property # Getter
    def capacity(self):
        return self._capacity

    @property # Getter
    def size(self):
        return self._size

jar = Jar()
jar.deposit(9)
print(jar)
jar.withdraw(4)
print(jar)