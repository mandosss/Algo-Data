#   The program runs and gives correct outputs to the problem
#       but becuase of some math arithmetic, it takes "too long"
#       with large numbers
#
#

def xoring(bit_value, bit_TestCase):
    return bin(bit_value ^ bit_TestCase)
        
def check_even_odd(number):
    if(number % 2):
        print('Odd')
    else:
        print('Even')
        
def main():
    num_test_cases = int(input())
    test_list = []
    i = 0
    while(i < num_test_cases):
        test_list.append(list(map(int, input().split())))
        i += 1
    for x in test_list:
        if x[0] == x[1]:
            check_even_odd(x[0])
        else:
            temp_xoring = x[0]
            while(x[0] < x[1]):
                x[0] += 1
                temp_xoring = int(xoring(temp_xoring,x[0]), 2)
            check_even_odd(temp_xoring)

if __name__ == "__main__":
    main()