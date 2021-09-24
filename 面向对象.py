'''
    面向过程：
        c,c++,c#,汇编

    面向对象：
        纯面向对象：java（詹姆斯.高斯林）: sun（绿色）
            c,c++,c#
             --> oak -->  java(爪哇岛)
    如何创建一个对象？
        图纸 -->  真正的车。
    中文：
        车：
            属性(变量): 身颜色，轮胎，牌子
            行为 所具有功能（方法）: 跑，拉货
    图纸：
        class Car:
            变量当成属性
            方法当成行为
    造对象：
        变量 = 类名()

人：
    属性：
    行为：
类就是画一张图纸，蓝图。
对象就是实际能得见摸得着的东西。

1.封装
1.隐藏属性
2.setxxx,getxx用于间接赋值和取值。

'''
#水杯的图纸
class cup:
    high=0.0
    volume=""
    color=""
    texture=""

    def water(self):
        print(self.texture,"材质的水杯,可以存放",self.high,"ml的水")
c =cup()

c.color="蓝色"
c.high="921"
c.volume="816"
c.texture="304钢材"

c.water()

#笔记本电脑
class Computer():
    username=""
    __screen=0
    price=0.0
    cpu=""
    size=0
    hour=0

    def setUsername(self,username):
        self.username = username
    def getUsername(self):
        return self.username

    def setScreen(self,screen):
        if screen<0 :
            print("屏幕大小不能小于0哦！！！")
        else:
            self.__screen=screen
    def getScreen(self):
        return self.__screen

    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        return self.price

    def setCpu(self,cpu):
        self.cpu=cpu
    def getCpu(self):
        return self.cpu

    def setSize(self,size):
        self.size=size
    def getSize(self):
        return self.size

    def setHour(self,hour):
        self.hour=hour
    def getHour(self):
        return self.hour
    #打字、打游戏、看视频
    def type(self):
        print(self.username,"正在打字")

    def game(self,gamename):
        print(self.username,"正在玩",gamename)

    def watchVideo(self):
        print(self.watchVideo,"看视频")

    def showComputer(self):
        print(self.username, "买了一台",
              "屏幕大小为",self.__screen,
              "价格为￥",self.price,
              "cpu型号为",self.cpu,
              "内存大小为",self.size,
              "待机时长为",self.hour,"小时的电脑",
              )
c=Computer()

c.setUsername("佳敏子")
c.setScreen(-5)
c.setPrice(5050)
c.setCpu("i5 8265U")
c.setSize(1500)
c.setHour(2)
#
print(c.getUsername(),c.getScreen())
c.game("消消乐")
print(c.showComputer())
# c.type()













