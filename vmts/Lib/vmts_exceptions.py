# -*- coding: utf-8 -*-

from vmts_logger import VmtsLogger


class VmtsExceptions(Exception):
    """
    Base class of vmts exceptions.
    """

    def __init__(self, msg):
        self.msg = msg
        VmtsLogger('error').error(self.msg)

    def __str__(self):

        return self.msg


class RpcValidationError(VmtsExceptions):
    """
    json-rpc protocol validation error.
    will be raised when found errors on protocol structure.
    """

    def __init__(self, msg):
        self.msg = msg
        super(RpcValidationError, self).__init__(self.msg)


class LackParameterError(VmtsExceptions):
    """
    json-rpc protocol construction error.
    will be raised when number of parameters isn`t right.
    """

    def __init__(self):
        self.msg = 'Lack of parameter for constructing protocol.'
        super(LackParameterError, self).__init__(self.msg)


class TransformJsonError(VmtsExceptions):
    """
    json-rpc protocol construction error.
    will be raised when json-string cannot be resolved.
    """

    def __init__(self):
        self.msg = 'Unable to transform json-string into python-dict.'
        super(TransformJsonError, self).__init__(self.msg)


class DefaultConnectionPoolInitializationError(VmtsExceptions):
    """
    Redis connection-pool instance hadn`t been initialized yet.
    will be raised when trying to initialize Redis class before the initialization of Default Connection-pool.
    """

    def __init__(self):
        self.msg = 'Default ConnectionPool hadn`t been initialized yet.'
        super(DefaultConnectionPoolInitializationError, self).__init__(self.msg)
