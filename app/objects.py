from dataclasses import dataclass

        
@dataclass
class ControllerResult:
    is_success: bool
    message: str
    data: dict
    
        