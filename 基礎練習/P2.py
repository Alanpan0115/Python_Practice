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

import math

def a9_function(a):
    L99 = []
    for i in a:
        if i <= 1:
            continue
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):  # 只需要檢查到平方根
            if i % j == 0:
                is_prime = False
                break  # 如果能整除，則不是質數
        if is_prime:
            L99.append(i)
    print('Q9', L99)

L9 = [2, 5, 9, 3, 6, 7, 11, 12, 17]
a9_function(L9)

# ----------------------------------------------------------------
# 10. 數字倒數
# 寫一個函式，輸入一個正整數 n，從 n 倒數到 1，每個數字都印出來。

def a10_function(a):
    print('Q10', end=" ")
    for i in range(a,0,-1):
        print(i, end=" ")  # 不換行，後面加空格
a10_function(23)
print()
# range(start, stop, step)
# start: 從哪裡開始（包含）
# stop: 到哪裡停止（不包含 stop）
# step: 每次走幾步，正數是遞增，負數是遞減

# ----------------------------------------------------------------
# 11. 擷取檔案副檔名
# 輸入一個檔案名稱字串（例如 "report.docx"），回傳副檔名（例如 "docx"）。
import os
def a11_function(a):
    name , ext = os.path.splitext(a)
    if ext:
        print('Q11. 附檔名為',ext[1:])
    else:
        print('Q11. 沒有附檔名')
a11_filename='test.docx'    
a11_function(a11_filename)
# ----------------------------------------------------------------
# 12. 將句子中的單字反轉
# 輸入一個英文句子，把每個單字反轉，但單字順序不變。
# 例如："Hello World" ➜ "olleH dlroW"
def a12_function(a12_str):
    # 使用 split() 以空白分割句子
    words = a12_str.split() # 這邊會變成 [Hello , World , !!!]
    result = []

    for word in words:
        reversed_word = word[::-1]  # 反轉單字
        result.append(reversed_word)

    print("Q12. 反轉結果：", " ".join(result))

# 測試
a12_str = "Hello World !!!"
a12_function(a12_str)


# ----------------------------------------------------------------
# 13. 合併兩個列表並移除重複值
# 給定兩個列表，合併它們並移除所有重複的元素，回傳新列表。
def a13_function(a,b):
    a13_addlist = a + b
    a13_ans =[]
    for i in a13_addlist:
        if i in a13_ans:
            continue
        else:
            a13_ans.append(i)
    print('Q13.',a13_ans)
a13_1 =['apple','banana','cake','dog']
a13_2 =['address','black','cake','dog']
a13_function(a13_1,a13_2)

# ----------------------------------------------------------------
# 14. 統計句子中的單字數量
# 輸入一句英文句子，回傳每個單字出現的次數（使用字典）。
def a14_function(a):
    a14_word = a.split()
    a14_list = {}
    for i in a14_word:
        if i.isdigit() in a14_list:
            a14_list[i]+=1
        else :
            a14_list[i]=1
    print('Q14.',a14_list)
    
a14_sentence = "My name is alan , I'm from Taipei Taiwan . I graduate form Cheng Young University. My job title is software engineer."
a14_function(a14_sentence)

# ----------------------------------------------------------------
# 15. 印出等腰三角形星星圖案
# 輸入一個整數 n，印出 n 層高的等腰星星三角形。

# 靠左三角形
print('Q15.')
print('靠左三角形')
def a15_function(a):
    for i in range (0,a) :
        for j in range(0,i):
            print('*',end='')
        print()
a15_function(10)

# 靠左顛倒三角形
print('靠左顛倒三角形')
def a15_function_1(a):
    for i in range (a,0,-1) :
        for j in range(0,i):
            print('*',end='')
        print()
a15_function_1(10)

# 靠右三角形
print('靠右三角形')
def a15_function_2(a):
    for i in range (a,0,-1) :
        spaces = a-i
        print(' ' * spaces + '*' * i)
a15_function_2(10)

# 靠右顛倒三角形
print('靠右顛倒三角形')
def a15_function_3(a):
    for i in range (0,a) :
        spaces = a-i
        print(' ' * spaces + '*' * i)
a15_function_3(10)

# 等腰三角形
print('等腰三角形')
def a15_function_4(a):
    for i in range (0,a) :
        spaces = a-i
        stars = 2 * i - 1
        print(' ' * spaces + '*' * stars)
a15_function_4(10)
# ----------------------------------------------------------------
# 16. 計算階乘
# 輸入一個正整數 n，計算 n!（例如：5! = 5×4×3×2×1）

# ----------------------------------------------------------------
# 17. 計算列表中的偶數總和
# 輸入一個整數列表，計算所有偶數的加總。

# ----------------------------------------------------------------
# 18. 萃取清單中大於平均值的數字
# 輸入一串整數，回傳高於平均值的所有數字（可用列表）。

# ----------------------------------------------------------------

# ----------------------------------------------------------------

# ----------------------------------------------------------------

# ----------------------------------------------------------------

# ----------------------------------------------------------------

# ----------------------------------------------------------------