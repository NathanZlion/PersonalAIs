from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.api.v1.middlewares.auth_middleware import AuthUserExtractFromTokenMiddleware
from src.app import app
from src.api.v1.routes import routers as v1_routers
from src.core.container import Container

container = Container()
app.container = container  # type: ignore

# Global middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(AuthUserExtractFromTokenMiddleware)
app.include_router(v1_routers, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, log_level="debug")
