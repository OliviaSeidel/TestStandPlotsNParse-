class Plot:
   def plotManyDataSets(xList, yList, plotTitle, saveFig):
       import matplotlib.pyplot as plt
       import matplotlib
       import colorsys


       def scale_lightness(rgb, scale_l):
           # convert rgb to hls
           h, l, s = colorsys.rgb_to_hls(*rgb)
           # manipulate h, l, s values and return as rgb
           return colorsys.hls_to_rgb(h, min(1, l * scale_l), s = s)


       print(len(xList))
       print(len(yList))
       # voltage and current are negative
       color = matplotlib.colors.ColorConverter.to_rgb("navy")
       rgbs = [scale_lightness(color, scale) for scale in [0, .5, 1, 1.5, 1.75, 2, 2.5, 2.75, 3, 3.75]]


       # rgbs = ['b','g','r','c','m','y','dimgrey','salmon','sienna','tan']


       plt.figure()
       plt.title(plotTitle)
       # plt.suptitle("Effect of 2W-Lamp Flash Frequencies and Voltages on Current in Vacuum")


       for i in range(0, len(yList) - 1):
           print(len(yList[i]))


       plt.xlabel("Voltage Across Field Cage (V)")
       plt.ylabel("Current output on Board (nanoAmps)")


       for i in range(0, len(yList)):
           plt.plot(xList, yList[i], color=rgbs[i], label=(str((i + 1) * 10) + "Hz"))


       plt.legend(loc='best', title='Flash Lamp Freq', prop={'size': 8})


       if saveFig is True:
           plt.savefig('CurrentVsVoltage.png', format = 'png', dpi = 1200)


       plt.show()


   def plotHistogram(xList: list, yList, plotTitle, saveFig):
       import matplotlib.pyplot as plt
       import matplotlib


       print(len(xList))
       print(len(yList))
       # voltage and current are negative
       color = matplotlib.colors.ColorConverter.to_rgb("navy")


       plt.figure()
       plt.title(plotTitle)
       # plt.suptitle("Effect of 2W-Lamp Flash Frequencies and Voltages on Current in Vacuum")


       for i in range(0, len(yList) - 1):
           print(len(yList[i]))


       plt.xlabel("Current (nA)")
       #plt.ylabel("Current output on Board (nanoAmps)")


       final_list = yList[0];


       for i in range(0, len(yList)):
           for j in range(0, len(yList[i])):
               #plt.hist(xList, yList[i], color=rgbs[i], label=(str((i + 1) * 10) + "Hz"))
               final_list.append(yList[i][j])


       plt.hist(final_list)


       #plt.legend(loc='best', title='Flash Lamp Freq', prop={'size': 8})


       if saveFig is True:
           plt.savefig('CurrentVsVoltageHist.png', format='png', dpi=1200)


       plt.show()


#test data
volt = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
ten_hz = [0, .0001, 0, 0, 0, .0001, 0, .0001, 0, .0002, .0002, .0002, .0002, .0003, .0003, .0003, .0003, .0004, .0003,
         .0004, .0003]
twenty_hz = [0, 0, .0001, .0001, .0001, .0001, .0002, .0001, .0002, .0004, .0003, .0004, .0007, .0004, .0006, .0006,
            .0005, .0006, .0007, .0006, .0007]
thirty_hz = [0, 0, 0, .0001, .0001, 0, .0001, .0001, .0003, .0003, .0005, .0006, .0008, .0008, .0009, .0009, .0010,
            .0009, .0010, .0010, .0010]
fourty_hz = [0.0001, .0001, 0, .0001, 0, .0001, .0001, .0001, .0002, .0004, .0006, .0008, .0010, .0010, .0012, .0010,
            .0012, .0012, .0011, .0010, .0013]
fifty_hz = [0.0001, .0001, .0001, .0001, .0002, 0, .0001, .0003, .0005, .0008, .0010, .0013, .0012, .0013, .0014, .0014,
           .0013, .0012, .0013, .0012, .0014]
sixty_hz = [0, .0001, .0002, .0001, .0001, .0001, 0, .0001, .0004, .0006, .0010, .0013, .0013, .0014, .0013, .0013,
           .0014, .0017, .0015, .0014, .0015]
seventy_hz = [0, .0001, .0002, .0001, .0001, 0, .0001, .0006, .0010, .0013, .0015, .0015, .0014, .0016, .0016, .0017,
             .0017, .0015, .0015, .0016, .0017]
eighty_hz = [0.0001, 0, .0001, .0001, 0, .0002, .0004, .0007, .0010, .0013, .0015, .0016, .0015, .0017, .0016, .0016,
            .0017, .0016, .0019, .0016, .0017]
ninety_hz = [0, .0001, 0, .0001, .0001, .0001, .0003, .0009, .0012, .0014, .0016, .0019, .0017, .0017, .0018, .0019,
            .0019, .0018, .002, .0020, .0021]
oneHundred_hz = [.0001, .0002, .0001, .0001, 0, .0001, .0005, .0011, .0015, .0015, .0018, .0019, .0020, .0017, .0019,
                .0020, .0021, .0019, .0021, .0022, .0023]
total_list = [ten_hz, twenty_hz, thirty_hz, fourty_hz, fifty_hz, sixty_hz, seventy_hz, eighty_hz, ninety_hz,
             oneHundred_hz]
Plot.plotHistogram(volt, total_list, "Current vs Voltage", True)
Plot.plotHistogram(volt, total_list, "Current", True)

