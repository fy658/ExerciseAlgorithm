def bubble_sort(lists):
    for i in range(len(lists)):
        #进行一轮比较换位后，n个元素中的最大元素将位于第n位，然后对前n-1个元素进行第二轮比较，重复该过程直到进行比较的元素只剩下一个为止
        for j in range(len(lists)-i-1):
            if lists[j]>lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists

print(bubble_sort([36,25,48,12,25,65,43,57]))
