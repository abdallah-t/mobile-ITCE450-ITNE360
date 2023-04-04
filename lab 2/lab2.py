import numpy as np
import matplotlib.pyplot as plt


d = np.arange(1, 1000, 1)
f = [900, 1800]
Gt = 28


def free_space_path_loss(d, f, Gt):
    # d - distance in m
    # f - frequency in MHz
    # return - path loss in dB
    path_loss = 32.45 + 20 * np.log10(d) + 20 * np.log10(f) - Gt
    return path_loss


def CCIR_path_loss(d, f, b, hb, hm):
    # d - distance in m
    # f - frequency in MHz
    # hb - height of base station in m
    # hm - height of mobile station in m
    # b - area covered by building in percentage
    # return - path loss in dB
    a = (1.1 * np.log10(f) - 0.7) * hm - (1.56 * np.log10(f) - 0.8)
    path_loss = 69.55 + 26.16 * \
        np.log10(f) - 13.82 * np.log10(hb) - a + \
        (44.9 - 6.55 * np.log10(hb)) * np.log10(d) - b
    return path_loss

# done check it out


def Hata_Model_medium_city(f, h):
    # f carrier frequency
    # h height of moblie anttena hm
    path_loss = (1.1*np.log10(f)-0.7)*h-(1.56*np.log10(f)-0.8)
    return path_loss


def Hata_Model_large_city(h, f):
    # f carrier frequency
    # h height of moblie anttena hm
    if f <= 300:
        path_loss = 8.29*np.power((np.log10(1.54*h)), 2)-1.1
    else:
        path_loss = 3.2*np.power((np.log10(11.75*h), 2))-4.97
    return path_loss


def Hata_Model_urban(f, h, hr, d):
    # f carrier frequency
    # hr height of moblie anttena hm
    # h height of base station
    # d distance between transmitter and receiver in km
    a = (1.1 * np.log10(f) - 0.7) * hr - (1.56 * np.log10(f) - 0.8)
    path_loss = 69.55+26.16 * \
        np.log10(f)-13.82*np.log10(h)-a+(44.9-6.55*np.log10(h))*np.log10(d)
    return path_loss


def Hata_Model_suburban(f, h, hr, d):
    # f carrier frequency
    # h height of base station
    # d distance between transmitter and receiver in km
    path_loss = Hata_Model_urban(f, h, hr, d)-2 * \
        np.power((np.log10(f/28)), 2) - 5.4
    return path_loss


def Hata_Model_rural(f, h, d):
    # f carrier frequency
    # h height of base station
    # d distance between transmitter and receiver in km
    path_loss = Hata_Model_urban(
        f, h, hr, d)-4.78*np.power(np.log10(f), 2)+18.33*np.log10(f)-40.98
    return path_loss


def plot_default(title):
    plt.legend()
    plt.xlabel('Distance (m)')  # Add a label for the x-axis
    plt.ylabel('Path loss (dB)')
    plt.title(f'{title}')


CCIR_path_loss_1 = CCIR_path_loss(d, f[0], 0.35, 35, 1)
CCIR_path_loss_2 = CCIR_path_loss(d, f[1], 0.35, 35, 1)
path_loss = free_space_path_loss(d, f[0], Gt)
path_loss_2 = free_space_path_loss(d, f[1], Gt)


fig1 = plt.figure(1)
plt.plot(d, path_loss, label='900 MHz')
plot_default("free_space_path_loss")


fig2 = plt.figure(2)
plt.plot(d, path_loss_2, 'r', label='1800 MHz')
plot_default("free_space_path_loss")


fig3 = plt.figure(3)
plt.plot(d, path_loss, label='900 MHz')
plt.plot(d, path_loss_2, 'r', label='1800 MHz')
plot_default("free_space_path_loss")


fig4 = plt.figure(4)
plt.plot(d, CCIR_path_loss_2, 'r', label='1800 MHz')
plot_default("CCIR_path_loss")


fig5 = plt.figure(5)
plt.plot(d, CCIR_path_loss_1, label='900 MHz')
plt.plot(d, CCIR_path_loss_2, 'r', label='1800 MHz')
plot_default("CCIR_path_loss")

fig6 = plt.figure(6)
plt.plot(d, Hata_Model_rural(f[0], 35, d), label='900 MHz')
plt.plot(d, Hata_Model_rural(f[1], 35, d), 'r', label='1800 MHz')
plot_default("Hata_Model_rural")

fig7 = plt.figure(7)
plt.plot(d, Hata_Model_suburban(f[0], 35, d), label='900 MHz')
plt.plot(d, Hata_Model_suburban(f[1], 35, d), 'r', label='1800 MHz')
plot_default("Hata_Model_suburban")

fig8 = plt.figure(8)
plt.plot(d, Hata_Model_urban(f[0], 35), label='900 MHz')
plt.plot(d, Hata_Model_urban(f[1], 35), 'r', label='1800 MHz')


fig10 = plt.figure(9)
plt.plot(d, Hata_Model_large_city(35, f[0]), label='900 MHz')
plt.plot(d, Hata_Model_large_city(35, f[1]), 'r', label='1800 MHz')


fig11 = plt.figure(10)
plt.plot(d, Hata_Model_medium_city(f[0], 35), label='900 MHz')
plt.plot(d, Hata_Model_medium_city(f[1], 35), 'r', label='1800 MHz')

plt.show()
