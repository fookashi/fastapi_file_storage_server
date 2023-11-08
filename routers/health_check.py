from fastapi import APIRouter, status
from schemas.health_check import HealthCheckResponse

health_check_router = APIRouter('/health')


@health_check_router.get(
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheckResponse,
)
def get_health() -> HealthCheckResponse:
    return HealthCheckResponse(status="OK")
