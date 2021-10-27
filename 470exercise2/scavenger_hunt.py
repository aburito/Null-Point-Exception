import matplotlib.pyplot as plt
import numpy as np


def read_waveforms(LA, RV, RA):
    infile = open('data/waveforms.csv', 'r')

    line = infile.readline()
    wf = 0  # which waveform are we trying to read (0 = LA, 1 = RV, 2 = RA)

    while line:
        line = line.strip()
        data = line.split(',')

        for i in range(0, len(data)):
            data[i] = float(data[i])

        if (wf == 0):
            LA.append(data)
        elif (wf == 1):
            RV.append(data)
        elif (wf == 2):
            RA.append(data)

        wf = (wf + 1) % 3
        line = infile.readline()

    infile.close()


def read_times(TL, TR):
    infile = open('data/times.csv', 'r')
    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)):
        data[i] = float(data[i]) * 1000

    TL.append(data)

    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)):
        data[i] = float(data[i]) * 1000

    TR.append(data)
    infile.close()


def plot_waveforms(LA, RV, RA, TL, TR):
    plt.plot(TL, LA[6, :])
    plt.title('Linear Acceleration of Instance 7')
    plt.xlabel('Time (ms)')
    plt.ylabel('Lin Accel (g)')
    plt.xticks(np.arange(0, 55, step=5))
    plt.savefig('graphs/Linear Acceleration of Instance 7.png')

    for i in range(0, 65):
        plt.subplot(311)
        plt.plot(TL, LA[i, :])
        plt.title('Waveforms for Instance ' + str(i + 1))
        plt.ylabel('Lin Accel (g)')
        plt.xticks(np.arange(0, 55, step=5))

        plt.subplot(312)
        plt.plot(TR, RV[i, :])
        plt.ylabel('Rot Vel (rad/sec)')
        plt.xticks(np.arange(0, 55, step=5))

        plt.subplot(313)
        plt.plot(TR, RA[i, :])
        plt.xlabel('Time (ms)')
        plt.ylabel('Rot Accel (rad/sec^2)')
        plt.xticks(np.arange(0, 55, step=5))

        plt.savefig('graphs/Instance ' + str(i + 1) + '.png')
        plt.close()


def plot_scatterplot(PLA, PRV, PRA):
    plt.scatter(PLA, PRV)
    plt.xlabel('Linear Acceleration (g)')
    plt.ylabel('Rotational Velocity (rad/sec)')
    plt.title('Peak Linear Acceleration (g) vs. Peak  Rotational Velocity (rad/sec)')
    plt.savefig('graphs/Linear Acceleration vs. Rotational Velocity.png')
    plt.close()
    print('\ngraphs/Linear Acceleration vs. Rotational Velocity.png printed \n')

    plt.scatter(PLA, PRA)
    plt.xlabel('Linear Acceleration (g)')
    plt.ylabel('Rotational Acceleration (rad/sec^2)')
    plt.title('Peak Linear Acceleration (g) vs. Peak Rotational Acceleration (rad/sec^2)')
    plt.savefig('graphs/Linear Acceleration vs. Rotational Acceleration.png')
    plt.close()
    print('graphs/Linear Acceleration vs. Rotational Acceleration.png printed\n')

    plt.scatter(PRV, PRA)
    plt.xlabel('Rotational Velocity (rad/sec)')
    plt.ylabel('Rotational Acceleration (rad/sec^2)')
    plt.title('Peak Rotational Velocity (rad/sec) vs. Peak Rotational Acceleration (rad/sec^2)')
    plt.savefig('graphs/Rotational Velocity vs. Rotational Acceleration.png')
    plt.close()
    print('graphs/Rotational Velocity vs. Rotational Acceleration.png printed')

def plot_rot_accel(RA):
    for i in range(0,65):
        instances.append(i)
    plt.xlabel('Instance')
    plt.ylabel('Rotational Acceleration (rad/sec^2)')
    plt.title('Average Rotational Acceleration')
    plt.savefig('graphs/Average Rotational Acceleration.png')

