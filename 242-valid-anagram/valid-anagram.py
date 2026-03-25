class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Если длины строк разные, они точно не могут быть анаграммами
        if len(s) != len(t):
            return False
        
        # Используем словари (хэш-таблицы) для подсчета символов
        # Ключ — символ, значение — количество его повторений
        countS, countT = {}, {}
        
        for i in range(len(s)):
            # Метод .get(ключ, 0) позволяет избежать ошибки, 
            # если символа еще нет в таблице
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # Сравниваем две хэш-таблицы. Если они идентичны — это анаграмма
        return countS == countT