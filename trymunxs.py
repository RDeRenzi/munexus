import munxs as nxs
import time
import numpy as np
import matplotlib.pyplot as P
tic = time.time()
path = '/home/roberto.derenzi/Downloads/mantid/muon_cupper/EMU00020882.nxs'
run = nxs.NeXusTree(path,'r')
#run.readfile()
run.opengrouppath(b'/run')
start_date = run.readpath(b'start_time').decode('utf-8')
run.opengrouppath(b'/run')
stop_date = run.readpath(b'stop_time').decode('utf-8')
run.opengrouppath(b'/run/sample')
temperature = run.readpath(b'temperature') # float32
run.opengrouppath(b'/run/sample')
orient = run.readpath(b'shape').decode('utf-8')
run.opengrouppath(b'/run/histogram_data_1')
y = run.readpath(b'counts') # int32
run.opengrouppath(b'/run/histogram_data_1')
resps = float(run.readpath(b'resolution'))
run.opengrouppath(b'/run/temperature_log_1')
T=run.readpath(b'values') # float32
toc = time.time()
dt = time.mktime(time.strptime(stop_date,'%Y-%m-%dT%H:%M:%S')) - time.mktime(time.strptime(start_date,'%Y-%m-%dT%H:%M:%S'))
t=np.linspace(0,dt,T.shape[0])
f,ax = P.subplots()
ax.plot(t,T)
f,ax = P.subplots(10,10,figsize=(10,10))
t = np.linspace(-0.231,31.769,2000)
#print('shape t = {}'.format(t.shape))
j=0
for k in range(10):
    for l in range(10):
        if j<96:
            ax[k,l].plot(t,y[j,:])
            j += 1
P.show()
print ('total time = {}'.format(toc-tic))

