import hubo_ach as ha
import math
import ach
import sys
import time
import datetime
from ctypes import *

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
state = ha.HUBO_STATE()
ref = ha.HUBO_REF()

[statuss, framesizes] = s.get(state, wait=False, last=False)

ref.ref[ha.LHR] = 0.04
ref.ref[ha.RHR] = 0.04
ref.ref[ha.RAR] = -0.04
ref.ref[ha.LAR] = -0.04
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0.08
ref.ref[ha.RHR] = 0.08
ref.ref[ha.RAR] = -0.08
ref.ref[ha.LAR] = -0.08
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0.11
ref.ref[ha.RHR] = 0.11
ref.ref[ha.RAR] = -0.11
ref.ref[ha.LAR] = -0.11
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0.14
ref.ref[ha.RHR] = 0.14
ref.ref[ha.RAR] = -0.14
ref.ref[ha.LAR] = -0.14
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0.16
ref.ref[ha.RHR] = 0.16
ref.ref[ha.RAR] = -0.16
ref.ref[ha.LAR] = -0.16
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.1

r.put(ref)
ref.ref[ha.LHP] = -0.1
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.3
r.put(ref)
ref.ref[ha.LHP] = -0.2
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.4
r.put(ref)
ref.ref[ha.LHP] = -0.3
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.6
r.put(ref)
ref.ref[ha.LHP] = -0.4
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.8
r.put(ref)
ref.ref[ha.LHP] = -0.5
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1
r.put(ref)
ref.ref[ha.LHP] = -0.6
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.2
r.put(ref)
ref.ref[ha.LHP] = -0.7
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.4
r.put(ref)
time.sleep(4);
ref.ref[ha.LHP] = -0.9
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.6
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.8
r.put(ref)
time.sleep(4);
ref.ref[ha.LHP] = -1
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 2
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 2.1
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 2.5
r.put(ref)
time.sleep(4);
i = 0
while i<2:
	i = i+1
	ref.ref[ha.RKN] = .5
	ref.ref[ha.RHP] = -0.25
	ref.ref[ha.RAP] = -0.25
	r.put(ref)
	time.sleep(4);
	ref.ref[ha.RKN] = 0.7
	ref.ref[ha.RHP] = -.35
	ref.ref[ha.RAP] = -.35
	r.put(ref)
	time.sleep(3);
	ref.ref[ha.RKN] = 1
	ref.ref[ha.RHP] = -0.5
	ref.ref[ha.RAP] = -0.5
	r.put(ref)
	time.sleep(3);
	ref.ref[ha.RKN] = 1.3
	ref.ref[ha.RHP] = -0.65
	ref.ref[ha.RAP] = -0.65
	r.put(ref)
	time.sleep(4);
	ref.ref[ha.RKN] = 1
	ref.ref[ha.RHP] = -0.5
	ref.ref[ha.RAP] = -0.5
	ref.ref[ha.RSR] = -0.2
	r.put(ref)
	time.sleep(3);
	ref.ref[ha.RKN] = 0.7
	ref.ref[ha.RHP] = -.35
	ref.ref[ha.RAP] = -.35
	r.put(ref)
	time.sleep(3);

ref.ref[ha.LKN] = 2.1
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 2.5
r.put(ref)
time.sleep(4);
ref.ref[ha.LHP] = -1
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 2
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.6
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.8
r.put(ref)
time.sleep(4);
ref.ref[ha.LHP] = -0.9
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.4
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1.2
r.put(ref)
################3
ref.ref[ha.LHP] = -0.7
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 1
r.put(ref)
ref.ref[ha.LHP] = -0.6
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.8
r.put(ref)
ref.ref[ha.LHP] = -0.5
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.6
r.put(ref)
ref.ref[ha.LHP] = -0.4
r.put(ref)
time.sleep(4);
ref.ref[ha.LKN] = 0.4
r.put(ref)
ref.ref[ha.LHP] = -0.3
r.put(ref)
ref.ref[ha.LKN] = 0.3
r.put(ref)
ref.ref[ha.LHP] = -0.2
r.put(ref)
r.put(ref)
ref.ref[ha.LHP] = -0.1
r.put(ref)
time.sleep(4);



ref.ref[ha.LHR] = 0.14
ref.ref[ha.RHR] = 0.14
ref.ref[ha.RAR] = -0.14
ref.ref[ha.LAR] = -0.04
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0.11
ref.ref[ha.RHR] = 0.11
ref.ref[ha.RAR] = -0.11
ref.ref[ha.LAR] = -0.11
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0.8
ref.ref[ha.RHR] = 0.8
ref.ref[ha.RAR] = -0.8
ref.ref[ha.LAR] = -0.8
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0.4
ref.ref[ha.RHR] = 0.4
ref.ref[ha.RAR] = -0.4
ref.ref[ha.LAR] = -0.4
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = 0
ref.ref[ha.RHR] = 0
ref.ref[ha.RAR] = 0
ref.ref[ha.LAR] = 0
r.put(ref)
time.sleep(4);

