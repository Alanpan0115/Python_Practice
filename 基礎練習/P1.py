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
    
# ----------------------------------------------------------------  
# 11. 英文字母計數
# 輸入一個字串，統計裡面英文字母 (a-z, A-Z) 出現了幾次。（忽略其他符號）

def a11_function(a):
    a11_dic={}
    for i in a:
        if i.isalpha(): # 只統計英文字母
            if i in a11_dic:
                a11_dic[i]+=1
            else:
                a11_dic[i]=1
    print('Q11. ',end='')
    print(a11_dic)
a11 = 'af1a1f5a13fasd2svd,oqmd1ojfiamdamvjmflamcladd5w4d8a1315vefiaj,d'
a11_function(a11)
    
# ----------------------------------------------------------------  
# 12. 檢查兩個字串是否為「異位詞」
# 兩個字串如果重新排列後一樣，叫異位詞（anagram），寫一個函式來檢查。
# （例："listen" 和 "silent" 是異位詞）

def a12_function(a,b):
    a_dic={}
    b_dic={}
    for i in a:
        if i.isalpha(): # 只統計英文字母
            if i in a_dic:
                a_dic[i]+=1
            else:
                a_dic[i]=1
    for i in b:
        if i.isalpha(): # 只統計英文字母
            if i in b_dic:
                b_dic[i]+=1
            else:
                b_dic[i]=1
    if a_dic == b_dic:
        print('Q12. a、b是異位詞')
    else:
        print('Q12. a、b並非異位詞')

    # 直接分類後比較最快        
    # if sorted(a) == sorted(b):
    #     print('Q12. a、b是異位詞')
    # else:
    #     print('Q12. a、b並非異位詞')
a= 'listen' 
b= 'silent'
a12_function(a,b)

# ----------------------------------------------------------------  
# 13. 移除列表中的重複元素
# 寫一個函式，輸入一個列表，回傳一個移除重複元素的新列表。
# （提示：可以用 set() 或自己寫迴圈）

def a13_function(a):
    a13 =[]
    for i in a :
        if i not in a13:
            a13.append(i)
    print('Q13.',a13)
a13_list = [1,2,53,8,1,3,94,13,2,15,46,1,68,144,2,62,42,663,74,22,61,144,216,46,8,53,11]
a13_function(a13_list)

# ----------------------------------------------------------------  
# 14. 找列表中的第二大數字
# 輸入一個數字列表，找出「第二大」的數字。
# （例：[10,20,30,40] → 第二大是 30）
    
def a14_function(a):
    a = sorted(a, reverse=True)  # 直接從大排到小
    print('Q14.', a[1])  # 取第2個就是第二大
a14 = [10, 25, 36, 51, 20, 7, 19]
a14_function(a14)


# ----------------------------------------------------------------  
# 15.判斷列表是否為遞增
# 寫一個函式，檢查一個數字列表是不是從小到大排列的。
# （例：[1,3,5,7] → 是；[5,3,2] → 否）

def a15_function(a):
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:  # 如果當前值小於或等於前一個，就不是遞增
            print('Q15. 否')
            return
    print('Q15. 是')  # 如果整個for迴圈都沒問題，就是遞增

a15 = [1, 3, 5, 7]      # ✅ 是
a15_function(a15)

# a15 = [1, 8, 2, 6, 3]   # ❌ 否
# a15_function(a15)

# ----------------------------------------------------------------  
# 16. 判斷年份是否為閏年
# 輸入一個年份，判斷它是不是閏年。（閏年的規則是：能被4整除但不能被100整除，或者能被400整除）

def a16_function(a):
    if (a%4 ==0 and a%100!=0) or a%400==0:
        print('Q16.',a,'為閏年')
    else:
        print('Q16.',a,'不為閏年')
a16_function(2020)

# ----------------------------------------------------------------  
# 17. 將字串每個字母後移一位
# 輸入一個字串，把每個英文字母往後移動一位（z變成a）。
# （例："abc" → "bcd"，"xyz" → "yza"）
def a17_function(a):
    result = ''
    for ch in a:
        if ch.isalpha():  # 只處理英文字母
            if ch == 'z':
                result += 'a'
            elif ch == 'Z':
                result += 'A'
            else:
                result += chr(ord(ch) + 1)
        else:
            result += ch  # 其他符號照原樣保留
    print('Q17.', result)

a17_function('abc')      # Q17. bcd
a17_function('xyzXYZ')   # Q17. yzaYZA
a17_function('hello!')   # Q17. ifmmp!

# ----------------------------------------------------------------  
# 18. 檢查字串是否為數字
# 寫一個函式，檢查字串是否完全由數字組成。
# （例如："1234" 是數字；"abc123" 不是）
def a18_function(a):
    if a.isdigit():
        print('Q18. 是')
    else:
        print('Q18. 不是')

a18 = 'afa1f3a1f31f3a13a'    
a18_function(a18)


