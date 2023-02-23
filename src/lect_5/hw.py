class Stack:
    def __init__(self):
        self.arr = []

    def __len__(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def __str__(self):
        return str(self.arr)

    def push(self, num):
        self.arr.append(num)

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.arr[-1]

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.arr.pop()


#
# st = Stack()
# arr = [4, 0, 1, 5, 9, 8, 2]
# for item in arr:
#     st.push(item)
# print(st.__str__())
#
#
def copy_reverse(inp_stack: Stack):
    st1 = Stack()
    for i in range(inp_stack.__len__()):
        n = inp_stack.top()
        st1.push(n)
        inp_stack.pop()
    return st1


#
#
# st1 = copy_reverse(st)
#
#
# def sort_stack(inp_st: Stack):
#     tmp_st = Stack()
#     while not inp_st.is_empty():
#         tmp = inp_st.pop()
#         while not tmp_st.is_empty() and tmp_st.top() > tmp:
#             inp_st.push(tmp_st.pop())
#         tmp_st.push(tmp)
#     return tmp_st
#
#
# print(st1)
# print(sort_stack(st1).__str__())
#
# n = 13
#
#
# def dec_to_bin(num: int):
#     st_dec_bin = Stack()
#     str_num = ""
#     if num == 0:
#         return 0
#     while int(num) != 0:
#         remain = num % 2
#         num = int(num / 2)
#         st_dec_bin.push(remain)
#
#     for i in range(st_dec_bin.__len__()):
#         str_num += str(st_dec_bin.pop())
#     return int(str_num)

# def ter_to_dec(ternary):
#     s = 0
#     ter_st = Stack()
#     for i,j in enumerate(reversed(str(ternary))):
#         ter_st.push(int(j)*int(str(3**i)))
#     while not ter_st.is_empty():
#         s+=ter_st.pop()
#     return s
# print(ter_to_dec(202212).__str__())

def help_classmate(inp_st: Stack):
    len_inp = inp_st.__len__()
    tmp_st = Stack()
    res_st = Stack()
    while not inp_st.is_empty():
        tmp = inp_st.pop()
        flag = True
        c = 0
        while not tmp_st.is_empty():
            if tmp > tmp_st.top():
                res_st.push(tmp_st.top())
                flag = False
                # break
                for i in range(c):
                    tmp_st.push(inp_st.pop())
                tmp_st.push(tmp)
                break
                # else:
                #     res_st.push(-1)

                # inp_st.push(tmp_st.top())
            else:
                inp_st.push(tmp_st.pop())
                c += 1
        if res_st.__len__() == len_inp:
            return copy_reverse(res_st)
        if flag:
            for i in range(c):
                tmp_st.push(inp_st.pop())
            tmp_st.push(tmp)
            # else:
            # tmp_st.push(inp_st.pop())
            # tmp_st.push(tmp)
            res_st.push(-1)
        else:
            pass
    return copy_reverse(res_st)



marks = [1, 2, 3, 4]


m_st = Stack()
for i in marks:
    m_st.push(i)
print(help_classmate(m_st).__str__())

# print(ter_to_dec(0))
# print(ter_to_dec(1))
# print(ter_to_dec(2))
# print(ter_to_dec(3))
# print(ter_to_dec(12))
# print(ter_to_dec(22))
# print(dec_to_bin(0))


class Stack:
    def __init__(self):
        self.arr = []

    def __len__(self):
        return len(self.arr)
    def is_empty(self):
        return len(self.arr)==0
    def __str__(self):
        return str(self.arr)
    def push(self,num):
        self.arr.append(num)
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.arr[-1]
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.arr.pop()

stack = Stack()
arr = [4, 0, 1, 5, 9, 8, 2]
for item in arr:
    stack.push(item)
print(stack.__str__())

def copy_reverse(inp_stack: Stack):
    st = Stack()
    while not inp_stack.is_empty():
        st.push(inp_stack.pop())
    return st

def copy_st(inp_stack: Stack):
    st = copy_reverse(inp_stack)
    while not st.is_empty():
        inp_stack.push(st.pop())
    return inp_stack

st1 = copy_st(stack)
print(st1.__str__())