"""
module user have a class User and object user
"""
# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
# pylint: disable=no-member
# pylint: disable=no-name-in-module
# pylint: disable=import-error
# pylint: disable=too-many-instance-attributes
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin


class User:
    """
    User class have main field  that describe user
    """

    def __init__(self, id, username, first_name, last_name, email, password, phone, user_status):
        self.id = id
        self.username = username
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = user_status
