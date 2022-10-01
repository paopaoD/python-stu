"""
    面向对象
"""


class Epidemics:
    def __init__(self, region="", now=0, total=0, cure=0):
        self.region = region
        self.now = now
        self.total = total
        self.cure = cure
"""
练一练：请指出下列代码的错误
tai_wan = ("台湾省", 4523061, 4545636, 13742)# 错误:缺少类名
hong_kong = Epidemics # 错误:缺少小括号
nei_meng_gu = Epidemics("内蒙古", 2, 2166, 2163), # 错误:多逗号
"""


# 练一练：哪个参数可以实现增加疫情现有人数：
def set_now(p1, p2, p3):
    # 改变栈帧中局部变量p1,不影响全局变量
    p1 = Epidemics("台湾省", 4523062, 4545636, 13742)
    p2.now += 1
    return p3.now + 1

tai_wan = Epidemics("台湾省", 4523061, 4545636, 13742)
hong_kong = Epidemics("香港", 277529, 354454, 67427)
nei_meng_gu = Epidemics("内蒙古", 2, 2166, 2163)
set_now(tai_wan, hong_kong, nei_meng_gu)
print(tai_wan.__dict__)
print(hong_kong.__dict__)
print(nei_meng_gu.__dict__)

# 1. 类和对象内存分布
class Computer:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price


huawei = Computer("华为", 4799)
print(huawei.brand)
print(huawei.price)

"""
    2. 软件架构设计思想
        封装：分而治之、变则疏之
        继承：抽象变化、统一行为
        多态：编码调父、运行用子
"""

# 方案1：
class Computer:
    """电脑"""

    def connect(self, device):
        """连接麦克风"""
        if type(device) == Microphone:
            device.record()
        elif type(device) == Camera:
            device.video()
        # elif 类型是手机:
        #     调用通话方法


class Microphone:
    """麦克风"""

    def record(self):
        print("录音")


class Camera:
    """摄像头"""

    def video(self):
        print("拍摄")


huawei = Computer()
huawei.connect(Microphone())
huawei.connect(Camera())


# -----------------------------------------------------------
# 方案2：将来连接其他设备时电脑不变
class Computer:
    """电脑"""

    def connect(self, device):
        """连接设备"""
        # 编码时调用父，运行时执行子
        if isinstance(device, Device):
            device.usb()


class Device:
    def usb(self):
        """电脑与外部设备连接的规范"""
        pass


class Microphone(Device):
    def usb(self):
        print("连接麦克风")


class Camera(Device):
    def usb(self):
        print("连接摄像头")


huawei = Computer()
huawei.connect(Microphone())
huawei.connect(Camera())
huawei.connect("手机")


# -----------------------------------------------------------
# 方案3：电脑可以连接多个设备
class Computer:
    """电脑"""

    def connect(self, *devices):
        """连接多个设备"""
        for item in devices:
            if isinstance(item, Device):
                item.usb()


class Device:
    def usb(self):
        """电脑与外部设备连接的规范"""
        pass


class Microphone(Device):
    def usb(self):
        print("连接麦克风")


class Camera(Device):
    def usb(self):
        print("连接摄像头")


huawei = Computer()
huawei.connect(Microphone(), Camera())
