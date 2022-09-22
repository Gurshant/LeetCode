
from typing import List
from math import inf
class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     result = []
        # finding_max =False
        # min_num=-inf
        # for i in range(0,len(intervals )+1):
            # if i == len(intervals):
            #     if len(intervals)==0 :
            #         result.append(newInterval)
            #     elif result[-1][1] < newInterval[1]:
            #         result.append(min_num, newInterval[1])
            #     break
            # if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
            #     finding_max =True
            #     min_num = min(intervals[i][0], newInterval[0])
            # elif finding_max:
            #     if intervals[i][0] > newInterval[1]:
            #         result.append([min_num, newInterval[1]])
            #         result.append(intervals[i])
            #         finding_max=False
            #     elif intervals[i][0] <= newInterval[1] <= intervals[i][1]:
            #         result.append([min_num, intervals[i][1]])
            #         finding_max=False
            # else: 
            #     result.append(intervals[i])
            
    #     return result

    def insert(self, intervals: List[List[int]], newInterval: List[int])-> List[List[int]]:
        result=[]
        finding_max =False
        min_num=-inf
        for i in range(0,len(intervals)+1):
            if i == len(intervals) +1:
                if len(intervals)==0 :
                    result.append(newInterval)
                elif not result or result[-1][1] < newInterval[1]:
                    result.append([min_num, newInterval[1]])
                break

            
            if finding_max :
                if intervals[i][0] <= result[-1][1] < intervals[i][1]:
                    result[-1][1] = intervals[i][1]
                    finding_max=False
                    return result + intervals[i+1:]
                elif result[-1][1] < intervals[i][0]:
                    result.append(intervals[i])
                    finding_max=False
                    return result + intervals[i+1:]
            elif intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                finding_max = True
                result.append([intervals[i][0], max(newInterval[1], intervals[i][1])])
            elif intervals[i][0] >newInterval[0]:
                min_num = newInterval[0]
            else: 
                result.append(intervals[i])


s= Solution()

print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))