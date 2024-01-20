import random


class Error(Exception):
    pass


class valueIsMoreThanExpected(Error):
    pass


class valueIsLowerThanExpected(Error):
    pass


x = []
for a in range(100):

    x.append(a)


Number = random.choice(x)
print(x)
print(Number)
while True:
    try:
        u_number = int(input('Enter your expected number : '))
        if u_number < Number:
            raise valueIsLowerThanExpected()
        elif u_number > Number:
            raise valueIsMoreThanExpected()

        break

    except valueIsMoreThanExpected:
        print('adad vared shode bishtar az adad mored nazar ast')

    except valueIsLowerThanExpected:
        print('adad vared shode kamrar az adad mored nazar ast')

print('hadsetoon dorost bud')
