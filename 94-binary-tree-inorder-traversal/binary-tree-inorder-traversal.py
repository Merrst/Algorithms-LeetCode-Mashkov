# Определение узла дерева: class TreeNode: val, left, right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Список для хранения итоговой последовательности значений
        result = []

        def dfs(node):
            # Базовый случай: если текущий узел пуст, завершаем выполнение функции
            if not node:
                return
            
            # Рекурсивный переход в левое поддерево до самого конца
            dfs(node.left)
            
            # Добавление значения узла в результат после обработки левой ветви
            result.append(node.val)
            
            # Рекурсивный переход в правое поддерево для завершения обхода ветви
            dfs(node.right)

        # Запуск вспомогательной функции от корневого узла
        dfs(root)
        return result