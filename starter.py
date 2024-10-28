"""
        :copyright: © 2020 by the  team.
        :license: MIT, see LICENSE for more details.
    """

from app import create_app
from app.api.cms.model.group import Group
from app.api.cms.model.group_permission import GroupPermission
from app.api.cms.model.permission import Permission
from app.api.cms.model.user import User
from app.api.cms.model.user_group import UserGroup
from app.api.cms.model.user_identity import UserIdentity
from app.config.code_message import MESSAGE

app = create_app(
    group_model=Group,
    user_model=User,
    group_permission_model=GroupPermission,
    permission_model=Permission,
    identity_model=UserIdentity,
    user_group_model=UserGroup,
    config_MESSAGE=MESSAGE,
)


if app.config.get("ENV") != "production":

    @app.route("/")
    def slogan():
        return

if __name__ == "__main__":
    app.logger.warning(
        """
        ----------------------------
        |  app.run() => flask run  |
        ----------------------------
        """
    )
    app.run()
