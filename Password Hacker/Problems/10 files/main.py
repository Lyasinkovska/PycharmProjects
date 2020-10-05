# write your code here
for i in range(1, 11):
    with open(f'file{i}.txt', 'w', encoding='utf-8') as f:
        f.write(f'{i}')
