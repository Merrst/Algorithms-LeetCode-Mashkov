class MyQueue:
    def __init__(self):
        # Первый стек для приема новых элементов
        self.in_stack = []
        # Второй стек для выдачи элементов в правильном порядке
        self.out_stack = []

    def push(self, x: int) -> None:
        # Просто добавляем элемент в основной стек
        self.in_stack.append(x)

    def pop(self) -> int:
        # Подготавливаем out_stack и забираем из него верхний элемент
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        # Если "выходной" стек пуст, перекладываем в него всё из "входного"
        # Это разворачивает порядок элементов, превращая стек в очередь
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Очередь пуста, только если оба стека пусты
        return not self.in_stack and not self.out_stack