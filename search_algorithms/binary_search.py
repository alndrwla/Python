import random

def search_binary(search_list, init, final, objective):

    if(init > final):
        return False

    middle = (init + final) // 2
    
    if search_list[middle] == objective:
        return True
    elif search_list[middle] < objective:
        return search_binary(search_list, middle +1, final, objective)
    else:
        return search_binary(search_list, init, middle-1, objective)


if __name__ == '__main__':

    size_list = int(input("What size is the list ? : "))
    objective = int(input("What number do you want to find ? : "))

    search_list = sorted([random.randint(0,100) for i in range(size_list)])
    objective_search = search_binary(search_list, 0, len(search_list), objective)

    print(f'The element {objective} {" is " if objective_search else "is not"} in the list.')