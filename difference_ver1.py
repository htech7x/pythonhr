a = input("input a: ")
b = input("input b: ")

def str_to_int(str1):

    la = set(str1.split())
    sa = set()
    for i in la:
        sa.add(int(i))
    return sa
n1 = str_to_int(a)
n2 = str_to_int(b)
c = set()
for i in n1:
    if i not in n2:
        c.add(i)

print(len(c))
