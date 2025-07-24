
class A:
    # 題目 1：成績總結器
    # ------------------------------------------------------------------
    # 功能： 給一串學生成績，印出平均、最高、最低。
    def score_cal():
        scores = [88, 73, 92, 85, 91]
        sum = 0
        count = len(scores)
        MAX = scores[0]
        MIN = scores[0]
    
        for i in scores: 
            sum += i
            avg = float(sum / count) # 平均
            
            if(i > MAX): # 最大
                MAX = i
            
            if(i < MIN): # 最小
                MIN = i
            
        print('平均值 : '+ str(avg))
        print('最大值 : '+ str(MAX))
        print('最小值 : '+ str(MIN))
        
        
    #score_cal()

    # 題目 2
    # ------------------------------------------------------------------
    # 題目 2：學生成績分析器
    # 🎯 題目說明：
    # ✅ 要完成的功能：
    # 印出平均分數（取小數點後 1 位）
    # 印出最高分與該學生的名字（可能有多人）
    # 印出低於 60 分（不及格）的學生列表（名字＋分數）
    # 列出所有學生的成績由高到低排序
    # 加分題：印出每個學生與他在班上的排名（並列不拆開）

    def analyst_score():
        scores = {
            "Ann": 88,
            "Ben": 73,
            "Charlie": 92,
            "Daisy": 85,
            "Eva": 91,
            "Alan": 92,
            "Alex": 92,
            "CJ": 61,
            "Dan": 57,
            "Bob": 43,
            "Ginger": 49,
            "Ian": 87
        }

        total = 0
        Max = list(scores.values())[0] 
        Min = list(scores.values())[0]
        aMax = []
        aMin = []
        under60 = []

        for name, score in scores.items():
            total += score

            if score > Max:
                Max = score
            if score < Min:
                Min = score
            if score < 60:
                under60.append(name)

        avg = total / len(scores)

        for name, score in scores.items():
            if score == Max:
                aMax.append(name)
            if score == Min:
                aMin.append(name)

        print('平均分數:', round(avg, 1))
        print('最高分:', Max, '，得分學生:', aMax)
        print('最低分:', Min, '，得分學生:', aMin)
        print('低於60分的學生:', under60)
        print('-----------------------------------------------------')
        print('分數由低到高排序：')

        # 延伸：將 (名字, 分數) 存入 list，再排序（這樣同分也能顯示正確）
        sorted_list = []

        for name, score in scores.items():
            sorted_list.append([score, name])  # 把分數放前面，方便 sort
        
        sorted_list.sort()  # 預設由小排到大

        for score, name in sorted_list:
            print(name, ":", score)

    #analyst_score()
 
class B:
    # 題目 3
    # ------------------------------------------------------------------

    # 題目 1：找出成績區間的人數
    # 📌 請列出以下幾個分數區間中，各有幾位學生：
    # 90 分以上
    # 80～89 分
    # 70～79 分
    # 60～69 分
    # 60 分以下

    # 題目 2：找出名字最長 & 最短的學生
    # 請找出：
    # 名字最長的學生（如 Charlie）
    # 名字最短的學生（如 Ben）
    # 順便列出他們的成績。

    # 題目 3：找出分數排名第 2 名的所有人
    # 有時候第一名很多人，第二名也可能很多人。
    # 請找出所有「第二高分」的學生姓名與分數。

    # 題目 4（挑戰）：印出所有人名和成績，依照「名字長度」由短到長排序
    
    
    
    def __init__(self):
        self.students = {
            "Ann": 88,
            "Ben": 73,
            "Charlie": 92,
            "Daisy": 85,
            "Eva": 91,
            "Alan": 92,
            "CJ": 61,
            "Dan": 57,
            "Bob": 43,
            "Ginger": 49,
            "Ian": 91
        }
    
    def score(self):
        ans1 = {
            "90分以上":0 , 
            "80～89 分":0, 
            "70～79 分":0, 
            "60～69 分":0, 
            "60 分以下":0
        }
        
        for  score in self.students.values():
            if score >= 90:
                ans1["90分以上"] += 1
            if score >= 80 and score <=90:
                ans1["80～89 分"] += 1
            if score >= 70 and score <=80:
                ans1["70～79 分"] += 1
            if score >= 60 and score <=70:
                ans1["60～69 分"] += 1
            if score <= 60 :
                ans1["60 分以下"] += 1
        
        for k, v in ans1.items():
            print(f"{k}：{v} 人")
    
    def compare_name(self):
        # dic 要取位置通常是轉乘list再去做選取
        keys_list = list(self.students.keys())
        max_name = keys_list[0]
        min_name = keys_list[0]
        
        for name in self.students.keys():
            if len(name) > len(max_name):
                max_name = name
            if len(name) < len(min_name):
                min_name = name
                  
        print("名字最長:"+max_name)
        print("名字最短:"+min_name)
            
    def second_top_score(self):
        scores = list(self.students.values())
        scores.sort(reverse=True)  # 從大排到小
        first = scores[0]
        
        # 找第一個不是最高分的分數
        for score in scores:
            if score < first:
                second = score
                break
        else:
            print("沒有第二高分")
            return

        # 找出所有分數等於 second 的學生
        print("第二高分:", second)
        for name, score in self.students.items():
            if score == second:
                print("學生:", name)
            
    def sort_all(self):
        all_students = list(self.students.items())    
        all_students.sort(key=lambda x: len(x[0]), reverse=True)

        print (all_students)
        #print(type(all))    
   
