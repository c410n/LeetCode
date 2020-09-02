class Solution:
    def rec_search(self, arr, pos, down, up, val):
        if up - down < 2:
            if arr[pos] == val:
                return pos
            else:
                return -1
        elif arr[pos] == val:
            return pos
        
        has_cycle_point = not arr[up-1] > arr[down]
        
        posl = down + math.floor((pos - down)/2)
        posr = pos + math.floor((up - pos)/2)
                
        if arr[pos] < val:
            if has_cycle_point:                
                rl = self.rec_search(arr, posl, down, pos, val)
                rr = self.rec_search(arr, posr, pos, up, val)
                return rl if rl != -1 else rr
            else:
                rr = self.rec_search(arr, posr, pos, up, val)
                return rr
        else: # arr[pos] > val
            if has_cycle_point:
                rl = self.rec_search(arr, posl, down, pos, val)
                rr = self.rec_search(arr, posr, pos, up, val)
                return rl if rl != -1 else rr
            else:
                rl = self.rec_search(arr, posl, down, pos, val)
                return rl
        
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return self.rec_search(nums, math.floor(len(nums)/2), 0, len(nums), target)