"""Custom Exceptions needed to not couple controller layer to specific framework"""

class ResourseNotFoundException(Exception):
    """For 404 HTTP codes"""

class OperationNotAllowedException(Exception):
    """For 405 HTTP codes"""

class ValueErrorException(Exception):
    """For 422 HTTP codes"""
