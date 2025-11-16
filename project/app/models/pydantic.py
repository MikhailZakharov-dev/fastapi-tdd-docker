from pydantic import BaseModel

class SymmaryPayloadSchema(BaseModel):
  url: str
  
