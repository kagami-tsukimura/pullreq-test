def fizzbuzz(n):
    if not isinstance(n, int):
        raise ValueError("入力は整数でなければなりません")
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)


if __name__ == "__main__":
    fizzbuzz(100)
