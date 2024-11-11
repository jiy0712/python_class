#계좌 생성 고객의 이름을 전달 받아 초기화하는 Account 클래스를 정의
#이를 상속받는 Saving, Deposit 클래스를 정의하도록 한다.
#각각 적금 계좌를 가진 고객의 이름과 입금 금액(원)을 저장하는 Saving 클래스와 예금 계좌를 가진 고객의 이름과 초기 금액과 인출 금액을 저장
#잔액(초기금액 - 인출금액)을 가지는 Deposit 클래스를 정ㅊ의하시오.
#클래스 정의 부분을 제외한 메인 부분의 코드가 다음과 같다고 할 때 적절한 클래스를 정의하여 프로그램을 완성하시오.

class Account: #저장 받은 것을 초기화
    #계좌 생성 고객의 이름을 전달 받아 초기화하는
    def __init__(self, name):
        self.name = name
class Saving(Account): #1번째. 저장
    # 각각 적금 계좌를 가진 고객의 이름과 입금 금액(원)을 저장
    def __init__(self, name, deposit_account):
        super().__init__(name)
        self.deposit_a = deposit_account
        self.deposit_a = self.deposit_a
    def __str__(self):
        return f"고객명 : {self.name}, 입금 금액 : {self.deposit_a}원"
class Deposit(Account):
    #예금 계좌를 가진 고객의 이름과 초기 금액과 인출 금액을 저장
    # 잔액(초기금액 - 인출금액)을 가지는
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a #처음
        self.b = b #뺀금액
        self.r = a - b #잔액
    def __str__(self):
        return f"고객명: {self.name}, 남은잔액: {self.r}원"

saving_account = Saving("Alice", 1000000)
deposit_account = Deposit("Bob", 500000, 100000)
print(saving_account)  # 고객 이름과 적금 잔액 출력
print(deposit_account)  # 고객 이름과 초기 잔액 출력
