# 圖形產生練習

# # 題目 1：直角三角形

def a1():
    n = int(input("請輸入三角形的行數："))
    for i in range(1, n + 1): #從n ~ 1
        print('*' * i)
# a1()
# ---------------------------------------------

# # 題目 2：倒直角三角形

def a2():
    n = int(input("請輸入倒三角形的行數："))
    for i in range(n, 0, -1):  # 從 n 倒數到 1
        print('*' * i)
# a2()

# ---------------------------------------------

# # 題目 3：等腰三角形

def a3():
    n = int(input("請輸入等腰三角形的行數："))
    for i in range(1, n + 1):
        space = ' ' * (n - i)        # 左邊空格，越高行空格越多
        stars = '*' * (2 * i - 1)    # 星星數量 = 2*i - 1
        print(space + stars)
# a3()
# ---------------------------------------------

# 題目 4：等腰倒三角形

def a4():
    n = int(input("請輸入等腰三角形的行數："))
    for i in range(n, 0, -1):
        space = ' ' * (n - i)        # 左邊空格，越高行空格越多
        stars = '*' * (2 * i - 1)    # 星星數量 = 2*i - 1
        print(space + stars)
# a4() 
 
# ---------------------------------------------

# 題目 5：菱形圖形
# 請印出一個 n 層的菱形（n 為奇數）。


#做出上半部

def a5_top(n_top):
    for i in range(1,n_top+1):
        space = (n_top - i) * ' '
        star = (2*i-1) * '*'
        print(space+star)

#做出下半部

def a5_down(n_down):
    for i in range (n_down, 0, -1):
        space = (n_down - i+1) * ' '
        star = (2*i-1) * '*'
        print(space+star)
        
#合體
def a5():
    n = int(input("請輸入菱形行數(需為奇數):"))
    n_top = int(n/2+1)
    n_down = int(n/2)
    a5_top(n_top)
    a5_down(n_down)

# a5()

# ---------------------------------------------

# 題目 6：邊框矩形

def a6():
    x = int(input("請輸入矩形邊框數(高):"))
    y = int(input("請輸入矩形邊框數(長):"))
    
    for i in range(0, x):
        if x < 2 or y < 2:
            print("邊框高與長至少需為 2")
            return
        
        if i==0 or i ==(x-1):
            print('*' * y)
        else:
            print ('*' * 1 + ' ' * (y-2) + '*' * 1)
        
a6()