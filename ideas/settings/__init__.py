# https://github.com/codingforentrepreneurs/Guides/blob/master/all/Create_a_Local_Django_Project.md
from .base import *

from .production import *

try:
   from .local import *
except:
   pass