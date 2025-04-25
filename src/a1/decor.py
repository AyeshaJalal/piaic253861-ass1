def decor(f):
    def wrapper():
        print("****************")
        f()
        print("****************")

    return wrapper


@decor
def msg():
    print("✨🎀🎉Hello, World!🎉🎀✨")


msg()
