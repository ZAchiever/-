
class Car(object):
    """car的基类
    """
    def __init__(self, id, driver):
        self.driver = driver  # 长度为二的set
        self.weight = 0
        self.amount_finished = 0
        self.amount_raw = 0
        self.empty_cost = 0
        self.full_cost = 0
        self.id = id  # 编号
        self.working = False  # 是否在工作

    def aa(self):
        print(self.weight)


class CarA(Car):
    """A车的基本信息重写
    """
    def __init__(self, id, driver):
        super().__init__(id, driver)
        self.driver = driver  # 长度为二的set
        self.weight = 8
        self.amount_finished = 550
        self.amount_raw = 720
        self.empty_cost = 25
        self.full_cost = 30
        self.id = id  # 编号
        self.working = False  # 是否在工作


class CarB(Car):
    """B车的基本信息重写
    """
    def __init__(self, id, driver):
        super().__init__(id, driver)
        self.driver = driver  # 长度为二的set
        self.weight = 5
        self.amount_finished = 450
        self.amount_raw = 600
        self.empty_cost = 20
        self.full_cost = 25
        self.id = id  # 编号
        self.working = False  # 是否在工作


class CarC(Car):
    """c车的基本信息重写
    """
    def __init__(self, id, driver):
        super().__init__(id, driver)
        self.driver = driver  # 长度为二的set
        self.weight = 10
        self.amount_finished = 300
        self.amount_raw = 400
        self.empty_cost = 15
        self.full_cost = 20
        self.id = id  # 编号
        self.working = False  # 是否在工作