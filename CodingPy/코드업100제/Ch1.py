# [1]
# Hello
# 출력하기

print("Hello")

# [2]
# Hello World
# 출력하기

print("Hello World")
#한 줄에 대해 출력

# [3]
# Hello
# World
# (두 줄에 걸쳐 줄을 바꿔 출력하기)

# Tip::

# 따옴표를 '''(작은따옴표) 혹은 """(큰따옴표) 와 같이 3개씩 사용하면 입력하는 모양대로 출력된다.
# 처음 따음표 ''' 뒤에 역슬래기()를 해주어야 직관적으로 코딩할 수 있게 된다.

#1번답압
print("Hello")
print("World")
#프린트 문이 끝난 후 자동개행

#2번답안
print("""Hello
World""")
#모양대로 출력

# [4]
# 'Hello'
# (단, 작은 따옴표도 함께 출력한다.)


print("\'Hello\'")
#이스케이프 시퀸스

# [5]
# "Hello World"
# (단, 큰따옴표도 함께 출력한다.)

print('\"Hello World\"')
#이스케이프 시퀸스

# [6]
# "!@#$%^&*()"
# (단, 큰따옴표도 함께 출력한다.)

print('\"!@#$%^&*()\"')
#문자 취급

# [7]
# "C:\Download\hello.cpp"
# (단, 큰따옴표도 함께 출력한다.)

print('\"C:\Download\hello.cpp\"')

# [8]
# ┌┬┐
# ├┼┤
# └┴┘
# 출력하기

#1번답안
print("""┌┬┐
├┼┤
└┴┘""")

#2번답안
print("""\
┌┬┐
├┼┤
└┴┘
""")
#"""에 이스케이프 시퀸스, \ 를 사용하면 보기 편하게 처리 할 수 있다.