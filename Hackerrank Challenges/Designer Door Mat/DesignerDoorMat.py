string = input()
string = string.split(" ")
n = int(string[0])
m = int(string[1])

for i in range(1, (n+1)//2):
    print((".|." * (2*i - 1)).center(m, '-'))
        
print("WELCOME".center(m, '-'))

for i in range((n-1)//2, 0, -1):
    print((".|." * (2*i - 1)).center(m, "-"))
