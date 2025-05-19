import pandas as pd

path_in = "/root/git/project/FootballOrange/NewStreamlitApplication/dataset/premier-player-23-24.csv"
path_out = "/root/git/project/FootballOrange/NewStreamlitApplication/dataset/player.csv"

# CSV 파일 읽기
df = pd.read_csv(path_in)  # 파일명을 실제 파일명으로 변경하세요

# 'Team' 컬럼의 공백 제거
df['Team'] = df['Team'].str.replace(" ", "", regex=False)

# 결과를 새 CSV로 저장
df.to_csv(path_out, index=False)


