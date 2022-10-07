# Packages
from typing import List, Union
from dataclasses import dataclass, field


@dataclass
class ReturnValue:
    """
    ReturnValue class is responsible for holding returned value from operations

    Args:
        success: True if operation is successful otherwise False
        message: message after successful operation
        error: error message after failed operation
        data: resulted data after operation completion
    """
    success: bool
    message: str = ""
    error: str = ""
    data: Union[List, dict, str, tuple] = field(default_factory=list)
