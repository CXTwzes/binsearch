# coding:utf-8


def search(item, lst, right, left):
    mid = (left + right) / 2
    if left <= right:
        if lst[mid] == item:
            return mid
        else:
            if item > lst[mid]:
                return search(lst, item, mid + 1, right)
            else:
                return search(lst, item, left, mid - 1)
    return -1
scores = []
numbers = []
score = 0
index = 1
score = raw_input('请输入一个整数(0表示结束）：')
while score != 0:
    scores.insert(index, score)
    numbers.insert(index, index - 1)
    index += 1
    score = input('请输入一个整数(0表示结束）：')
print ('编号\t' + '\t'.join([str(i) for i in numbers]))
print ('分数值\t' + '\t'.join([str(i) for i in scores]))
nfScore = int(input('您要查找的分数是：'))
result = search(scores, nfScore, 0, index - 2)
if result != -1:
    print(str(nfScore) + ' 的编号是 ' + str(result))
else:
    print('Not Found')
