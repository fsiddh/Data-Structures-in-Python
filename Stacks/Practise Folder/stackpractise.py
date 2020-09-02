class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next=None):
        self._element = element
        self._next = next


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

        self._postfix = list()
        self._operators = ['*', '/', '%', '-', '+']

    def len(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, element):
        newest = _Node(element)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1
    
    def pop(self):
        if self.isempty():
            print('Your stack is empty')
            return 
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def priority(self, operator):
        if operator == '*' or operator == '/' or operator == '%':
            return 1
        else:
            return 0
                
    def itp(self, phrase):
        p = self._top

        for character in phrase:
            if character == '(':  # Left Parenthesis
                self.push(character)
            elif character == ')':  # Right Parenthesis
                p = self._top
                while p:
                    e = p._element
                    p = p._next
                    if e == ')':
                        return 
                    self._postfix.append(e)
                    
            elif character in self._operators:  # OPERATORS
                if self.isempty():
                    self.push(character)
                elif self._top._element not in self._operators:
                    self.push(character)
                else:
                    if self.priority(character) > self.priority(self._top._element):
                        self.push(character)
                    else:
                        e = self.pop()
                        self._postfix.append(e)                            
            else:  # OPERANDS
                self._postfix.append(character)

        # To empty stack
        temp = self._top
        while temp:
            e = self.pop()
            self._postfix.append(e)
            temp = temp._next
        
    def show_postfix(self):
        result = ''.join(self._postfix)
        print(result)

    def top(self):
        if self.isempty():
            print('Stack empty')
            return 
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element)
            p = p._next
        print() 

    

if __name__ == '__main__':
    S = Stack()

    # S.push('A+B')
    # S.display()

    S.itp('A+B')
    S.show_postfix()
