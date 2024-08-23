import numpy as np
import matplotlib.pyplot as plt

def read_forces(fn):
    time, total_x, total_y, total_z, _, _, _, _, _, _ = np.loadtxt(
        fn, unpack=True)
    F = np.array([total_x, total_y, total_z])
    return time, F

time, F_tot = read_forces('postProcessing/forces/0/force.dat')
_   , M_tot = read_forces('postProcessing/forces/0/moment.dat')

print('Final total force:     {} N'.format(F_tot[:, -1]))
print('Final total moment z:  {} N.m'.format(M_tot[-1, -1]))
print('')

plt.plot(time, F_tot[0, :], label='Total force x')
plt.plot(time, F_tot[1, :], label='Total force y')
plt.plot(time, F_tot[2, :], label='Total force z')

m = len(time)

maxF = np.max(np.abs(F_tot[:, m//2:]))
plt.ylim([-1.5*maxF, 1.5*maxF])

plt.grid()
plt.xlabel('Time (-)')
plt.ylabel('Force (N)')
plt.legend()
plt.tight_layout()
plt.savefig('forces.pdf')

plt.figure()
plt.plot(time, M_tot[0, :], label='Total moment x')
plt.plot(time, M_tot[1, :], label='Total moment y')
plt.plot(time, M_tot[2, :], label='Total moment z')

maxM = np.max(np.abs(M_tot[:, m//2:]))
plt.ylim([-1.5*maxM, 1.5*maxM])

plt.grid()
plt.xlabel('Time (-)')
plt.ylabel('Moment (N.m)')
plt.legend()
plt.tight_layout()
plt.savefig('moments.pdf')

plt.close()
