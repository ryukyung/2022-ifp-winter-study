''' 12.4 연습문제
다음 소스 코드를 완성하여 게임 캐릭터의 체력(health)과 이동 속도(movement spped)가 출력되게 만드세요
'''
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print['health']
print['movement_speed']

'''12.5 심사문제
표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다.
입력된 첫번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤
딕셔너리를 출력하는 프로그램을 만드세요.
input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.
'''
a=input().split()
b=map(float, input().split()) # 실수
x=dict(zip(a,b)) #zip에 넣은 다음 dict에 넣어 딕셔너리로 만듦
print(x)