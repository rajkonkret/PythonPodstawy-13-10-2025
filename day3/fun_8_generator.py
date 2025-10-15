# generator - dane na żądanie
# lazy - dane tylko kiedy potrzebne
import time


def kwadrat(x):
    for i in range(x):  # od 0 do x - 1 (od 0 do 4)
        print(i ** 2)


kwadrat(5)


def kwadrat2(x):
    for i in range(x):
        yield i ** 2  # zwraca wartośc, zapamiętuje gdzie zakończył


# print(kwadrat2(5)) # <generator object kwadrat2 at 0x00000168737B8FB0>
kwa = kwadrat2(5)
print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4
print(next(kwa))  # 9
print(next(kwa))  # 16
# print(next(kwa))  # StopIteration - generator wyczerpal dane

for i in kwadrat2(5):
    print(i)
    time.sleep(1)  # symulacja długotrwalego zadania, stop na 1 sekundę
