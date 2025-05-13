def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return -1

    return 1


n = int(input())
cnt = 0
for _ in range(n):
    if is_palindrome(input()) == 1:
        cnt += 1

print(cnt * (cnt - 1))