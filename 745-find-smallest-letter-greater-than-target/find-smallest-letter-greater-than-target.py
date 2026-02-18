class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # начинаем с первой буквы
        left = 0
        
        # заканчиваем на последней букве
        right = len(letters) - 1

        # пока есть где искать
        while left <= right:
            
            # берем середину
            mid = (left + right) // 2

            # если буква в середине меньше или равна target
            if letters[mid] <= target:
                # ищем правее
                left = mid + 1
            else:
                # ищем левее
                right = mid - 1

        # если дошли до конца списка,
        # возвращаем первую букву (зацикливание)
        return letters[left % len(letters)]
