import random


def bigthree():
    data = list()
    for i in range(10):
        data.append(random.randint(0, 100))
    print(data)
    sdata = sorted(data)
    return min(sdata[-3:])


if __name__ == '__main__':
    print(bigthree())