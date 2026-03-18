class MinStack:
    def __init__(self):
        # Основной стек для хранения всех чисел
        self.stack = []
        # Дополнительный стек для хранения текущих минимумов
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Если новый элемент меньше или равен текущему минимуму, кладем его в min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Если удаляемое число — это текущий минимум, убираем его и из min_stack
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Просто возвращаем последний элемент основного стека
        return self.stack[-1]

    def getMin(self) -> int:
        # Минимум всегда лежит на вершине min_stack
        return self.min_stack[-1]