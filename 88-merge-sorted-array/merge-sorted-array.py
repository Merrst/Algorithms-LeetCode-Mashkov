class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Указатель на последний значимый элемент в nums1
        i = m - 1
        # Указатель на последний элемент в nums2
        j = n - 1
        # Указатель на последнюю позицию в итоговом массиве nums1
        k = m + n - 1

        # Двигаемся с конца, сравнивая элементы обоих массивов
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]       # Копируем больший элемент из nums1
                i -= 1
            else:
                nums1[k] = nums2[j]       # Копируем больший элемент из nums2
                j -= 1
            k -= 1

        # Если остались элементы в nums2, переносим их в начало nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1