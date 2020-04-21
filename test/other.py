# other.py
print('__name__:', __name__)
from .cool import cool_func

print('Call it remotely')
cool_func()