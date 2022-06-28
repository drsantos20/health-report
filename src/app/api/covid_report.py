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
