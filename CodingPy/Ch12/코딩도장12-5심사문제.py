# 표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 
# 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤 딕셔너리를 출력하는 프로그램을 만드세요. 
# input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.
# ex)
# >>> health health_regen mana mana_regen
# >>> 575.6 1.7 338.8 1.63
# {'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
# >>> health mana melee attack_speed magic_resistance
# >>> 573.6 308.8 600 0.625 35.7
# {'health': 573.6, 'mana': 308.8, 'melee': 600.0, 'attack_speed': 0.625, 'magic_resistance': 35.7}
# 문제 제출 코딩도장 Python
# 답안 제출 2022/01/05 18:18 경준현

first = input().split()
second = map(float, input().split())
statDict = dict(zip(first,second))
print(statDict)

# first에는 key값을, second에는 value값을 입력받는다. second는 실수로 받는다고 하였으므로 map(float,input().split())을 사용하여 실수로 캐스팅한다.
# dict를 생성하는 방법에는 여러 방법이 있지만, 이번에는 리스트 형식으로 값을 받았으므로 zip을 이용하여 dict를 생성한다.
