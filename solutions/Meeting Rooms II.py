class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        I = sorted(intervals)
        P = None
        C = 0
        while I:
            i = 0
            while i < len(I):
                if P == None:
                    # print("A")
                    P = I[i]
                    del I[i]
                else:
                    if P[1] <= I[i][0]:
                        P = I[i]
                        del I[i]
                    else:
                        i += 1
                # print("M", i, P, C, I[i] if len(I) > i else "Empty", I)
            C += 1
            P = None
            # print("E", i, P, C, I[i] if len(I) > i else "Empty", I)
        return C