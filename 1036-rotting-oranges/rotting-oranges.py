from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Поиск начальных гнилых апельсинов и подсчет свежих
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # Если свежих апельсинов сразу нет, время ожидания равно 0
        if fresh_count == 0:
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Пошаговое распространение гнили через BFS
        while queue and fresh_count > 0:
            minutes += 1
            # Обработка всех апельсинов, ставших гнилыми на текущей минуте
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Если сосед — свежий апельсин, он становится гнилым
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        
        # Если после обхода остались свежие апельсины, возвращается -1
        return minutes if fresh_count == 0 else -1