ref.ref[ha.LHR] = -0.04
ref.ref[ha.RHR] = -0.04
ref.ref[ha.RAR] = 0.04
ref.ref[ha.LAR] = 0.04
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = -0.08
ref.ref[ha.RHR] = -0.08
ref.ref[ha.RAR] = 0.08
ref.ref[ha.LAR] = 0.08
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = -0.11
ref.ref[ha.RHR] = -0.11
ref.ref[ha.RAR] = 0.11
ref.ref[ha.LAR] = 0.11
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = -0.14
ref.ref[ha.RHR] = -0.14
ref.ref[ha.RAR] = 0.14
ref.ref[ha.LAR] = 0.14
r.put(ref)
time.sleep(4);
ref.ref[ha.LHR] = -0.16
ref.ref[ha.RHR] = -0.16
ref.ref[ha.RAR] = 0.16
ref.ref[ha.LAR] = 0.16
r.put(ref)
time.sleep(4);


r.put(ref)
ref.ref[ha.RHP] = -0.1
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 0.3
r.put(ref)
ref.ref[ha.RHP] = -0.2
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 0.4
r.put(ref)
ref.ref[ha.RHP] = -0.3
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 0.6
r.put(ref)
ref.ref[ha.RHP] = -0.4
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 0.8
r.put(ref)
ref.ref[ha.RHP] = -0.5
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1
r.put(ref)
ref.ref[ha.RHP] = -0.6
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.2
r.put(ref)
ref.ref[ha.RHP] = -0.7
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.4
r.put(ref)
time.sleep(4);
ref.ref[ha.RHP] = -0.9
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.6
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.8
r.put(ref)
time.sleep(4);
ref.ref[ha.RHP] = -1
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 2
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 2.1
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 2.5
r.put(ref)
time.sleep(4);


i = 0
while i<2:
	i = i+1
	ref.ref[ha.LKN] = .5/2
	ref.ref[ha.LHP] = -0.25/2
	ref.ref[ha.LAP] = -0.25/2
	r.put(ref)
	time.sleep(4);
	ref.ref[ha.LKN] = 0.7/2
	ref.ref[ha.LHP] = -.35/2
	ref.ref[ha.LAP] = -.35/2
	r.put(ref)
	time.sleep(3);
	ref.ref[ha.LKN] = 1/2
	ref.ref[ha.LHP] = -0.5/2
	ref.ref[ha.LAP] = -0.5/2
	r.put(ref)
	time.sleep(3);
	ref.ref[ha.LKN] = 1.3/2
	ref.ref[ha.LHP] = -0.65/2
	ref.ref[ha.LAP] = -0.65/2
	r.put(ref)
	time.sleep(4);
	ref.ref[ha.LKN] = 1/2
	ref.ref[ha.LHP] = -0.5/2
	ref.ref[ha.LAP] = -0.5/2
	ref.ref[ha.LSR] = 0.2/2
	r.put(ref)
	time.sleep(3);
	ref.ref[ha.LKN] = 0.7/2
	ref.ref[ha.LHP] = -.35/2
	ref.ref[ha.LAP] = -.35/2
	r.put(ref)
	time.sleep(3);

ref.ref[ha.RKN] = 2.1
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 2.5
r.put(ref)
time.sleep(4);
ref.ref[ha.RHP] = -1
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 2
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.6
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.8
r.put(ref)
time.sleep(4);
ref.ref[ha.RHP] = -0.9
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.4
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1.2
r.put(ref)
################3
ref.ref[ha.RHP] = -0.7
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 1
r.put(ref)
ref.ref[ha.RHP] = -0.6
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 0.8
r.put(ref)
ref.ref[ha.RHP] = -0.5
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 0.6
r.put(ref)
ref.ref[ha.RHP] = -0.4
r.put(ref)
time.sleep(4);
ref.ref[ha.RKN] = 0.4
r.put(ref)
ref.ref[ha.RHP] = -0.3
r.put(ref)
ref.ref[ha.RKN] = 0.3
r.put(ref)
ref.ref[ha.RHP] = -0.2
r.put(ref)
r.put(ref)
ref.ref[ha.RHP] = -0.1
r.put(ref)
time.sleep(4);























# Close the connection to the channels
r.close()
s.close()
