from typing import Any
from fastapi import APIRouter
from trailscraper.record_sources.cloudtrail_api_record_source import CloudTrailAPIRecordSource
from utils.time import parse_human_readable_time
from pydantic import BaseModel
import json

class RecordBody(BaseModel):
    from_date: str
    to_date: str

router = APIRouter()

@router.post("/")
def get_records(record_body: RecordBody) -> Any:
    from_date = parse_human_readable_time(record_body.from_date)
    to_date = parse_human_readable_time(record_body.to_date)
    resp = CloudTrailAPIRecordSource().load_from_api(from_date, to_date)
    records = [record.raw_source for record in resp]
    return json.loads(json.dumps({'records': records}, indent=2))
    