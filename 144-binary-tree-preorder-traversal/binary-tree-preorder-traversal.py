# Определение узла дерева: class TreeNode: val, left, right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Список для накопления значений в порядке прямого обхода
        result = []

        def dfs(node):
            # Если узел пуст, завершаем выполнение текущего шага рекурсии
            if not node:
                return
            
            # Сначала записываем значение текущего (корневого) узла
            result.append(node.val)
            
            # Затем рекурсивно переходим к обработке левого поддерева
            dfs(node.left)
            
            # В последнюю очередь обрабатываем правое поддерево
            dfs(node.right)

        # Инициируем обход, начиная с корневого узла дерева
        dfs(root)
        return result