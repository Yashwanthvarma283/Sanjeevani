from pydantic import BaseModel

class userCreation(BaseModel):
    name:str
    
class userResponse(BaseModel):
    id:int
    name:str
    class config:
        from_attributes=True
    