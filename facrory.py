from abc import ABCMeta, abstractmethod


class Payment:  # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huaei = use_huabei

    def pay(self, money):
        if self.use_huaei:
            print("花呗支付%d" % money)
        else:
            print('支付宝余额宝支付%d元。' % money)


class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d元。' % money)


class PaymentFactory:
    def create_payment(self, mothod):
        if mothod == 'alipay':
            return Alipay()
        elif mothod == 'wechat':
            return WechatPay()
        elif mothod == 'huabei':
            return Alipay(use_huabei=True)
        else:
            raise TypeError("No such payment named %s " % mothod)


pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(99)
