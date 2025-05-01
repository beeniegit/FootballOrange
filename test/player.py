import csv

class player:
    def __init__(self, 이름, 국적, 포지션, 나이, 출전수, 선발, 출전시간, 경기수_평균, 골, 어시스트, 공격포인트, 필드골, 패널티킥_득점, 패널티킥, 경고, 퇴장, 기대_득점, 기대_득점_PK제외, 기대_어시스트, 기대_공격포인트_PK제외, 드리블_거리, 패스_전진_거리, 드리블_횟수, 평균_득점, 평균_어시스트, 평균_공격포인트, 평균_필드골, 평균_기대_득점_및_어시스트_PK제외, 평균_기대_득점, 평균_기대_어시스트, 평균_기대_공격포인트, 평균_기대_득점_PK제외, 평균_기대_공격포인트_PK제외, 팀):
        self.이름 = 이름
        self.국적 = 국적
        self.포지션 = 포지션
        self.나이 = 나이
        self.출전수 = 출전수
        self.선발 = 선발
        self.출전시간 = 출전시간
        self.경기수_평균 = 경기수_평균
        self.골 = 골
        self.어시스트 = 어시스트
        self.공격포인트 = 공격포인트
        self.필드골 = 필드골
        self.패널티킥_득점 = 패널티킥_득점
        self.패널티킥 = 패널티킥
        self.경고 = 경고
        self.퇴장 = 퇴장
        self.기대_득점 = 기대_득점
        self.기대_득점_PK제외 = 기대_득점_PK제외
        self.기대_어시스트 = 기대_어시스트
        self.기대_공격포인트_PK제외 = 기대_공격포인트_PK제외
        self.드리블_거리 = 드리블_거리
        self.패스_전진_거리 = 패스_전진_거리
        self.드리블_횟수 = 드리블_횟수
        self.평균_득점 = 평균_득점
        self.평균_어시스트 = 평균_어시스트
        self.평균_공격포인트 = 평균_공격포인트
        self.평균_필드골 = 평균_필드골
        self.평균_기대_득점_및_어시스트_PK제외 = 평균_기대_득점_및_어시스트_PK제외
        self.평균_기대_득점 = 평균_기대_득점
        self.평균_기대_어시스트 = 평균_기대_어시스트
        self.평균_기대_공격포인트 = 평균_기대_공격포인트
        self.평균_기대_득점_PK제외 = 평균_기대_득점_PK제외
        self.평균_기대_공격포인트_PK제외 = 평균_기대_공격포인트_PK제외
        self.팀 = 팀


def listmaker(filename):
    persons = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = player(
                이름=row['Player'],
                국적=row['Nation'],
                포지션=row['Pos'],
                나이=row['Age'],
                출전수=row['MP'],
                선발=row['Starts'],
                출전시간=row['Min'],
                경기수_평균=row['90s'],
                골=row['Gls'],
                어시스트=row['Ast'],
                공격포인트=row['G+A'],
                필드골=row['G-PK'],
                패널티킥_득점=row['PK'],
                패널티킥=row['PKatt'],
                경고=row['CrdY'],
                퇴장=row['CrdR'],
                기대_득점=row['xG'],
                기대_득점_PK제외=row['npxG'],
                기대_어시스트=row['xAG'],
                기대_공격포인트_PK제외=row['npxG+xAG'],
                드리블_거리=row['PrgC'],
                패스_전진_거리=row['PrgP'],
                드리블_횟수=row['PrgR'],
                평균_득점=row['Gls_90'],
                평균_어시스트=row['Ast_90'],
                평균_공격포인트=row['G+A_90'],
                평균_필드골=row['G-PK_90'],
                평균_기대_득점_및_어시스트_PK제외=row['G+A-PK_90'],
                평균_기대_득점=row['xG_90'],
                평균_기대_어시스트=row['xAG_90'],
                평균_기대_공격포인트=row['xG+xAG_90'],
                평균_기대_득점_PK제외=row['npxG_90'],
                평균_기대_공격포인트_PK제외=row['npxG+xAG_90'],
                팀=row['Team']
            )
            persons.append(person)
    return persons

l = listmaker("/root/git/project/FootballOrange/data/csv/premier-player-23-24.csv")

for pla in l:
    print(f'[이름] {pla.이름}')
    print(f'[경고] {pla.경고}')
    print(f'[어시스트] {pla.어시스트}')
    print(f'[기대 어시스트] {pla.기대_어시스트}')
    print(f'[득점] {pla.골}')
    print(f'[기대 득점] {pla.기대_득점}')
    print(f'[팀] {pla.팀}')
    print()
    