# make empty data and time Lists
LA_list = []
RV_list = []
RA_list = []
TL_list = []
TR_list = []
instances = []

read_waveforms(LA_list, RV_list, RA_list)
read_times(TL_list, TR_list)

# convert all data and time lists to numpy arrays for plotting
LA = np.array(LA_list)
RV = np.array(RV_list)
RA = np.array(RA_list)
TL = np.array(TL_list[0])
TR = np.array(TR_list[0])
# plot_waveforms(LA, RV, RA, TL, TR)

# plot_rot_accel(RA)

minLA = []
avgLA = []
maxLA = []

minRV = []
avgRV = []
maxRV = []

minRA = []
avgRA = []
maxRA = []

for i in range(0, 65):
    minLA.append(np.min(LA[i]))
    avgLA.append(np.mean(LA[i]))
    maxLA.append(np.max(LA[i]))

    minRV.append(np.min(RV[i]))
    avgRV.append(np.mean(RV[i]))
    maxRV.append(np.max(RV[i]))

    minRA.append(np.min(RA[i]))
    avgRA.append(np.mean(RA[i]))
    maxRA.append(np.max(RA[i]))

MLA = np.array(minLA)
ALA = np.array(avgLA)
PLA = np.array(maxLA)

MRV = np.array(minRV)
ARV = np.array(avgRV)
PRV = np.array(maxRV)

MRA = np.array(minRA)
ARA = np.array(avgRA)
PRA = np.array(maxRA)

# plot_scatterplot(PLA, PRV, PRA)
#
# print('MLA: min: ' + str(np.min(MLA)) + ', max: ' + str(np.max(MLA)) + ', avg: ' + str(np.mean(MLA)))
# print('ALA: min: ' + str(np.min(ALA)) + ', max: ' + str(np.max(ALA)) + ', avg: ' + str(np.mean(ALA)))
# print('PLA: min: ' + str(np.min(PLA)) + ', max: ' + str(np.max(PLA)) + ', avg: ' + str(np.mean(PLA)) + '\n')
#
# print('MLA: min: ' + str(np.min(MRV)) + ', max: ' + str(np.max(MRV)) + ', avg: ' + str(np.mean(MRV)))
# print('ARV: min: ' + str(np.min(ARV)) + ', max: ' + str(np.max(ARV)) + ', avg: ' + str(np.mean(ARV)))
# print('PRV: min: ' + str(np.min(PRV)) + ', max: ' + str(np.max(PRV)) + ', avg: ' + str(np.mean(PRV)) + '\n')
#
# print('MRA: min: ' + str(np.min(MRA)) + ', max: ' + str(np.max(MRA)) + ', avg: ' + str(np.mean(MRA)))
# print('ARA: min: ' + str(np.min(ARA)) + ', max: ' + str(np.max(ARA)) + ', avg: ' + str(np.mean(ARA)))
# print('PRA: min: ' + str(np.min(PRA)) + ', max: ' + str(np.max(PRA)) + ', avg: ' + str(np.mean(PRA)))
bigMaxLA = maxLA
bigMaxRA = maxRA
bigMaxRV = maxRV

bigMaxLA.sort()
bigMaxLA = bigMaxLA[-5:]

for i in LA:
    if i == bigMaxLA[0]:
        print(i)
    elif i == bigMaxLA[1]:
        print(i)
    elif i == bigMaxLA[2]:
        print(i)
    elif i == bigMaxLA[3]:
        print(i)
    elif i == bigMaxLA[4]:
        print(i)
# for i in


# for k in LA:
#     for i in bigMaxLA:
#         if i == k:
#             # print(i)
#             print(LA.index(k))

bigMaxRA.sort()
# print(bigMaxRA[-5:])

bigMaxRV.sort()
# print(bigMaxRV[-5:])