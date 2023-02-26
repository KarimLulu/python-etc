import os
from contextlib import chdir


print('before:', os.getcwd())
# before: /home/gram
with chdir('/'):
    print('inside:', os.getcwd())
    # inside: /
print('after:', os.getcwd())
# after: /home/gram
