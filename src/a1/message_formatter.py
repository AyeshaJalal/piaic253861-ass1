def decor1(func):
    def wrapper():
        message = func()
        return f"🎉 {message} 🎉"

    return wrapper


def decor2(func):
    def wrapper():
        message = func()
        border = "*" * len(message)
        return f"{border}\n{message}\n{border}"

    return wrapper
