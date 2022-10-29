

import unittest
import time
import uiautomation
import subprocess

class TestNotePad(unittest.TestCase):
    def setUp(self) -> None:
        # 初始化
        subprocess.Popen("notepad.exe")  # 打开记事本
        time.sleep(1)
        self.notepad = uiautomation.WindowControl(Name="无标题 - 记事本")
        time.sleep(1)
        print("===============", self.notepad)
        self.notepad.ButtonControl(Name="最大化").Click()

    def tearDown(self) -> None:
        time.sleep(1)
        self.notepad.ButtonControl(Name="关闭").Click()
        time.sleep(0.5)
        self.notepad_1 = uiautomation.WindowControl(Name = "记事本")
        self.notepad_1.SetTopmost()
        self.notepad_1.ButtonControl(Name="不保存(N)").Click()

    def test_notepad(self):
        self.notepad.SetTopmost()
        time.sleep(1)
        text_content = "人生苦短，我用Python！"
        self.notepad.EditControl(Name="文本编辑器").SendKeys(text_content)

    def test_notepad_text(self):
        self.notepad.SetTopmost()
        time.sleep(1)
        text_content_1 = ' '*47 + "Python之禅！\n\
                          优美胜于丑陋（Python 以编写优美的代码为目标）\n\
                          明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）\n\
                          简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）\n\
                          复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）\n\
                          扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）\n\
                          间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）\n\
                          可读性很重要（优美的代码是可读的）\n\
                          即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）\n\
                          不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）\n\
                          当存在多种可能，不要尝试去猜测\n\
                          而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）\n\
                          虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）\n\
                          做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）\n\
                          如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）\n\
                          命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）"
        self.notepad.EditControl(Name="文本编辑器").SendKeys(text_content_1)


if __name__ == "__main__":
    unittest.main()











