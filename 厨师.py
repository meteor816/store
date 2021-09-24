# class chef:
#     __name=""
#     __age=0
#     def setName(self,n):
#         # self.__name=name
#         self.__name=n
#     def getName(self):
#         return self.__name
#     def setAge(self,a):
#         self.__age=a
#         if a<0 or a>120:
#             print("输入非法!!!请重新输入")
#         else:
#             self.__age=a
#     def getAge(self):
#         return self.__age
#
# class vegetable(chef):
#     def fireddish(self):
#         print("年仅",self.a",self,"n","厨师正在炒菜")
#
# # c=chef()
# v=vegetable()
# v.n="二鼻子"
# v.a=16
# v.fireddish()


class person:
     age=0
     sex=""
     name=""
     def setAge(self,age):
         if age<0 or age>120:
             print("输入非法！！")
         else:
            self.age=age
     def getAge(self,age):
         return self.age

     def setSex(self,sex):
         self.sex=sex
     def getSex(self,sex):
         return self.sex

     def setName(self,name):
         self.name=name
     def getName(self):
         return self.name

class worker(person):
    def work(self):
        print("姓名为",self.name,"年龄为",self.age,"性别为",self.sex,"的工人在干活")


class student(person):
    number=""

    def learn(self):
        print("年龄为",self.age,"性别为",self.sex,"学号为",self.number,"的",self.name,"同学正在学习")
    def song(self,songname):
        print("年龄为",self.age,"性别为",self.sex,"学号为",self.number,"的",self.name,"同学正在唱",songname,"的歌曲")

w=worker()
w.setAge(32)
w.setSex("男")
w.setName("觉得金")

w.work()

s=student()
s.age=22
s.sex="男"
s.name="庄文杰"
s.number="1710014118"
s.learn()
s.song("花好月圆夜")




