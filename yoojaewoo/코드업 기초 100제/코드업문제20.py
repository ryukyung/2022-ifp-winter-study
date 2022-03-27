# 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
# 입력 :
# 1.435867
# 출력 :
# 1
# 435867
# 내 풀이)
jungsu, silsu = input().split('.')
print(jungsu, end='\n' + silsu)
# 강의 풀이)
string = input().split('.')
print('''\
{}
{}
'''.format(string[0], string[1]))