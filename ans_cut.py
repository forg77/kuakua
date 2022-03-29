reading = open('ans_content.txt','r',encoding='utf-16')
ans_list = []
cur_str = ""
flag = False
while True:

    add_str = reading.readline()
    if not add_str:
        print('done')
        print(len(ans_list))
        break
    if flag and add_str == '\n':
        ans_list.append(add_str)
    else:
        cur_str += add_str
        flag = False
        if add_str[-3:] == '##\n':
            ans_list.append(cur_str)
            cur_str = ""
            flag = True


while True:
    s = int(input())
    print(ans_list[s])
