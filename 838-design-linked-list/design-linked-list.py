class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        # Инициализируем пустой список и храним его размер
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        curr = self.head
        # Идем по ссылкам до нужного узла
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        # Новый узел становится головой и указывает на старую голову
        self.head = ListNode(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        if index <= 0:
            self.addAtHead(val)
            return
        curr = self.head
        # Ищем узел перед тем местом, куда хотим вставить
        for _ in range(index - 1):
            curr = curr.next
        curr.next = ListNode(val, curr.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            # "Прыгаем" через один узел, исключая его из списка
            curr.next = curr.next.next
        self.size -= 1