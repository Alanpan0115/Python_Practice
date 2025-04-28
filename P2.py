# 1. 數字總和
# 寫一個函式，輸入一個正整數 n，回傳從 1 加到 n 的總和。
def a1_function(a):
    total = 0
    for i in range(0,a):
        total+=i
    print('Q1.',total)
a1_function(10)


# ----------------------------------------------------------------
# 2. 檢查字串是否為迴文
# 輸入一個字串，判斷是否是「回文」（從前往後、從後往前都一樣）。
# （例："level" 是回文；"python" 不是）
def a2_function(a):
    if a == a[::-1]:  # 直接拿反過來的字串比較
        print("Q2. 是回文")
    else:
        print("Q2. 不是回文")
a2_aa = 'python'
a2_function(a2_aa)

# ----------------------------------------------------------------
# 3. 列出所有偶數
# 寫一個函式，輸入一個整數 n，列出從 1 到 n 的所有偶數。

def a3_function(n):
    L3 = []
    for i in range(0,n):
        if i%2==0:
            L3.append(i)
    print('Q3,',L3)
a3_function(10)

# ----------------------------------------------------------------
# 4. 數列最大差值
# 給定一個整數列表，找出「最大值」和「最小值」之間的差。
# （例：[10, 3, 7, 20] → 最大 20，最小 3，差是 17）

def a4_function(a):
    aa=max(L4)
    bb=min(L4)
    print('Q4. 最大值和最小值差距為:',aa-bb)
L4=[5,7,63,89,12,147,5]
a4_function(L4)

# ----------------------------------------------------------------
# 5. 找出重複元素
# 給定一個列表，找出裡面所有重複出現過的元素。
# （例：[1,2,3,2,1,5] → 重複有 1 和 2）

def a5_function(a):
    a5_dic ={}
    for i in L5:
        if i in a5_dic:
            a5_dic[i]=a5_dic[i]+1
        else :
            a5_dic[i]=1
    #print('Q5.',a5_dic)
    for i in a5_dic:
        if a5_dic[i]>1:
            print('Q5.',i,'重複出現',a5_dic[i],'次')
L5=[5,7,2,7,5,1,3,4,9,5,7,6,2,3]
a5_function(L5)


# ----------------------------------------------------------------
# 6. 計算列表平均數
# 寫一個函式，輸入一個數字列表，回傳平均值（總和除以數量）。

def a6_function(a):
    total = sum(a)
    average = total / len(a)
    print('Q6.',average)
L6 = [2,8,6,9,1,3,65,7]
a6_function(L6)

# ----------------------------------------------------------------
# 7. 將列表元素平方
# 輸入一個數字列表，回傳每個元素平方後的新列表。
# （例：[1,2,3] → [1,4,9]）
def a7_function(a):
    L77 = []
    for i in L7:
        L77.append(i*i)
    print('Q7.',L77)
L7 = [1,2,3,4]
a7_function(L7)

# ----------------------------------------------------------------
# 8. 找最長字串
# 給定一個字串列表，找出最長的那個字串。
# （例：["hi", "hello", "world"] → "hello"）

def a8_function(a):
    max_length=len(a[0])
    for i in a :
        if len(i)>max_length:
            max_length=len(i)
    print('Q8. 最長字串為 :',i,'共有',max_length,'個字')
L8 = ['aaaa','bbbbb','acac','ccccccccc','ddddddddddd']
a8_function(L8)
    
# ----------------------------------------------------------------
# 9. 判斷質數列表
# 寫一個函式，輸入一個數字列表，回傳其中所有的質數（prime number）。
# （例：[2,3,4,5,6] → [2,3,5]）

def a9_function(a):
    L99 = []
    for i in a:
        if i > 1 and all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):  # 檢查是否為質數
            L99.append(i)
    print('Q9', L99)

L9 = [2, 5, 9, 3, 6, 7, 11, 12, 17]
a9_function(L9)
