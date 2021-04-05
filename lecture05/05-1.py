result = 0


def add(num):
    global result
    result += num
    return result


print(add(3))
print(add(4))
print("=============")


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal1.sub(2))
print("===============")


class Cookie2:
    pass


a = Cookie2()
b = Cookie2()
print(a, b)
print(type(a), type(b))
print("===============")


class Cookie:
    def setdata(self, first, second):
        self.first = first
        self.second = second

        print(self.first)
        print(self.second)

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = Cookie()
b = Cookie()
a.setdata(2, 3)
b.setdata(6, 3)
print(id(a.first))
print(id(b.first))
print(a.add(), b.add())
print(a.sub(), b.sub())
print(a.mul(), b.mul())
print(a.div(), b.div())


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal(3, 4)
b = FourCal(6, 5)
print(a.add(), b.sub())


# inherit
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())


# add
class MoreFourCal2(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result



a = MoreFourCal2(4, 4)
print(a.pow())
print("=================")

# a = FourCal(4, 0)
# a.div()         #error

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = SafeFourCal(4, 0)
print(a.div())
print("=======================")

class Family:
    lastname = "kim"

print(Family.lastname)
id(Family.lastname)

Family.lastname = "park"
print(Family.lastname)
print(id(Family.lastname))

a = Family()
b = Family()
print(id(a.lastname))
print(id(b.lastname))