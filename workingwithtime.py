### SAMPLE PRACTICE CODE for working and dealing with TIME and DATES ###

import datetime as dt
from datetime import datetime, deltatime, timezone
import tz

dt.tz_localize('America/Houston')
dt.tz_convert('America/Houston')

def function(param1, param2=None, *args, **kwargs):
    """The type and description of each parameter is optional, but should be included if not obvious.
    If \*args or \*\*kwargs are accepted, they should be listed as ``*args`` and ``**kwargs``.
    
    Args:
        param1 (int): The first parameter example.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented for long descriptions.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        bool: True if successful, False otherwise.
        The return type is optional and may be specified at the beginning of the ``Returns`` section followed by a colon.
        Following lines should be indented to match the first line. The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::
            {
                'param1': param1,
                'param2': param2
            }
    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True
    
