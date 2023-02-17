
class ArrayStack:
    def __init__(self):
        self.arr = []
    def __len__(self):
        return (len(self.arr))
    # def __str__(self):
    #     return str(self.arr)
    def isempty(self):
        return len(self.arr)==0
    def push(self, num):
        self.arr.append(num)
    def pop(self):
        if self.isempty():
            raise Exception("Empty stack")
        else:
            return self.arr.pop()
    def top(self):
        return(self.arr[-1])


# arr = [1,2,3,4,5,6,7]
# stack = ArrayStack()
# for i in arr:
#     stack.push(i)
# stack.__str__()


open = "([{"
close = ")]}"
str = "([{)]}"
st = ArrayStack()
# for i in str:
#     stack.push(i)
# stack.__str__()

def matching_paren(str, st):
    for i in str:
        if i in open:
            st.push(i)
        elif i in close:
            pos = close.index(i)
            if (st.__len__() > 0) and open[pos] == st.top():
                st.pop()
            else:
                return False
    if st.isempty():
        return True
    else:
        return False
print(matching_paren("{([]}", st))



