num = int(input())
word = input()
counter = 0
for i in range(num):
    if word[i] == 'a' or word[i] == 'i' or word[i] == 'u' or word[i] == 'e' or word[i] == 'o' :
        counter += 1
print(str(counter))
