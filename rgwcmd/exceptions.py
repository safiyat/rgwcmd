""" RGWCMD Exceptions """

class RgwcmdException(RuntimeError):
    """There was an unlabeled exception that was raised during your request"""
    def __init__(self, message="RADOS-GW error occured.", code=500):
        self._msg = message
        self._code = code

    def get_message(self):
        return self._msg

    def get_code(self):
        return self._code


class AccessDenied(RgwcmdException):
    """Access was denied for the request."""


class UserExists(RgwcmdException):
    """Attempt to create existing user."""


class MissingKeys(RgwcmdException):
    """Only access or secret key provided."""


class InvalidAccessKey(RgwcmdException):
    """Invalid access key specified."""


class InvalidArgument(RgwcmdException):
    """Invalid argument specified."""


class InvalidKeyType(RgwcmdException):
    """Invalid key type specified."""


class InvalidSecretKey(RgwcmdException):
    """Invalid secret key specified."""


class KeyExists(RgwcmdException):
    """Provided access key exists and belongs to another user."""


class EmailExists(RgwcmdException):
    """Provided email address exists."""


class SubuserExists(RgwcmdException):
    """Specified subuser exists."""


class InvalidAccess(RgwcmdException):
    """Invalid subuser access specified."""


class IndexRepairFailed(RgwcmdException):
    """Bucket index repair failed."""


class BucketNotEmpty(RgwcmdException):
    """Attempted to delete non-empty bucket."""


class ObjectRemovalFailed(RgwcmdException):
    """Unable to remove objects."""


class BucketUnlinkFailed(RgwcmdException):
    """Unable to unlink bucket from specified user."""


class BucketLinkFailed(RgwcmdException):
    """Unable to link bucket to specified user."""


class NoSuchObject(RgwcmdException):
    """Specified object does not exist."""


class IncompleteBody(RgwcmdException):
    """Either bucket was not specified for a bucket policy request or bucket
       and object were not specified for an object policy request."""


class InvalidCap(RgwcmdException):
    """Attempt to grant invalid admin capability."""


class NoSuchCap(RgwcmdException):
    """User does not possess specified capability."""


class InternalError(RgwcmdException):
    """Internal server error."""


class NoSuchUser(RgwcmdException):
    """User does not exist."""


class NoSuchBucket(RgwcmdException):
    """Bucket does not exist."""


class NoSuchKey(RgwcmdException):
    """No such access key."""


class ServerDown(RgwcmdException):
    """The backing server is not available."""


class InvalidQuotaType(RgwcmdException):
    """You must specify either a 'user' or 'bucket' quota type"""


class BucketAlreadyExists(RgwcmdException):
    """The bucket already exists"""
