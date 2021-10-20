from abc import ABCMeta, abstractmethod


"""接口"""
"""报错误，不了接受关键字参数"""
# class Payment(metclass=ABCMeta):  # abstract class
#     @abstractmethod
#     def pay(self, money):
#         pass

class Payment:  # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print('支付宝支付%d元。' % money)


class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d元。' % money)


p = Alipay()
p.pay(100)
