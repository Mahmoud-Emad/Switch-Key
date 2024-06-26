from typing import Any, Dict, List

from switchkeys.api.response.types import (
    SwitchKeysAuthResponse,
    SwitchKeysOrganizationResponse,
    SwitchKeysProjectResponse,
    SwitchKeysUserResponse,
)


def parse_user(
    user_data: Dict[str, Any]
) -> SwitchKeysUserResponse | List[SwitchKeysUserResponse]:
    """
    Parse user data.

    Args:
        user_data (Dict[str, Any]): User data to be parsed.

    Returns:
        SwitchKeysUserType | List[SwitchKeysUserType]: Parsed user object or list of parsed user objects.
    """

    if type(user_data) == list:
        users: List[SwitchKeysUserResponse] = []
        for user in user_data:
            users.append(
                SwitchKeysUserResponse(
                    background_color=user.get("background_color"),
                    email=user.get("email"),
                    first_name=user.get("first_name"),
                    full_name=user.get("full_name"),
                    is_active=user.get("is_active"),
                    id=user.get("id"),
                    joining_at=user.get("joining_at"),
                    last_name=user.get("last_name"),
                )
            )
    else:
        return SwitchKeysUserResponse(
            background_color=user_data.get("background_color"),
            email=user_data.get("email"),
            first_name=user_data.get("first_name"),
            full_name=user_data.get("full_name"),
            is_active=user_data.get("is_active"),
            id=user_data.get("id"),
            joining_at=user_data.get("joining_at"),
            last_name=user_data.get("last_name"),
        )


def parse_organization(
    organization_data: Dict[str, Any]
) -> SwitchKeysOrganizationResponse:
    """
    Parse organization data.

    Args:
        organization_data (Dict[str, Any]): Organization data to be parsed.

    Returns:
        SwitchKeysOrganizationResponse: Parsed organization object.
    """

    return SwitchKeysOrganizationResponse(
        id=organization_data.get("id"),
        name=organization_data.get("name"),
        created=organization_data.get("created"),
        modified=organization_data.get("modified"),
        members=parse_user(organization_data.get("members")),
        owner=parse_user(organization_data.get("owner")),
    )


def parse_project(project_data: Dict[str, Any]) -> SwitchKeysProjectResponse:
    """
    Parse project data.

    Args:
        project_data (Dict[str, Any]): Project data to be parsed.

    Returns:
        SwitchKeysProjectResponse: Parsed project object.
    """

    return SwitchKeysProjectResponse(
        id=project_data.get("id"),
        name=project_data.get("name"),
        created=project_data.get("created"),
        modified=project_data.get("modified"),
        organization=parse_organization(project_data.get("organization")),
    )

def parse_auth(auth_data: Dict[str, Any]) -> SwitchKeysAuthResponse:
    """
    Parse auth data.

    Args:
        auth_data (Dict[str, Any]): Auth data to be parsed.

    Returns:
        SwitchKeysAuthResponse: Parsed project object.
    """

    return SwitchKeysAuthResponse(
        id=auth_data.get("id"),
        email=auth_data.get("email"),
        first_name=auth_data.get("first_name"),
        last_name=auth_data.get("last_name"),
        joining_at=auth_data.get("joining_at"),
        password=auth_data.get("password"),
        user_type=auth_data.get("user_type"),
        access_token=auth_data.get("access_token"),
        refresh_token=auth_data.get("refresh_token"),
    )
