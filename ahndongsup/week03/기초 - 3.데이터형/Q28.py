# 정수 1개를 입력받아 그대로 출력해보자.

# 파이썬에서의 int() 데이터형의 크기는 4바이트(32비트)로 지정되어있다.
# 이보다 큰 범위를 지정하고자 할 때는 long 데이터 형을 이용하면 된다.

# 파이썬에서 제공하는 데이터형
# int (plain integers) : 정수
# long (long integers) : int 보다 범위가 큰 정수(메모리 한계까지 저장 가능, 사실상 무제한)
# float (floating point numbers) : 실수
# complex (complex numbers) : 복소수

integer = int(input())
print(integer)