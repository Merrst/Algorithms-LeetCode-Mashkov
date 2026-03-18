class MyCircularQueue:
    def __init__(self, k: int):
        # Создаем массив фиксированного размера k
        self.queue = [0] * k
        self.size = k
        self.head = 0  # Индекс первого элемента
        self.count = 0 # Текущее количество элементов

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        # Находим индекс для вставки через остаток от деления
        tail = (self.head + self.count) % self.size
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        # Просто сдвигаем голову очереди вперед
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        # Находим индекс последнего добавленного элемента
        tail = (self.head + self.count - 1) % self.size
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size