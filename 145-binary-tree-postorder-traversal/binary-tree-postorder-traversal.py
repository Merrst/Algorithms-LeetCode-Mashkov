# Определение узла дерева: class TreeNode: val, left, right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Список для сбора значений в порядке обратного обхода (лево-право-корень)
        result = []

        def dfs(node):
            # Базовый случай: если достигнут пустой узел, выходим из рекурсии
            if not node:
                return
            
            # Рекурсивно обрабатываем сначала все узлы в левом поддереве
            dfs(node.left)
            
            # Затем рекурсивно обрабатываем все узлы в правом поддереве
            dfs(node.right)
            
            # В самую последнюю очередь записываем значение текущего узла
            result.append(node.val)

        # Запускаем процесс обхода с корневого узла дерева
        dfs(root)
        return result