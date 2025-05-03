from a1.message_formatter import decor1, decor2


@decor2
@decor1
def get_name():

    name = input("Enter Your Name:")

    return name


print(get_name())
