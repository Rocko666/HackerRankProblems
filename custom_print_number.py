if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 20:
        list1 = []
        list1 = list(range(n))
        print(list1)
        j = []
        for i in list1:
            j.append(i*i)
        print(j)
