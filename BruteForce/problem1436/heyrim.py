def generator_666_list(n):
    count = 0
    num = 1

    while(count != n):
        if (not(str(num).find("666") == -1)):
            count += 1
        num += 1
        
    n_666 = num-1
    return n_666

N = int(input())

print(generator_666_list(N)) 