# Определение узла дерева: class TreeNode: val, left, right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Вспомогательная функция с передачей границ (минимально и максимально допустимое значение)
        def validate(node, low=-float('inf'), high=float('inf')):
            # Базовый случай: пустое дерево является валидным BST
            if not node:
                return True
            
            # Если значение текущего узла выходит за рамки допустимого интервала, дерево невалидно
            if not (low < node.val < high):
                return False
            
            # Рекурсивно проверяем левое поддерево (обновляем верхнюю границу) 
            # и правое поддерево (обновляем нижнюю границу)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Запускаем проверку от корня с бесконечными границами
        return validate(root)