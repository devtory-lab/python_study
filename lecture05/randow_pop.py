import random


def random_pop(data):
    num = random.randint(0, len(data) - 1)
    return data.pop(num)

def random_choice(data):
    num = random.choice(data)
    data.remove(num)
    return num

if __name__ == "__main__":
    data = [1,2,3,4,5]
    data2 = [6,7,8,9,10]
    data3 = [11,12,13,14,15]
    while data:
        print(random_pop(data))

    print("============dddd==============")

    while data2:
        print(random_choice(data2))

    print("============dddd==============")

    random.shuffle(data3)
    print(data3)

# webbrowser : webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다. 다음 예제는 웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 가게 해 준다.
import webbrowser

webbrowser.open("google.com")
webbrowser.open_new("naver.com")