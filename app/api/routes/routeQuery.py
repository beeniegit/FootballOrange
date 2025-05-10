from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from util.sqlite.database import SessionLocal
from util.sqlite.models import Player
from util.sqlite.sqliteSample import SqliteTool

router = APIRouter(
    prefix="/playersQuery"
)

tool = SqliteTool()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
async def get_root(index: int | None = None, db: Session = Depends(get_db)):

    QUERY = None
    if index is None:
        QUERY = """
        SELECT *
        FROM players
        """
    else:
        QUERY = f"""
        SELECT *
        FROM players
        WHERE player_id = {index}
        """

    rows = tool.EXECUTE(QUERY)
    return {"players" : rows}

@router.get("/position")
async def get_position(position:str = "FW", db: Session = Depends(get_db)):
    players = db.query(Player).all()

    # 올바른 포지션이 입력되었는지 확인
    if (position not in ["MF", "FW", "DF", "GK"]) :
        return {"error" : "잘못된 포지션 정보를 입력했습니다."}

    QUERY = None
    if position is None:
        QUERY = """
        SELECT *
        FROM players 
            """
    else:
        QUERY = f"""
        SELECT *
        FROM players
        WHERE player_position = {position}
        """

    rows = tool.EXECUTE(QUERY)
    return {f"{position} players" : rows}

# "OB" 라는 단어를 입력 -> OB 에 해당하는 선수들 리스트를 반환
# "YB" 라는 단어를 입력 -> YB 에 해당하는 선수들 리스트를 반환
@router.get("/Group")
async def get_obyb(age=30, group:str="OB", db: Session = Depends(get_db)):

    players = db.query(Player).all()
    if group not in ["OB", "YB"]:
        return {"error" : "잘못된 그룹을 입력했습니다. OB 또는 YB를 입력해야 합니다."}

    QUERY = None
    if group == "OB":
        QUERY = """
         SELECT *
        FROM players 
        WHERE 30 < player_age
        """
        rows = tool.EXECUTE(QUERY)

        return {"OB" : rows}
    else:
        QUERY = """
                SELECT *
                FROM players 
                    WHERE 30 < player_age
        """
        rows = tool.EXECUTE(QUERY)
        return {"YB" : rows}

# 팀, 골
@router.get("/search")
async def get_search(team:str, goal:int | None = None, db: Session = Depends(get_db)):

    players = db.query(Player).all()

    QUERY = None
    # 아무것도 입력받지 않은 경우
    if team == None & goal == None:
        return {"result" : players}

    # 팀만 입력받은 경우
    if team != None & goal == None:

        QUERY = """
                SELECT *
                FROM players 
                    WHERE player_team = {team}
        """
        rows = tool.EXECUTE(QUERY)
        return {"result" : rows}

    # 골만 입력받은 경우
    if team == None & goal != None:
        QUERY = """
                SELECT *
                FROM players 
                    WHERE player_goal = {goal}
        """
        rows = tool.EXECUTE(QUERY)
        return {"result" : rows}

    # 둘 다 입력받은 경우
    else:
        QUERY = """
                SELECT *
                FROM players 
                    WHERE player_goal = {goal} AND player_team = {team}
        """
        rows = tool.EXECUTE(QUERY)
        return {"result" : rows}

# 기능 구현해보기 -> 테스트(동작) -> 고치기 :: GPT 물어보기 -> 마무리 테스트





