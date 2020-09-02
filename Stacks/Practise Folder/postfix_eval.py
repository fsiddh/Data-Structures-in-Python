from test_linkedstack import StacksLinked 

class PostfixEval:
    def __init__(self):
        self._S = StacksLinked()
    
    def evaluation(self, expression):
        for c in expression:
            if c.isalnum():
                self._S.push(int(c))
            else:
                first_pop = self._S.pop()
                second_pop = self._S.pop()
                
                if c == '*':
                    print('{} * {} = {}'.format(second_pop, first_pop, second_pop * first_pop))
                    self._S.push(second_pop * first_pop)
                elif c == '/':
                    print('{} / {} = {}'.format(second_pop, first_pop, second_pop / first_pop))
                    self._S.push(second_pop / first_pop)
                elif c == '%':
                    print('{} % {} = {}'.format(second_pop, first_pop, second_pop % first_pop))
                    self._S.push(second_pop % first_pop)
                elif c == '+':
                    print('{} + {} = {}'.format(second_pop, first_pop, second_pop + first_pop))
                    self._S.push(second_pop + first_pop)
                elif c == '-':
                    print('{} - {} = {}'.format(second_pop, first_pop, second_pop - first_pop))
                    self._S.push(second_pop - first_pop)


if __name__ == '__main__':
    P = PostfixEval()

    P.evaluation('562*+')
    x = P._S._top._element
    print('Postfix Evaluation: {}'.format(x))
    
    
