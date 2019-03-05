import random

def binary_search(data, target, low, high):
    """
        Return True if target is found in indicated portion of a python list.
        The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True;
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data, target, mid+1, high)


def main():
    cool_list = [int(random.random()*1000000) for i in range(1000000)]  
    #cool_list.append(500001) 
    cool_list.sort()     
    print(binary_search(cool_list, 1, 0, len(cool_list)))

if __name__ == '__main__':
    main()