# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

# 입력
# 영문자 1개가 입력된다. (a ~ z)
# f

# 출력
# a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.
# a b c d e f

# 내 풀이)
alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abc = input()
for i in alphabet:
    print('{}'.format(i), end =' ')
    if i == abc:
        break
# 강의 풀이)
converter = ord(input())
for i in range(97, converter+1):
  print( chr(i), end=' ' )