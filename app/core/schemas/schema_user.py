from pydantic import BaseModel

class Schema_UserWSP(BaseModel):
    wsp_name : str
    wsp_number : str

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "wsp_name":"Diego",
                "wsp_number":"56981732415"
            }
        }