"""
This is a module for setting up the application container, for dependency injection.
"""

from dependency_injector import containers, providers
import pkgutil

from src.repository.user_repo import UserRepo
from src.services.auth_service import AuthService
import src


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

    user_repo = providers.Singleton(UserRepo)

    auth_service = providers.Factory(
        AuthService,
        user_repo=user_repo,
    )
