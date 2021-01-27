
class Tool(object):
    # 类属性
    count =0
    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        # "显示工具总数"
        print("工具对象总数%d" % cls.count)

# too1 = Tool('斧头')
# tool2 = Tool('榔头')
# tool3 = Tool('铁锹')
# print("现在创建了%d 个工具"% Tool.count)
# Tool.show_tool_count()


class Dog(object):
    # 狗对象计数
    dog_count = 0

    @staticmethod
    def run():
        # 不需要访问实例属性也不需要访问类属性的方法
        print("狗在跑...")

    def __init__(self, name):
        self.name = name

Dog.run()



DrugIntroduce.objects.