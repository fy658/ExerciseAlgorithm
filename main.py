# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # s = [False, False, False]
    # for i in range(3):
    #     if s[i]:
    #         print(s[i])
    #         continue
    #     # print(s[i])
    #     s[i] = True
    print('hello','fangyu', sep="")
    s = 'helloword'
    t= 'hellot'
    print(s.find(t))
    # array1 = list(map(int, input().split()))[1:]
    # print(array1)
    # print(float('-inf'))
    # t1, t2 = map(int, input().split())
    # print(t1, t2)

    # array = [1,2,4,5]
    # print(array[1:8])
    # m = list(filter(lambda x: x != '', input().split(',')))
    # print(m)
    arr = [1,3,6,8,4]
    arr1 = arr.pop(0)
    ## append()方法如果是添加一个数组，那么也会把他作为一个元素添加到原来数组中去  [3, 6, 8, 4, [8, 4]]
    arr.append(arr[2:])
    print(arr1, arr)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
