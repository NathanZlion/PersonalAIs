from src.api.v1.middlewares.auth_middleware import AuthUserExtractFromTokenMiddleware
from src.app import app
from src.api.v1.routes import routers as v1_routers
from src.core.container import Container

container = Container()
app.container = container  # type: ignore

# Global middlewares
app.add_middleware(AuthUserExtractFromTokenMiddleware)

app.include_router(v1_routers, prefix="/v1")
