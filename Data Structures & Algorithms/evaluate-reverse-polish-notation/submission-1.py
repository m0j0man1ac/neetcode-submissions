class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'*', '+', '/', '-'}
        stack = []

        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(Solution.evaluate(t, a, b))
                continue

            stack.append(t)

        #print(stack)
        return int(stack[-1])

    @staticmethod
    def evaluate(t: str, a: str, b:str) -> int:
        a = int(a)
        b = int(b)

        match t:
            case "*":
                return a * b
            case "/":
                return a / b
            case "+":
                return a + b
            case "-":
                return a - b

        #shouldnt reach here
        return a + b
