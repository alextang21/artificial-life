import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/backLegSensorData.npy")
matplotlib.pyplot.plot(backLegSensorValues, label="back", linewidth=4)
frontLegSensorValues = numpy.load("data/frontLegSensorData.npy")
matplotlib.pyplot.plot(frontLegSensorValues, label = "front")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()