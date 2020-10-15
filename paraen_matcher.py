from stack import Stack


def par_checker(symbolString):
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = str(s.pop())
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)


if __name__ == '__main__':
    print(par_checker('{{([][])}()}'))
    print(par_checker('[{()]'))
