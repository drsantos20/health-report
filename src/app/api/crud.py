from app.api.models import CovidReportSchema
from app.db import covid_report, database


async def post(payload: CovidReportSchema):
    query = covid_report.insert().values(
        country=payload.country,
        confirmed=payload.confirmed,
        deaths=payload.deaths,
        recovered=payload.recovered,
    )
    return await database.execute(query=query)
