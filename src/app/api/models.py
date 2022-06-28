from pydantic import BaseModel


class CovidReportSchema(BaseModel):
    country: str
    state: str
    confirmed: int
    deaths: int
    recovered: int


class CovidSchemaDB(CovidReportSchema):
    id: int
