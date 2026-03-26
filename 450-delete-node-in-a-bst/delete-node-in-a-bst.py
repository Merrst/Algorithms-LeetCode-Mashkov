# Определение узла дерева: class TreeNode: val, left, right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Базовый случай: если дерево пустое или ключ не найден
        if not root:
            return None
        
        # Поиск целевого узла в зависимости от значения ключа
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Случай 1 и 2: у узла нет детей или только один потомок
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Случай 3: у узла два ребенка
            # Находим минимальный узел в правом поддереве (successor)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Копируем значение преемника в текущий узел
            root.val = curr.val
            # Удаляем преемника из правого поддерева
            root.right = self.deleteNode(root.right, curr.val)
            
        # Возвращаем обновленный корень поддерева
        return root