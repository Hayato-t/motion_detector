import matplotlib.pyplot as plt
import numpy
import sys

args = sys.argv
args.pop(0)
if len(args) == 0:
    print("need more than 1 file.")
    exit()
else:
    spike_time = []
    spike_channel = []
    for arg in args:
        for line in open(arg,'r'):
            split_line = line[:-1].split('\t')
            spike_time.append(split_line[0])
            spike_channel.append(split_line[1])
    plt.plot(spike_time, spike_channel, '.')
    plt.show()

