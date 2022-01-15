from math import cos, log10, pi
from numpy import abs
from . import thinkdsp

samples_per_frame = 256


def split(input_file):
    """ Splits audio file into frames
    and applies hamming window.
    :param input_file: path to audio file
    :return: array of waves (frames)
    """
    frames = []
    wave = thinkdsp.read_wave(input_file)

  
    totframes = len(wave.ts)
    framerate = wave.framerate
    length = totframes / framerate
    framelength = samples_per_frame / framerate
    numframes = int(length / framelength)


    for index in range(numframes):

        currentstart = index * framelength
        frames.append(wave.segment(start=currentstart, duration=framelength))

    return frames, framelength

def applyhamming(framearray):
    """Multiplying each frame with a hamming window
    :param framearray: array of waves (frames)
    :return: array of hamming window filtered frames
    """
    pi2 = 2 * pi
    hammingwindow = []

    for index in range(samples_per_frame):
        hammingwindow.append((0.54 + 0.46 * (cos(pi2 * index / 255))))

    for framenumber in range(len(framearray)):
        for samplenumber in range(len(hammingwindow)):
            framearray[framenumber].ys[samplenumber] *= hammingwindow[samplenumber]

    return framearray


def energy(framearray):
    """ Calculates the energy of each frame
    :param framearray: array of waves (frames)
    :return: array of energy per frame
    """

    frame_energy = []

    for framenumber in range(len(framearray)):
        frame_energy.append([0])
        for samplenumber in range(samples_per_frame):
            frame_energy[framenumber] += ((framearray[framenumber].ys[samplenumber])**2)
    return frame_energy


def fourier(framearray):
    """ Fourier transforms all waves from array.
    (Real values only)
    :param framearray: array of waves (frames)
    :return: array of FFT waves (spectrums)
    """

    fourier_frame = []

    for frame in framearray:
        index = frame.make_spectrum()
        fourier_frame.append(index)

    return fourier_frame


def inverse_fourier(fourierarray):
    """ Apply logarithm to magnitude spectrum
    and IFFT to get output of homomorphic operation
    :param fourierarray: array of spectrums (frames)
    :return: array of IFFT spectrums (waves)
    """

    framearray = []

    for frame in fourierarray:
        framearray.append([])
        for samplenumber in range(len(frame.hs)):
            if frame.hs[samplenumber] != 0:
                frame.hs[samplenumber] = 20 * log10(abs(frame.hs[samplenumber]))


    for framenumber in range(len(framearray)):
        framearray[framenumber] = fourierarray[framenumber].make_wave()

    
    for frame in framearray:
        frame.ys[0] = 0

    return framearray



def sampling(framearray):
    """ High Sample Cepstum depending on Sex
    (Male default)
    :param framearray: array of frames (waves)
    :return framesample: array of sampled cepstums (waves)
    """

    index = 40  # or 20 for female

    pitchamp = []
    pitchperiod = []
   
    for frame in framearray:
        framesplit = frame.ys[index:int(samples_per_frame / 2)].tolist()
        value = max(framesplit)
        maxindex = framesplit.index(value) + index
        pitchamp.append(value)
        pitchperiod.append(maxindex)

    return pitchamp, pitchperiod



def meanenergy(energyarray):
    """ Mean Energy audio feature:
    Low predictability rate (61%)
    :param energyarray: array of energies per frame (waves)
    :return meanaudio: average energy throughout utterance
    """

    meanaudio = 0

    for energies in energyarray:
        meanaudio += energies

    if len(energyarray) > 0:
        meanaudio /= len(energyarray)
        return meanaudio[0]

    return meanaudio


def maxpitchamp(amparray):
    """ Max Pitch Amplitude audio feature:
    High Predictability rate (86%)
    :param amparray: array of pitch period amplitudes (floats)
    :return maxamp: Max pitch period amplitude
    """

    maxamp = 0
    if len(amparray) > 0:
        maxamp = max(amparray)

    return maxamp


def vowelduration(amparray, maxamp):
    """ Vowel Duration audio feature:
    High Predictability rate (82%)
    :param amparray: array of maximum amplitudes (float)
    :param maxamp: maximum pitch amplitude
    :return voweldur: vowel duration in msec (float)
    """

    voweldur = 0
    threshold = 0.7 * maxamp

    for amp in amparray:
        v = 0
        if amp >= threshold:
            v = 1

        voweldur += (v/2)

    voweldur *= 0.23
    return voweldur


def fundamentalf(periodarray, framelength):
    """Calculates pitch deviation to detect stress
       if pitch deviation >= 5, classified as stressed
       :param periodarray: array of pitch periods (index)
       :param framelength: length of frames in seconds
       :return average: average Fundamental Frequency for utterance
    """
    fundarray = []

    for period in periodarray:
        temp = period / (samples_per_frame/2) * framelength
        F0 = 1/temp
        fundarray.append(F0)

    average = 0
    if len(fundarray) > 0:
        average = sum(fundarray)/len(fundarray)

    return average
