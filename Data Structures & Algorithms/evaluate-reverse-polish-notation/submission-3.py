class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []

        for elem in tokens:
            # if elem is integer
            print(f"elem: {elem} is digit? {elem.isnumeric()}")
            if elem.isnumeric():
                stack.append(elem)
            elif len(elem) > 1 and '-' in elem:
                # edge case for negative numbers
                print(f"elem: {elem} is negative number, adding to stack")
                stack.append(elem)
            # else its operator
            else:
                newVal = None
                # switch case
                match elem:
                    case "+":
                        # grab 2 elements
                        val2 = int(stack.pop())
                        val1 = int(stack.pop())
                        # do operation
                        newVal = val1 + val2
                        print(f"doing operation: {val1} + {val2} = {newVal}")
                    case "-":
                        # grab 2 elements
                        val2 = int(stack.pop())
                        val1 = int(stack.pop())
                        # do operation
                        newVal = val1 - val2
                        print(f"doing operation: {val1} - {val2} = {newVal}")

                    case "*":
                        # grab 2 elements
                        val2 = int(stack.pop())
                        val1 = int(stack.pop())
                        # do operation
                        newVal = val1 * val2
                        print(f"doing operation: {val1} * {val2} = {newVal}")

                    case "/":
                        # grab 2 elements
                        val2 = int(stack.pop())
                        val1 = int(stack.pop())
                        # do operation
                        newVal = int(val1 / val2)
                        print(f"doing operation: {val1} // {val2} = {newVal}")
                
                # add new val to the stack
                stack.append(newVal)
            
        return stack.pop()
