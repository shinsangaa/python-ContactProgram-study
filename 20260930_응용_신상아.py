# 과제2. contact.py 응용한 프로그램 작성
# 성적 관리 프로그램
# 학생의 학점, 학생의 등수 확인

class ScoreInfo :
    def __init__(self, name, subject, score) :
        self.name = name
        self.subject = subject
        self.score = score

    def print_info(self) :
        print('=' * 30)
        print('이름 : ', self.name)
        print('과목 : ', self.subject)
        print('점수 : ', self.score)

# 메뉴1. 이름, 과목, 점수를 입력받아 ScoreInfo 객체 생성
def set_scoreinfo() :
    name = input('학생 이름 입력 : ')
    subject = input('과목명 입력 : ')
    while True :
        score = input('점수 입력 : ')
        if score == 'A+' or score == 'A' or score == 'B+' or score == 'B' or score == 'C+' or score == 'C' or score == 'D+' or score == 'D' or score == 'F' :
            scoreinfo = ScoreInfo(name, subject, score)
            print(f'이름 : {name}, 과목명 : {subject}, 점수 : {score}')
            return scoreinfo
        else :
            print('성적을 잘 못 입력하셨습니다.')


# 메뉴2. 이름을 입력받으면 학생의 학점 출력
def gpa_scoreinfo(scoreinfo_list, name) :
    for scoreinfo in scoreinfo_list :
        if scoreinfo.name == name :
            cal_gpa_scoreinfo(scoreinfo_list, name)
    print(f'{name}의 학점 : {cal_gpa_scoreinfo(scoreinfo_list, name)}')
            

# 메뉴3. 이름을 입력받으면 학생의 등수 출력
# 정렬 코드는 반복문 종료 후 밖에서 정렬해야 함
def rank_scoreinfo(scoreinfo_list, name) :
    all_student_gpa_list = []
    all_student_list = []
    for scoreinfo in scoreinfo_list : # 학생이름 리스트 생성
        all_student_list.append(scoreinfo.name)
    all_student_list = list(set(all_student_list)) # 중복값 제거. for문 밖에서 실행

    # 모든 학생의 이름과 gpa를 2차원리스트로 저장
    for student_name in all_student_list :
        gpa = cal_gpa_scoreinfo(scoreinfo_list, student_name)
        name_gpa_2d_list = [student_name, gpa] # [학생이름, gpa값] 2차원 리스트
        all_student_gpa_list.append(name_gpa_2d_list) # [['홍길동', 3.5], ['김민지', 4.0], ...]

    all_student_gpa_list.sort(key=lambda x:(-x[1], x[0])) # gpa값 내림차순 정렬, 동점인 경우 이름 오름차순
    print('전체 학생 성적 : ', all_student_gpa_list)

    for i, data in enumerate(all_student_gpa_list) :
        if data[0] == name :
            rank = i + 1 # 인덱스는 0부터 시작하므로 +1
            print (f'{name} 학생의 등수는 {rank}등 입니다.')
            return

# 각 학생의 학점 계산
def cal_gpa_scoreinfo(scoreinfo_list, name) :
    student_score_list = []
    for scoreinfo in scoreinfo_list :
        if scoreinfo.name == name :
            student_score_list.append(scoreinfo.score)

    # 데이터가 없어서 리스트 길이가 0이라면 None 반환하고 함수 종료
    if len(student_score_list) == 0 :
        return None
    for i in range(len(student_score_list)) :
        if student_score_list[i] == 'A+' :
            student_score_list[i] = 4.5
        elif student_score_list[i] == 'A' :
            student_score_list[i] = 4.0
        elif student_score_list[i] == 'B+' :
            student_score_list[i] = 3.5
        elif student_score_list[i] == 'B' :
            student_score_list[i] = 3.0
        elif student_score_list[i] == 'C+' :
            student_score_list[i] = 2.5
        elif student_score_list[i] == 'C' :
            student_score_list[i] = 2.0
        elif student_score_list[i] == 'D+' :
            student_score_list[i] = 1.5
        elif student_score_list[i] == 'D' :
            student_score_list[i] = 1.0
        elif student_score_list[i] == 'F' :
            student_score_list[i] = 0.0

    student_gpa = sum(student_score_list) / len(student_score_list)
    
    return student_gpa


# 메뉴4. 프로그램 종료 시 데이터를 scoreinfo_db.txt에 저장
def store_scoreinfo(scoreinfo_list) :
    f = open('scoreinfo_db.txt', 'w')
    for scoreinfo in scoreinfo_list :
        f.write(scoreinfo.name + '\n')
        f.write(scoreinfo.subject + '\n')
        f.write(str(scoreinfo.score) + '\n')
    f.close()

# 프로그램 시작 시 scoreinfo_db.txt 파일에서 기존 데이터 읽어옴
# f.close() 쓰지 않아도 된다 (프로그램 종료 시 파일 닫힘)
def load_scoreinfo(scoreinfo_list) :
    f = open('scoreinfo_db.txt', 'rt')
    lines = f.readlines()
    num = len(lines) / 3
    num = int(num)

    for i in range(num) :
        name = lines[3*i].rstrip('\n')
        subject = lines[3*i + 1].rstrip('\n')
        score = lines[3*i + 2].rstrip('\n')
        scoreinfo = ScoreInfo(name, subject, score)
        scoreinfo_list.append(scoreinfo)

def print_menu() :
    print('=' * 30)
    print('1. 이름, 과목, 점수 입력')
    print('2. 학생의 학점 확인')
    print('3. 학생의 등수 확인')
    print('4. 종료')
    print('=' * 30)

    menu = input('메뉴 선택 : ')
    return int(menu)

def run() :
    scoreinfo_list = []
    load_scoreinfo(scoreinfo_list)

    while True : 
        menu = print_menu()

        if menu == 1 :
            scoreinfo = set_scoreinfo()
            scoreinfo_list.append(scoreinfo)
        elif menu == 2 :
            name = input('학생 이름을 입력하세요 : ')
            gpa_scoreinfo(scoreinfo_list, name)
        elif menu == 3 :
            name = input('학생 이름을 입력하세요 : ')
            rank_scoreinfo(scoreinfo_list, name)
        elif menu == 4 :
            store_scoreinfo(scoreinfo_list)
            break
        else :
            print('1 ~ 4 중 다시 선택하세요.')

if __name__ == '__main__' :
    run()
