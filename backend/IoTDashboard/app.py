import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from IoTDashboard.constants import FAST_API_APP
from IoTDashboard.router import router
from IoTDashboard.services.middlewares import CustomHTTPSRedirectMiddleware
from IoTDashboard.services.sentry import init_sentry
from IoTDashboard.settings import APP_ENV

# Sentry
init_sentry(app=FAST_API_APP)

app = FastAPI()

if APP_ENV != "LOCAL":
    app.add_middleware(CustomHTTPSRedirectMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=80,
        reload_dirs=["IoTDashboard"],
        reload=True,
        workers=1,
    )
