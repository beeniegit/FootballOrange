from fastapi import APIRouter, Query
from datetime import datetime
from util.players import listmaker

person_list = listmaker.listmaker("/root/git/project/FootballOrange/data/csv/premier-player-23-24.csv")

router = APIRouter(
    prefix="/players"
)

@router.get("")
async def get_root(index: int | None = None):
    return {"players" : person_list} if index is None else person_list[index]

@router.get("/team")
async def get_team(team:str = "Manchester United"):
    new_list = []
    
    for pla in person_list:
        if pla.팀 == team:
            new_list.append(pla)
    
    return {"players" : new_list}

@router.get("/position")
async def get_position(position:str = "FW"):
    new_list = []

    for pla in person_list:
        if pla.포지션 == position:
            new_list.append(pla)

    return {"players" : new_list}

@router.get("/OBYB")
async def get_obyb(age:int = 30):
    ob_list = []
    yb_list = []
    for pla in person_list:
        if pla.나이 < age:
            yb_list.append(pla)
        else :
            ob_list.append(pla)

    return {"Young Players" : yb_list, "Old Players" : person_list}

@router.get("/search")
async def get_search(parameter=str):
    new_list = []

    for pla in person_list:

