import random

def sort_merge(my_list):

    if len(my_list) > 1:
        half = len(my_list) // 2
        left = my_list[:half]
        rigth = my_list[half:]

        sort_merge(left)
        sort_merge(rigth)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(rigth):

            if left[i] < rigth[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = rigth[j]
                j += 1
            
            k += 1
        
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(rigth):
            my_list[k] = rigth[j]
            j += 1
            k += 1
        
    return my_list


if __name__ == '__main__':
    size_list = int(input('What size is the list ? '))
    my_list = [random.randint(0,100) for i in range(size_list)]

    ordered_list = sort_merge(my_list)
    print(ordered_list)