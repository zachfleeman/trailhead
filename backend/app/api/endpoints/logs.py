from typing import Any
from fastapi import APIRouter
from trailscraper.record_sources.cloudtrail_api_record_source import CloudTrailAPIRecordSource
from utils.time import parse_human_readable_time
import json

router = APIRouter()

@router.get("/")
def get_logs(from_s: str, to_s: str) -> Any:
    from_date = parse_human_readable_time(from_s)
    to_date = parse_human_readable_time(to_s)
    resp = CloudTrailAPIRecordSource().load_from_api(from_date, to_date)
    records = [record.raw_source for record in resp]
    return json.loads(json.dumps({'records': records}, indent=2))
    