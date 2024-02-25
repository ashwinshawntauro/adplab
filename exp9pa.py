def median(list):
    if not list:
        return None
    list.sort()
    mid=len(list)//2
    return list[mid]+1 if len(list)%2 else (list[mid-1]+list[mid])/2

list=[10,12,43,52,66,32,12,23]
print(median(list))