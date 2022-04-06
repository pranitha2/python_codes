List = []
my_list =[1, 1, 1, 5, 5,3]
my_list.sort()
freq = {}

for item in my_list:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

for key, value in freq.items():
    if(value>1):
         List.append(key)   

List.sort()
print(List)
