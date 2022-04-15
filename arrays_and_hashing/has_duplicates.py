A = [1,2,3,4,5]
my_set = set() #Has set

def has_duplicates(A):
    for i in A:
        if i in my_set:
            print('Has a duplicate ', i)
            return True
        my_set.add(i)
    print(my_set)
    return False
        
print(has_duplicates(A))
