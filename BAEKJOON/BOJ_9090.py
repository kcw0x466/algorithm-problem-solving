str_count=int(input())
str_list=[]

def strReverse(str):
    list=str.split(' ')
    reverse_wordList=[]
    for i in list:
        reverse_wordList.append(i[::-1])       
    reverse_str=' '.join(reverse_wordList)
    return reverse_str

for i in range(str_count):
    str=input()
    str_list.append(str)

for i in range(str_count):
    print(strReverse(str_list[i]))