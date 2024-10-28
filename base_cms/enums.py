"""
    enums of Lin
    ~~~~~~~~~
    :copyright: © 2020 by the fanbozhou.
    :license: MIT, see LICENSE for more details.
"""
from enum import Enum


# status for user is admin
# 是否为超级管理员的枚举
class GroupLevelEnum(Enum):
    ROOT = 1
    GUEST = 2
    USER = 3
