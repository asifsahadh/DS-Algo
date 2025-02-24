# Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.

def merge(intervals):
    
    intervals.sort()
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged

merge(intervals)