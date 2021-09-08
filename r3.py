lines = []
with open ('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] #s[0]的字串，可以當成清單，再繼續取出[0:5]，0可省略
    name = s[0][5:] #s[0]的字串，可以當成清單，再繼續取出[5:最後]，最後可省略
    print(name)