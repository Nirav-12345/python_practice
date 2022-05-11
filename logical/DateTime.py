import time
from datetime import datetime

print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("Elapsed time : %s" % time.ctime())
t = datetime.now()
print("Elapsed Time",t.second)

