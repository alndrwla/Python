import random

def bubble_sort(my_list):
    n = len(my_list)

    for i in range(n):
        for j in range(0,n -i -1):

            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    return my_list


if __name__ == '__main__':
    size_list = int(input('What size is the list ? '))

    my_list = [random.randint(0,100) for i in range(size_list)]

    ordered_list = bubble_sort(my_list)
    print(ordered_list)