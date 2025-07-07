num_n=int(input)
n_list=[]
for i in range(num_n):
    _tmp=int(input())
    n_list.append(_tmp)
print(len(n_list))
print(f'{sum(num_n):.1f}')
print(f'{sum(n_list)/len(n_list):.1f}')
