from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from util.sqlite.database import SessionLocal
from util.sqlite.models import Player

router = APIRouter(
    prefix="/playersTest"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
async def get_root(index: int | None = None, db: Session = Depends(get_db)):
    players = db.query(Player).all()
    return {"players" : players} if index is None else players[index]

@router.get("/team")
async def get_team(team:str = "Manchester United", db: Session = Depends(get_db)):
    new_list = []
    players = db.query(Player).all()

    for pla in players:
        if pla.팀 == team:
            new_list.append(pla)
    
    return {"players" : new_list}

@router.get("/position")
async def get_position(position:str = "FW", db: Session = Depends(get_db)):
    players = db.query(Player).all()

    # 올바른 포지션이 입력되었는지 확인
    if (position not in ["MF", "FW", "DF", "GK"]) :
        return {"error" : "잘못된 포지션 정보를 입력했습니다."}

    # 리스트 생성
    new_list = []
    for pla in players:
        if position in pla.포지션:
            new_list.append(pla)
    return {"players" : new_list}

# "OB" 라는 단어를 입력 -> OB 에 해당하는 선수들 리스트를 반환
# "YB" 라는 단어를 입력 -> YB 에 해당하는 선수들 리스트를 반환
@router.get("/Group")
async def get_obyb(group:str="OB", db: Session = Depends(get_db)):

    players = db.query(Player).all()
    if group not in ["OB", "YB"]:
        return {"error" : "잘못된 그룹을 입력했습니다. OB 또는 YB를 입력해야 합니다."}

    if group == "OB":
        new_list = []
        for pla in players:
            if pla.나이 >= 30:
                new_list.append(pla)
        return {"OB" : new_list}

    else:
        new_list = []
        for pla in players:
            if pla.나이 < 30:
                new_list.append(pla)
        return {"YB" : new_list}

# 팀, 골
@router.get("/search")
async def get_search(team:str, goal:int | None = None, db: Session = Depends(get_db)):

    players = db.query(Player).all()

    # 아무것도 입력받지 않은 경우
    if team == None & goal == None:
        return {"result" : players}

    # 팀만 입력받은 경우
    if team != None & goal == None:
        list = []
        for pla in players:
            if pla.팀 == team:
                list.append(pla)
        return {"result" : list}

    # 골만 입력받은 경우
    if team == None & goal != None:
        list = []
        for pla in players:
            if pla.골 >= goal:
                list.append(pla)
        return {"result" : list}

    # 둘 다 입력받은 경우
    else:
        list = []
        for pla in players:
            if pla.팀 == team:
                list.append(pla)
        for pla in list:
            if pla.골 < goal:
                list.remove(pla)
        return {"result" : list}

# 기능 구현해보기 -> 테스트(동작) -> 고치기 :: GPT 물어보기 -> 마무리 테스트





