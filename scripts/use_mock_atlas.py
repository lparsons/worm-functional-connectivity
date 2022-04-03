import numpy as np
import matplotlib.pyplot as plt
import wormfunconn as wfc
import os

# Get atlas folder
folder = os.path.join(os.path.dirname(__file__),"../atlas/")

# Create FunctionalAtlas instance from file
funatlas = wfc.FunctionalAtlas.from_file(folder,"mock")

# Generate the stimulus array
nt = 1000 # Number of time points 
dt = 0.1 # Time step
stim_type="rectangular" # Type of standard stimulus
dur = 1. # Duration of the stimulus
stim = funatlas.get_standard_stimulus(nt,dt=dt,stim_type=stim_type,duration=dur)

# Get the responses
stim_neu_id = "AVAL"
resp_neu_ids = ["AVAL","AVAR","ASEL","AWAL","wrong_id"]
resp, labels, msg = funatlas.get_responses(stim, dt, stim_neu_id, resp_neu_ids=None,top_n=5)

print(msg)
# Plot
time = np.arange(nt)*dt
for i in np.arange(resp.shape[0]):
    plt.plot(time,resp[i],label=labels[i])
plt.legend()
plt.show()
