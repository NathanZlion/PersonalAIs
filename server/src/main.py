from src.app import app
from src.api.v1.routes import routers as v1_routers
from src.core.container import Container


container = Container()
app.container = container  # type: ignore

app.include_router(v1_routers, prefix="/v1")
