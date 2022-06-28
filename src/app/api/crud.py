from app.api.models import CovidReportSchema
from app.db import covid_report, database


async def post(payload: CovidReportSchema):
    query = covid_report.insert().values(
        country=payload.country,
        confirmed=payload.confirmed,
        state=payload.state,
        deaths=payload.deaths,
        recovered=payload.recovered,
    )
    return await database.execute(query=query)


async def get(id: int):
    query = covid_report.select().where(id == covid_report.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = covid_report.select()
    return await database.fetch_all(query=query)
