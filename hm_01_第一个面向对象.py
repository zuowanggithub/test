class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")

# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print("%d" % addr)  #更新一下
