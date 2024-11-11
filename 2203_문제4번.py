#중복 없는 랜덤으로 로또 번호 6가지 정수를 생성하여 리스트에 저장하고 사용자로부터 정수를 입력받아 리스트에 저장한 후, 두 리스트를 비교하는 프로그램을 작성
#1~49까지의 수 6가지를 중복 업서는 랜덤 리스트를 만들어 반환하는 Lotto 클래스를 정의

#로또 게임의 결과를 보여주기 위한 LottoGame 클래스를 다음과 같이 정의하기
#사용자가 입력한 6가지의 로또 번호 리스트를 전달 받아 랜덤으로 만들어진 로또 리스트와 비교하여 일치하는 수의 개수와 일치하는 로또 번호 리스트를 반환하는 함수를 정의
#두 리스트를 매개변수로 일치하는 번호를 저장하여 일치하는 숫자의 개수와 숫자ㅏ의 리스트를 반환하는 함수를 정의
#메인에서 로또 번호 입력 함수 호출, 만들어진 클래스 활용해서 두 리스트의 일치하는 수의 개수와 수 리스트를 출력

import random

class Lotto: #범위에 맞는 랜덤번호를 생성한다
    def __init__(self):
        self.number = []
    def random_numbers(self):
        self.number = random.sample(range(1, 50), 6)
        return self.number


class LottoGame: #입력한 번호를 이용해 객체 생성되고
    def __init__(self, u_number):
        self.u_number = u_number
        self.lotto = Lotto()
        self.l_number = self.lotto.random_numbers()
    def c_numbers(self):
        m_number = set(self.u_number) & set(self.l_number)
        return len(m_number), sorted(m_number)

def uu_numbers(): #첫번째 시작
    u_number = []
    for i in range(6):
        while True:
            try: #6개 사용자에게 입력 받는다
                num = int(input(f"1부터 40까지 수를 입력하시오 ({i+1}번째) : "))
                if num < 1 or num > 49:
                    print("범위를 벗어났습니다.")
                elif num in u_number:
                    print("중복 숫자입니다.")
                else:
                    u_number.append(num)
                    break
            except ValueError:
                print("숫자를 입력하세요.")
    return u_number

u_number = uu_numbers()
game = LottoGame(u_number)
m_count, m_number = game.c_numbers()

# 결과 출력
print("\n")
print("입력한 번호 : ", u_number)
print("생성된 번호 : ", game.l_number)
print("일치하는 수 개수 : ", m_count, "일치하는 번호 리스트 : ", m_number)