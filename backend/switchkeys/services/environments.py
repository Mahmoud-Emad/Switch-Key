from typing import Dict, List
from switchkeys.models.users import DeviceType, ProjectEnvironmentUser, UserDevice
from switchkeys.models.management import (
    EnvironmentFeature,
    ProjectEnvironment,
    OrganizationProject,
)


def get_all_environments() -> List[ProjectEnvironment]:
    """Return all environments"""
    return ProjectEnvironment.objects.all().order_by("name")


def get_all_project_environments(
    project_id: OrganizationProject,
) -> List[OrganizationProject]:
    """Return all project environments"""
    return ProjectEnvironment.objects.filter(project__id=project_id).order_by("name")


def get_environment_by_id(id: str) -> ProjectEnvironment:
    """Return project environment who has the same id"""
    if not id.isdigit():
        return None
    try:
        return ProjectEnvironment.objects.get(id=int(id))
    except ProjectEnvironment.DoesNotExist:
        return None


def get_environment_by_key(environment_key: str) -> ProjectEnvironment | None:
    """Return project environment who has the same id"""
    try:
        return ProjectEnvironment.objects.get(environment_key=str(environment_key))
    except ProjectEnvironment.DoesNotExist:
        return None


def get_environment_user_by_id(user_id: str) -> ProjectEnvironmentUser | None:
    """Return project environment who has the same id"""
    if not user_id.isdigit():
        return None
    try:
        return ProjectEnvironmentUser.objects.get(id=int(user_id))
    except ProjectEnvironmentUser.DoesNotExist:
        return None


def get_all_environment_features() -> List[EnvironmentFeature]:
    """Return all environment features"""
    return EnvironmentFeature.objects.all().order_by("key")


def get_environment_user_username(username: str) -> ProjectEnvironmentUser | None:
    """Check and return the user if created or none if not."""
    try:
        return ProjectEnvironmentUser.objects.get(username=username)
    except ProjectEnvironmentUser.DoesNotExist:
        return None


def create_environment_user(
    username: str, device_type: DeviceType, device_version: str, features: Dict
) -> ProjectEnvironmentUser | None:
    """Create the user."""
    device = UserDevice.objects.get_or_create(
        device_type=device_type, version=device_version
    )

    return ProjectEnvironmentUser.objects.create(
        username=username, features=features, device=device[0]
    )

def get_all_environment_features(environment: ProjectEnvironment) -> List[EnvironmentFeature]:
    return EnvironmentFeature.objects.filter(environment__id = environment.id)