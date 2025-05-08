import sqlite3

from app.util.players import listmaker

conn = sqlite3.connect('app/example.db')

# 커서 객체 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players  (
        Player TEXT,
        Nation TEXT,
        Pos TEXT,
        Age INTEGER,
        MP INTEGER,
        Starts REAL,
        Min REAL,
        AVGs REAL,
        Gls REAL,
        Ast REAL,
        GnA REAL,
        GmPK REAL,
        PK REAL,
        PKatt REAL,
        CrdY REAL,
        CrdR REAL,
        xG REAL,
        npxG REAL,
        xAG REAL,
        npxGpxAG REAL,
        PrgC REAL,
        PrgP REAL,
        PrgR REAL,
        GlsAvg REAL,
        AstAvg REAL,
        GnAAvg REAL,
        GmPKAvg REAL,
        GnAmPKAvg REAL,
        xGAvg REAL,
        xAGAvg REAL,
        xGaxAGAvg REAL,
        npxGAvg REAL,
        npxGnxAGAvg REAL,
        Team TEXT
    )
''')

players = listmaker.listmaker("/root/git/project/FootballOrange/data/csv/premier-player-23-24.csv")

cursor = conn.cursor()
for p in players:
    cursor.execute('''
                   INSERT INTO players
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                           ?, ?, ?)
                   ''', (
                       p.이름, p.국적, p.포지션, p.나이, p.출전수, p.선발, p.출전시간,
                       p.경기수_평균, p.골, p.어시스트, p.공격포인트, p.필드골, p.패널티킥_득점,
                       p.패널티킥, p.경고, p.퇴장, p.기대_득점, p.기대_득점_PK제외,
                       p.기대_어시스트, p.기대_공격포인트_PK제외, p.드리블_거리, p.패스_전진_거리,
                       p.드리블_횟수, p.평균_득점, p.평균_어시스트, p.평균_공격포인트,
                       p.평균_필드골, p.평균_기대_득점_및_어시스트_PK제외, p.평균_기대_득점,
                       p.평균_기대_어시스트, p.평균_기대_공격포인트, p.평균_기대_득점_PK제외,
                       p.평균_기대_공격포인트_PK제외, p.팀
                   ))
conn.commit()


# 데이터 조회 예시
cursor.execute("""
SELECT Player, Age, Gls
FROM players
WHERE 
Age >= 30 AND
Gls >= 5
ORDER BY Age DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 연결 종료
conn.close()
