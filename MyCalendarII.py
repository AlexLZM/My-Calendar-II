class MyCalendarTwo:
    def __init__(self):
        self.pos = []
        self.cnt = {}

    def book(self, start: 'int', end: 'int') -> 'bool':
        i = bisect.bisect_left(self.pos, start)
        j = bisect.bisect_left(self.pos, end)
        
        if any(self.cnt[self.pos[k]] >= 2 for k in range(i, j)):
            return False
          
        if start not in self.cnt:
            c = self.cnt[self.pos[i-1]] if i-1 >= 0 else 0
            if c >= 2: return False
            self.pos.insert(i,start)
            j += 1
            self.cnt[start] = c
            
        if end not in self.cnt:
            self.pos.insert(j,end)
            self.cnt[end] = self.cnt[self.pos[j-1]]
            
        for k in range(i, j):
            self.cnt[self.pos[k]] += 1

        return True
