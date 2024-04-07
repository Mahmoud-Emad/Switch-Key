from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from switchkeys.api.permissions import (
    UserIsAuthenticated,
)
from switchkeys.api.custom_response import CustomResponse
from switchkeys.serializers.users import OrganizationUserSerializer
from switchkeys.services.users import get_user_by_id, get_all_users


class BaseGeneralUserAPIView(ListAPIView, GenericAPIView):
    permission_classes = [UserIsAuthenticated]
    serializer_class = OrganizationUserSerializer

    def get_queryset(self) -> Response:
        """get all users in the system for a normal user"""
        query_set = get_all_users()
        return query_set


class GeneralUserAPIView(GenericAPIView):
    permission_classes = [UserIsAuthenticated]
    serializer_class = OrganizationUserSerializer

    def get(self, request: Request, id: str) -> Response:
        """To get a user by id"""
        user = get_user_by_id(id)
        if user is not None:
            return CustomResponse.success(
                data=self.get_serializer(user).data,
                message="User found",
                status_code=200,
            )
        return CustomResponse.not_found(message="User not found", status_code=404)
