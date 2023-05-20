from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = ''
    signup_timestamp: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user1 = User(**external_data)
print(user1.__repr__())
