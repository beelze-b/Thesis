import pyfits
import matplotlib
import numpy as np

matplotlib.use('Agg')

import matplotlib.pyplot as plt


catalog = pyfits.getdata('MatchHellHSCMags2.fits')

starIndices = np.where(catalog['mu_class'] == 2)[0]
galIndices = np.where(catalog['mu_class'] == 1)[0]

def MagnitudeErrorPlot(magnitudes, errors, bandString, starboolean):
    fig = plt.figure()
    if starboolean:
        stargal = 'Stars'
    else:
        stargal = 'Galaxies'
    title = 'Distribution of Magnitudes and Errors of ' + stargal + ' for Band ' + bandString
    filename = 'data/magnitude_error/' + stargal + bandString + '.png'

    # get the ones that are not numbers
    magnitudeIndices = np.where(np.logical_not(np.isnan(magnitudes)))[0]
    errorsIndices = np.where(np.logical_not(np.isnan(errors)))[0]
    indices = np.array(list(set(magnitudeIndices.tolist() + errorsIndices.tolist())))
    magnitudes = magnitudes[indices]
    errors = errors[indices]

    plt.title(title)

    ax = plt.gca()
    plt.scatter(magnitudes, errors)

    ax.set_ylabel('Mag (AB)')
    ax.set_xlabel('Mag (AB)')

    # to get nice ranges
    # this needs to happen after plotting otherwise plot gets messed up

    # do it for x
    xticks, xticklabels = plt.xticks()
    # shift half a step to the left
    # x0 - (x1 - x0) / 2 = (3 * x0 - x1) / 2
    xmin = (3*xticks[0] - xticks[1])/2.
    # shift half a step to the right
    xmax = (3*xticks[-1] - xticks[-2])/2.
    plt.xlim(xmin, xmax)
    plt.xticks(xticks)

    # do it for y
    yticks, yticklabels = plt.yticks()
    # shift half a step to the left
    # x0 - (x1 - x0) / 2 = (3 * x0 - x1) / 2
    ymin = (3*yticks[0] - yticks[1])/2.
    # shaft half a step to the right
    ymax = (3*yticks[-1] - yticks[-2])/2.
    plt.ylim(ymin, ymax)
    plt.yticks(yticks)


    plt.savefig(filename)
    plt.close(fig)

MagnitudeErrorPlot(catalog['magR'][starIndices], catalog['magRError'][starIndices], 'R', 1)
MagnitudeErrorPlot(catalog['magI'][starIndices], catalog['magIError'][starIndices], 'I', 1)
MagnitudeErrorPlot(catalog['magZ'][starIndices], catalog['magZError'][starIndices], 'Z', 1)

MagnitudeErrorPlot(catalog['mag_j'][starIndices], catalog['mag_j_error'][starIndices], 'J', 1)
MagnitudeErrorPlot(catalog['mag_h'][starIndices], catalog['mag_h_error'][starIndices], 'H', 1)
MagnitudeErrorPlot(catalog['mag_k'][starIndices], catalog['mag_k_error'][starIndices], 'K', 1)

MagnitudeErrorPlot(catalog['mag_36'][starIndices], catalog['mag_45error'][starIndices], r'$3.6\mu{}m$', 1)
MagnitudeErrorPlot(catalog['mag_45'][starIndices], catalog['mag_36error'][starIndices], r'$4.5\mu{}m$', 1)

MagnitudeErrorPlot(catalog['magR'][galIndices], catalog['magRError'][galIndices], 'R', 0)
MagnitudeErrorPlot(catalog['magI'][galIndices], catalog['magIError'][galIndices], 'I', 0)
MagnitudeErrorPlot(catalog['magZ'][galIndices], catalog['magZError'][galIndices], 'Z', 0)

MagnitudeErrorPlot(catalog['mag_j'][galIndices], catalog['mag_j_error'][galIndices], 'J', 0)
MagnitudeErrorPlot(catalog['mag_h'][galIndices], catalog['mag_h_error'][galIndices], 'H', 0)
MagnitudeErrorPlot(catalog['mag_k'][galIndices], catalog['mag_k_error'][galIndices], 'K', 0)

MagnitudeErrorPlot(catalog['mag_36'][galIndices], catalog['mag_45error'][galIndices], r'$3.6\mu{}m$', 0)
MagnitudeErrorPlot(catalog['mag_45'][galIndices], catalog['mag_36error'][galIndices], r'$4.5\mu{}m$', 0)

