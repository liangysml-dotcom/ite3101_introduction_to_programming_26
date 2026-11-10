n = [3, 5, 7]

def double_list(x):
    new_list = []
for i in range(0, len(x)):
    new_list.append(x[i] * 2)
return new_list
# Don't forget to return your new list!

def double_list(x:List{int}) -> List[int]:
    for i in range(0,len(x)):
        x[i] = x[i] * 2
    return x 

print(double_list(n))
