import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .constants import FAST_API_APP
from .db import engine
from .router import router
from .services.middlewares import CustomHTTPSRedirectMiddleware
from .services.sentry import init_sentry
from .settings import APP_ENV

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

if APP_ENV != "LOCAL":
    app.add_middleware(CustomHTTPSRedirectMiddleware)
    # Sentry
    init_sentry(app=FAST_API_APP)

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
