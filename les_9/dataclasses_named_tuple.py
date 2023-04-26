from collections import namedtuple
from dataclasses import dataclass

some_ob = namedtuple('SomeObj', 'name')
some_ob.name = 12

print(some_ob.name)

###########################################################################


@dataclass
class User:
    name: str
    password: str
