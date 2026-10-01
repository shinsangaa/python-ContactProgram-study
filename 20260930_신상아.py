# 과제1. 계좌 관리 프로그램 완성
# Account 클래스 - 예금주, 계좌번호, 잔고
import random

class Account :
    def __init__(self, name, num, money) :
        self.name = name
        self.num = num
        self.money = money

    def print_info(self) :
        print('=' * 30)
        print('이름 : ', self.name)
        print('계좌번호 : ', self.num) # 10자리 난수 생성
        print('잔액 : ', self.money)
        print('=' * 30)

# 메뉴1. 사용자로부터 이름을 입력받아 Account 객체 생성 (계좌개설)
def set_account() :
    name = input('이름 입력 : ')
    num = str(random.randint(100000, 999999))
    money = 0
    account = Account(name, num, money)
    print(f'예금주 : {name}, 계좌번호 : {num}')
    return account

# 메뉴2. 사용자로부터 계좌번호, 돈을 입력받아 해당 계좌번호에 돈을 입금
# 메뉴2, 3, 4 에서 for문으로 먼저 감싸야 하는데 작성하지 않아 오류 발생함
# 'for account in account_list' 코드 작성해 수정완료
# contact.py 파일과 같이 'for i, contact in enumerate(contact_list)' 코드 쓰려 했으나
# 오류 발생 원인 파악을 못해 다른 코드로 작성함
def deposit_account(account_list, num, deposit) :
    for account in account_list :
        if account.num == num:
            account.money = account.money + deposit
            print(f'잔액은 {account.money}원 입니다.')
            return
        else :
            print('해당 계좌는 존재하지 않습니다.')

# 메뉴3. 사용자로부터 계좌번호, 돈을 입력받아 해당 계좌번호에 돈을 출금
def withdraw_account(account_list, num, withdraw) :
    for account in account_list :
        if account.num == num :
            if account.money >= withdraw : # 잔액 부족한 경우 체크
                account.money = account.money - withdraw
                print(f'잔액은 {account.money}원 입니다.')
            else :
                print('잔액이 부족합니다.')
            return
        else :
            print('해당 계좌는 존재하지 않습니다.')
        

# 메뉴4. 사용자로부터 계좌번호를 입력받아 잔액 출력
def balance_account(account_list, num) :
    for account in account_list :
        if account.num == num :
            print(f'잔액은 {account.money:,}원 입니다.')
            return
        else :
            print('해당 계좌는 존재하지 않습니다.')

# 메뉴5. 프로그램 종료 시 데이터를 account_db.txt에 저장
def store_account(account_list) :
    f = open('account_db.txt', 'w')
    for account in account_list :
        f.write(account.name + '\n')
        f.write(account.num + '\n')
        f.write(str(account.money) + '\n')
    f.close()

# 프로그램 시작 시 account_db.txt 파일에서 기존 데이터 읽어옴
def load_account(account_list) :
    f = open('account_db.txt', 'rt') # 'rt' 텍스트 읽기 모드
    lines = f.readlines()
    num = len(lines) / 3
    num = int(num)

    for i in range(num) :
        name = lines[3*i].rstrip('\n')
        num = lines[3*i + 1].rstrip('\n')
        money = lines[3*i + 2].rstrip('\n')
        account = Account(name, num, money)
        account_list.append(account)

def print_menu() :
    print('=' * 30)
    print('1. 계좌 개설')
    print('2. 입금')
    print('3. 출금')
    print('4. 잔액 확인')
    print('5. 종료')
    print('=' * 30)

    menu = input('메뉴 선택 : ')
    return int(menu)

def run() :
    account_list = []
    load_account(account_list)

    while True :
        menu = print_menu()

        if menu == 1 :
            account = set_account()
            account_list.append(account)
        elif menu == 2 :
            num = input('계좌번호를 입력하세요 : ')
            for account in account_list :
                if account.num == num :
                    deposit = int(input('입금하실 금액을 입력하세요 : '))
                    deposit_account(account_list, num, deposit)

        elif menu == 3 :
            num = input('계좌번호를 입력하세요 : ')
            withdraw = int(input('출금하실 금액을 입력하세요 : '))
            withdraw_account(account_list, num, withdraw)

        elif menu == 4 :
            num = input('계좌번호를 입력하세요 : ')
            balance_account(account_list, num)

        elif menu == 5 :
            store_account(account_list)
            break
        else :
            print('1 ~ 5 중 다시 입력하세요.')

if __name__ == '__main__' :
    run()
