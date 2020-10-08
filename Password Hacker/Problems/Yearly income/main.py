# write your code here
with open('salary.txt', 'r', encoding='utf-8') as f1, \
    open('salary_year.txt', 'a', encoding='utf-8') as f2:
    for line in f1.read().split():
        f2.write(str(int(line.strip()) * 12) + '\n')
