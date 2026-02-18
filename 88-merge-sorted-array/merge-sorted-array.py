class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # i — последний индекс значимых элементов в nums1
        i = m - 1
        # j — последний индекс nums2
        j = n - 1
        # k — последний индекс итогового массива nums1
        k = m + n - 1

        # идем с конца и сравниваем элементы
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # берем больший элемент
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # если в nums2 что-то осталось, переносим в nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
