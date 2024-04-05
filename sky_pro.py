n, p = map(int, input().split())
p //= 10
list_ = []
for i in range(p):
    list_.append('*')

for i in range(n - p):
    list_.append('.')

list_ = str(list_).split('')
print(list_)
