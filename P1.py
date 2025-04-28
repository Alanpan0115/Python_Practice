# 1. 整數相加
# 寫一個函式，接收兩個整數參數，回傳它們的和。
def a1_function(a,b):
    print("Q1.兩數相加合為 : " + str(a+b))
a1_function(5,6)

# ----------------------------------------------------------------
# 2. 判斷奇數或偶數
# 輸入一個整數，判斷是奇數還是偶數。
def a2_function(a):
    if a%2 ==1:
        print("Q2.此數為奇數")
    else:
        print("Q2.此數為偶數")
a2_function(8)

# ----------------------------------------------------------------
# 3.反轉字串
# 寫一個函式，接收一個字串，回傳這個字串的反轉結果。
def a3_function(a):
    reversed_string = ''
    for i in a:
        reversed_string = i + reversed_string
    print("Q3.",reversed_string)
a3_function('abcdefg')

# ----------------------------------------------------------------
# 4. 找出最大值
# 給一個數字串列，找出其中最大的數字。
def a4_function(L4):
    Max = L4[0]
    for i in L4:
        if i> Max:
            Max=i
    print("Q4.",Max)
    # print(max(L4)) --> 最簡單
L4 = [10,5,9,50,63,74,19]
a4_function(L4)

# ----------------------------------------------------------------
# 5. 計算字母出現次數
# 輸入一個字串，計算字母 'a' 出現了幾次。（忽略大小寫）
def a5_function(a):
    a = a.upper()  # 把字串轉成大寫
    a5_dic = {}    # 建立一個空字典
    for i in a:
        if i in a5_dic:
            a5_dic[i] += 1  # 如果已經有這個字母，數量 +1
        else:
            a5_dic[i] = 1   # 如果第一次遇到，設為 1
    print("Q5.",a5_dic)
a5_function('AcdCdBabfAackajfAag')

# ----------------------------------------------------------------
# 6. 印出九九乘法表
# 用 for 迴圈印出 1 到 9 的九九乘法表。

def a6_function():
    print('Q6.99乘法表')
    for i in range(1,10):
        for j in range(1,10):
            print(str(i) +' x '+ str(j) + ' = '+ str(i*j))
a6_function()

# ----------------------------------------------------------------
# 7. 判斷質數
# 輸入一個正整數，判斷是否為質數（只能被1和自己整除的數）。
def a7_function(a):
    if a <= 1:
        print("Q7.不是質數")
        return
    for i in range(2, a):
        if a % i == 0:
            print("Q7.不是質數")
            return
    print("Q7.是質數")

a7_function(7)

# ----------------------------------------------------------------
# 8. 建立一個簡單的列表
# 寫一個函式，回傳一個包含從 1 到 10 的整數列表。
def a8_function(a):
    a8_List=[]
    if a < 1:
        print('輸入數值不可小於1')
        return
    for i in range (1,a):
        a8_List.append(i)
    print('Q8.',a8_List)
a8_function(10)

# ----------------------------------------------------------------  
# 9. 計算總和
# 輸入一個列表，計算所有數字的總和。
def a9_function(a):
    total = 0  # 一開始要先設定 total = 0
    for i in a:
        total += i  # i 就是元素，直接加
    print('Q9.',total)
a9_List = [1, 3, 5, 7, 9, 11]
a9_function(a9_List)

# ----------------------------------------------------------------
#10. 找出列表中的偶數
#輸入一個整數列表，回傳其中所有偶數組成的新列表。

def a10_function(a):
    L10 =[]
    for i in a:
        if i % 2 ==0:
           L10.append(i)
    print('Q10.',L10) 

a10_List = [11,2,6,8,9,20,36,77,1,7,99]
a10_function(a10_List)
    