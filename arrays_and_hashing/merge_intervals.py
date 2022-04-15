intervals = [[1,2], [4,7], [5,9], [3,5], [10,15]]

def merge_intervals(arr):
    arr.sort(key = lambda x:x[1])
    #print(arr)
    output = [arr[0]]

    for start, end in arr[1:]:
        last_end = output[-1][1]

        if last_end >= start:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])

    return output

print(merge_intervals(intervals))