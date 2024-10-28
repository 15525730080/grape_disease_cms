from base_cms import UserGroup as LinUserGroup
from base_cms import db


class UserGroup(LinUserGroup):
    @classmethod
    def delete_batch_by_user_id_and_group_ids(cls, user_id, group_ids: list, commit=False):
        cls.query.filter_by(user_id=user_id).filter(cls.group_id.in_(group_ids)).delete(synchronize_session=False)
        if commit:
            db.session.commit()
