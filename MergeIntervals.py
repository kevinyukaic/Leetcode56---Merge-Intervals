# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#First though: simular to scheduling problems
#we could use two pointers to move along the intervals 
#if the next start of the interval is smaller than the end of the previous one
# we merge them together, so the end pointer shift to the larger ends
# and check the next interval,
# if the next start is larger than the end of the current one
# we append the current one in the list and shift to the next one

#will in comes in order?
#if not, we need to handle different start order.
#we could also sort by start time first
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        
        sortedList = []
        result = []
        #check the input here
        if (intervals == None or intervals == []):
            return []
        if(len(intervals) == 1):
            return intervals
        
        for i in intervals:
            sortedList.append([i.start,i.end])
        sortedList.sort()
            

        pCurr = 0
        pNext = 1
        mergeCount = 0
        #if the next start is smaller than the current end
        #merge them to one
        while(pNext < len(sortedList)):
            if(sortedList[pNext][0] <= sortedList[pCurr][1]):
                sortedList[pCurr][1] = max(sortedList[pCurr][1],sortedList[pNext][1])
                pNext+=1
                if(pNext == len(sortedList)):
                    result.append(Interval(s = sortedList[pCurr][0], e = sortedList[pCurr][1]))
                    
            elif(sortedList[pNext][0] > sortedList[pCurr][1]):
                result.append(Interval(s = sortedList[pCurr][0], e = sortedList[pCurr][1]))
                pCurr = pNext
                pNext += 1
                if(pCurr == len(intervals)-1):
                    result.append(Interval(s = sortedList[pCurr][0], e = sortedList[pCurr][1]))
        return result     
            