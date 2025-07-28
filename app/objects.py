from dataclasses import dataclass
from flask import Response

        
@dataclass
class ControllerResult:
    is_success: bool
    message: str
    http_status: Response
    data: dict
    
        