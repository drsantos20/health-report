from typing import List

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.api.models import CovidSchemaDB, CovidReportSchema


router = APIRouter()


@router.post("/", response_model=CovidSchemaDB, status_code=201)
async def create_covid_report(payload: CovidReportSchema):
    covid_report_id = await crud.post(payload)

    response_object = {
        "id": covid_report_id,
        "country": payload.country,
        "confirmed": payload.confirmed,
        "deaths": payload.deaths,
        "recovered": payload.recovered,
    }
    return response_object


@router.get("/{id}/", response_model=CovidSchemaDB)
async def read_covid_report(id: int):
    covid_report = await crud.get(id)
    if not covid_report:
        raise HTTPException(status_code=404, detail="Report not found")
    return covid_report


@router.get("/", response_model=List[CovidSchemaDB])
async def read_all_covid_report():
    return await crud.get_all()