class C:
    def __init__(self):
        # 給定一個字典，代表每個人喜歡的水果
        # 請找出哪個水果是最多人選的

        self.favorites = {
            "Ann": "apple",
            "Ben": "banana",
            "Charlie": "apple",
            "Daisy": "mango",
            "Eva": "banana",
            "Alan": "apple",
            "CJ": "banana"
        }

    # 預期輸出：最多人喜歡的是 "apple"（或 "banana"），出現 3 次
    def cnt_fruit(self):
        fruit_list = list(self.favorites.values())
        counts = {}  # key:水果名稱, value:次數

        for f in fruit_list:
            if f in counts:
                counts[f] += 1
            else:
                counts[f] = 1

        # 找出出現次數最多的水果和數量
        max_count = max(counts.values())
        most_common_fruits = [k for k, v in counts.items() if v == max_count]

        print("最多人喜歡的水果：", most_common_fruits)
        print("出現次數：", max_count)
        
    # 使用者輸入一個水果名，列出喜歡的人有哪些
    def input_fruit(self):
        question = input("請輸入水果名 : ")
        fruit_name=[]
        for name, fruit in self.favorites.items():
            if fruit == question:
               fruit_name.append(name)
        if True :
            print("目前喜歡 "+question+" 共有 "+str(len(fruit_name))+" 人")
              
    # 每種水果對應喜歡的人名清單（反轉字典）
    def reverse_list(self):
        reverse_f = list(self.favorites.items())
        ans ={}
        for name , fruit in reverse_f:
            if fruit not in ans:
                ans[fruit] = []
            ans[fruit].append(name)
            
        print(ans)
        
    # 判斷是否有多人喜歡的水果完全一樣
    def same_fruit(self):
        fr = list(self.favorites.items())
        temp = {}
        for name , fruit in fr:
            if fruit not in temp:
                temp[fruit] = []
            temp[fruit].append(name)
        for f , n in temp.items():
            if len(n) >= 2:
                print(f + '共有' + str(len(n)) +'人喜歡，分別是'+str(n))

class D:
       
    def __init__(self):
        # 初始信件資料，每封信是 sender: subject
        self.mails = {
            "Ann": "請假單 - 人資部",
            "Ben": "專案報告 - 技術部",
            "Charlie": "新品上市提案 - 行銷部",
            "Daisy": "午餐表單 - 人資部",
            "Eva": "產品優化報告 - 技術部",
            "Alan": "新年活動構想 - 行銷部",
            "CJ": "內部講座邀請 - 技術部"
        }
    
    # 將信件依照部門分類
    def mail_group(self):
        group = list(self.mails.items())
        mail_g ={}
        
        for k,v in group :
            department = v.split(" - ")[1] #透過split去做分割，他這樣會變成兩段，取編號1的那段
            title = v.split(" - ")[0]
            if department not in mail_g:
                mail_g[department] = []
            mail_g[department].append(title)
         
        temp_mail_g = list(mail_g.items())
        for k , v in temp_mail_g:
            print('部門:'+k)
            
            for i in v:
                print('信件標題:'+i)
            
            print('-----------------')
        
    # 找出來自技術部的信件
    def search_tech(self):
        st = list(self.mails.items())
        for k , v in st:
            if '技術部' in v:
                print(k+' : '+v)
                
    # 統計每個部門的信件數量
    def mail_num(self):
        st = list(self.mails.items())
        stt ={} # 部門 / 信件標題
        for k , v in st:
            dep = v.split(' - ')[1]
            mail_title = v.split(' - ')[0]
            if dep not in stt:
                stt[dep] = []
            stt[dep].append(mail_title)
        for dep, titles in stt.items():
            print(dep + ' : ' + str(len(titles)))
        
        
if __name__ == "__main__":
    a = A()
    
    b = B()
    # b.score()  
    # b.compare_name()
    # b.second_top_score()
    # b.sort_all()

    c = C()
    # c.cnt_fruit()
    # c.input_fruit()
    # c.reverse_list()
    # c.same_fruit()
    
    d = D()
    # d.mail_group()
    # d.search_tech()
    d.mail_num()