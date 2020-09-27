# GITHUB.COM/FSWAIR | @FLUSWAIR
from datetime import datetime
now=datetime.now()

# 1-2 digits number generate; int( now second % now day * now minute / 100 )
number = int(now.second % now.day / now.minute * 100)
print(number)
