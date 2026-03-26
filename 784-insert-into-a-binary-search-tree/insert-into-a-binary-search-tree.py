# Определение узла дерева: class TreeNode: val, left, right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Базовый случай: если нашли пустое место, создаем и возвращаем новый узел
        if not root:
            return TreeNode(val)
        
        # Если вставляемое значение больше текущего узла, идем в правое поддерево
        if val > root.val:
            # Рекурсивно обновляем правую ветвь
            root.right = self.insertIntoBST(root.right, val)
        # Если значение меньше текущего, идем в левое поддерево
        else:
            # Рекурсивно обновляем левую ветвь
            root.left = self.insertIntoBST(root.left, val)
            
        # Возвращаем корень измененного дерева
        return root