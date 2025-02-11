from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attribute=True)
    
    id: Optional[int]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None