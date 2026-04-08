class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # Сохранение цвета исходного пикселя для сравнения
        start_color = image[sr][sc]
        
        # Если текущий цвет уже равен целевому, замена не требуется
        if start_color == color:
            return image
        
        # Определение размеров матрицы
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Проверка выхода за границы и соответствия исходному цвету
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return
            
            # Установка нового цвета для текущего пикселя
            image[r][c] = color
            
            # Рекурсивные вызовы для соседних клеток в четырех направлениях
            dfs(r + 1, c) # Вниз
            dfs(r - 1, c) # Вверх
            dfs(r, c + 1) # Вправо
            dfs(r, c - 1) # Влево
            
        # Запуск обхода со стартовой позиции
        dfs(sr, sc)
        
        return image