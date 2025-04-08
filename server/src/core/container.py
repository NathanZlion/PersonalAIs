"""
This is a module for setting up the application container, for dependency injection.
"""

from dependency_injector import containers, providers
import pkgutil

from src.repository.spotify_credentials_repo import SpotifyCredentialsRepo
from src.repository.session_repo import SessionRepo
from src.repository.user_repo import UserRepo
from src.services.auth_service import AuthService
import src
from src.services.session_service import SessionService
from src.services.spotify_credentials_service import SpotifyCredentialsService
from src.services.user_service import UserService


class Container(containers.DeclarativeContainer):
    """Application container."""

    package = src

    modules = [
        module_name
        for _, module_name, _ in pkgutil.walk_packages(
            package.__path__, package.__name__ + "."
        )
    ]

    wiring_config = containers.WiringConfiguration(modules=modules)

    # Repositories
    user_repo = providers.Singleton(UserRepo)
    session_repo = providers.Singleton(SessionRepo)
    spotify_credentials_repo = providers.Singleton(SpotifyCredentialsRepo)

    # Services
    session_service = providers.Factory(SessionService, session_repo=session_repo)
    auth_service = providers.Factory(
        AuthService,
        user_repo=user_repo,
        session_service=session_service,
    )
    spotify_credentials_service = providers.Factory(
        SpotifyCredentialsService, spotify_credentials_repo=spotify_credentials_repo
    )
    user_service = providers.Factory(
        UserService,
        user_repo=user_repo,
        session_service=session_service,
    )
