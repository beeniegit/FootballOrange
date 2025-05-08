import csv
from app.util.players.player import player

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