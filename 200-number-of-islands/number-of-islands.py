class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Проверка на пустую входную сетку
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands_count = 0

        def dfs(r, c):
            # Условие выхода: выход за границы сетки или встреча с водой ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            # Пометка текущей клетки как посещенной путем изменения '1' на '0'
            grid[r][c] = '0'

            # Рекурсивные переходы к соседним клеткам в четырех направлениях
            dfs(r + 1, c) # вниз
            dfs(r - 1, c) # вверх
            dfs(r, c + 1) # вправо
            dfs(r, c - 1) # влево

        # Проход по всем ячейкам матрицы
        for r in range(rows):
            for c in range(cols):
                # Если найдена суша, увеличивается счетчик и запускается DFS
                if grid[r][c] == '1':
                    islands_count += 1
                    dfs(r, c)

        return islands_count