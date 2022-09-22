# Balance Fair

def balance_pair(brackets: str) -> bool:
    # if brackets.strip() == "" or len(brackets) % 2 == 1:
    if not brackets or len(brackets) % 2 == 1:
        return False
    person: list = []
    for bracket in brackets:
        if bracket in "{[(":
            person.append(bracket)
        elif bracket in "}])":
            peek: str = person[-1]
            if peek == "{" and bracket == "}":
                person.pop()
            elif peek == "[" and bracket == "]":
                person.pop()
            elif peek == "(" and bracket == ")":
                person.pop()
            # pass  # you can use pass keyword or eclipse ...
            else:
                return False
        else:
            return False
    return True


print(balance_pair("[{}]"))


def two_digit(number: list, target: int) -> list:
    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            if number[i] + number[j] == target:
                return [i, j]
    return [-1, -1]


print(two_digit([22, 4, 6, 9, 8, 7], 29))