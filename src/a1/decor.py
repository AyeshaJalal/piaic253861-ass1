def decor1(ff):
    def inner():
        print("☀️☀️☀️✨✨✨🧨🧨🧨")
        return ff().upper()

    return inner


def decor2(f):
    def inner():
        # print(f)
        return print(f().split())

    return inner


@decor2
@decor1
def get_name():
    name = input("Enter Your Name:")
    name = name + "   Welcome   " + "🎉🎉🎉"

    return name


print(get_name())
