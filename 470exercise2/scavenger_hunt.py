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


# make empty data and time Lists
LA_list = []
RV_list = []
RA_list = []
TL_list = []
TR_list = []

read_waveforms(LA_list, RV_list, RA_list)
read_times(TL_list, TR_list)

# convert all data and time lists to numpy arrays for plotting
LA = np.array(LA_list)
RV = np.array(RV_list)
RA = np.array(RA_list)
TL = np.array(TL_list[0])
TR = np.array(TR_list[0])
plot_waveforms(LA, RV, RA, TL, TR)

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


# PLA = np.max(LA)
# minMax = 0
# flag = True
# for i in LA_list:
#
#     maxLA.append(i)
#
# # for i in MLA:
# #     print(i)
# MLA = np.array(maxLA)
# # print(minMax)
# # print(MLA)
# # print(max(maxLA))
# print(maxLA)

MLA = np.array(minLA)
ALA = np.array(avgLA)
PLA = np.array(maxLA)

MRV = np.array(minRV)
ARV = np.array(avgRV)
PRV = np.array(maxRV)

MRA = np.array(minRA)
ARA = np.array(avgRA)
PRA = np.array(maxRA)
# print(np.min(PLA))
# print(np.max(PLA))
# print(np.mean(PLA))
print('MLA: min: ' + str(np.min(MLA)) + ', max: ' + str(np.max(MLA)) + ', avg: ' + str(np.mean(MLA)))
print('ALA: min: ' + str(np.min(ALA)) + ', max: ' + str(np.max(ALA)) + ', avg: ' + str(np.mean(ALA)))
print('PLA: min: ' + str(np.min(PLA)) + ', max: ' + str(np.max(PLA)) + ', avg: ' + str(np.mean(PLA)) + '\n')

print('MLA: min: ' + str(np.min(MRV)) + ', max: ' + str(np.max(MRV)) + ', avg: ' + str(np.mean(MRV)))
print('ARV: min: ' + str(np.min(ARV)) + ', max: ' + str(np.max(ARV)) + ', avg: ' + str(np.mean(ARV)))
print('PRV: min: ' + str(np.min(PRV)) + ', max: ' + str(np.max(PRV)) + ', avg: ' + str(np.mean(PRV)) + '\n')

print('MRA: min: ' + str(np.min(MRA)) + ', max: ' + str(np.max(MRA)) + ', avg: ' + str(np.mean(MRA)))
print('ARA: min: ' + str(np.min(ARA)) + ', max: ' + str(np.max(ARA)) + ', avg: ' + str(np.mean(ARA)))
print('PRA: min: ' + str(np.min(PRA)) + ', max: ' + str(np.max(PRA)) + ', avg: ' + str(np.mean(PRA)))

