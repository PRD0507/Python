from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def size(self):
        return len(self.container)

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def isEmpty(self):
        return len(self.container) == 0

    def top_of_stack(self):
        return self.container[len(self.container) - 1]

    def reverse(self, str):
        for i in str:
            self.container.append(i)

        reverse_str = ''
        while self.isEmpty() == 0:
            reverse_str += self.container.pop()

        return reverse_str

    def balanced_paranthsis(self, str):
        match_dict = {')': '(',
                      '}': '{',
                      ']': '['}
        flag = 1

        if str[0] == '}' or str[0] == ')' or str[0] == ']':
            flag = 0

        else:
            for i in str:
                if i == '(' or i == '{' or i == '[':
                    self.container.append(i)

                if i == '}' or i == ')' or i == ']':
                    if match_dict[i] == self.top_of_stack():
                        self.container.pop()
                    else:
                        flag = 0

        if flag == True:
            print("Balanced Paranthesis")

        else:
            print("unbalanced paranthesis")


if __name__ == '__main__':
    stack = Stack()

    # str = "We will conquere COVID-19"
    # reverse_str = stack.reverse(str)

    str = "))"

    stack.balanced_paranthsis(str)