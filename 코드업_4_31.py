'''
10진수를 입력받아 8진수(octal)로 출력해보자.
'''
octcal = int(input()) #octcal 변수에 int형으로 입력받은 수 저장
print(oct(octcal)[2:]) #[2:]로 앞 두자리를 생략 시켜줌