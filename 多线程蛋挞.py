'''
任务：三个厨师同时造蛋挞，每造一个，放入到篮子里。
    如果篮子满了，等待3秒。判断是否已满
    蛋挞的篮子：500个
    每个人手里都有3000元，每个蛋挞2元。
    开始卖蛋挞，当篮子蛋挞不够，等待2秒，一直到钱花光为止

'''
from threading import Thread
#500个蛋挞
bread=0
import time
class cook(Thread):
   username=""   #厨师名
   count=0   #蛋挞的数量
   def run(self) -> None:
       global bread
       while True:
          if bread<500:
             bread=bread+1
             self.count=self.count+1
             print(self.username,"总共做了",self.count,"个蛋挞")

          elif bread==500:
              time.sleep(3)

class customer(Thread):
    username=""
    count=0
    def run(self) -> None:
        money =3000
        global bread
        while True:
            if money>0:
                bread=bread-1
                money=money-2
                self.count=self.count+1
                print(self.username,"总共买了",self.count,"个蛋挞")
            elif money<0:
                print("余额不足！！")
                break

c1=cook()
c2=cook()
c3=cook()
c1.username = "张三"
c2.username = "李四"
c3.username = "王五"

c1.start()
c2.start()
c3.start()

k1=customer()
k2=customer()
k3=customer()
k4=customer()
k5=customer()
k6=customer()

k1.username="一号"
k2.username="二号"
k3.username="三号"
k4.username="四号"
k5.username="五号"
k6.username="六号"

k1.start()
k2.start()
k3.start()
k4.start()
k5.start()
k6.start()








