class Plot:
    def plotManyDataSets(xList, yList, plotTitle, saveFig):
        import matplotlib.pyplot as plt
        import matplotlib
        import colorsys

        def scale_lightness(rgb, scale_l):
            # convert rgb to hls
            h, l, s = colorsys.rgb_to_hls(*rgb)
            # manipulate h, l, s values and return as rgb
            return colorsys.hls_to_rgb(h, min(1, l * scale_l), s=s)

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
            plt.savefig('CurrentVsVoltage.png', format='png', dpi=1200)

        plt.show()

    def plotDots(self, totTime, currentCh, plotTitle, xLabel, yLabel):
        import matplotlib.pyplot as plt
        import matplotlib
        import colorsys

        plt.figure()
        for i in range(0, 15):
            plt.plot(totTime[i], currentCh[i], 'o')

        if plotTitle is "":
            plt.title("Reconstructed current from time between resets")

        if xLabel is "":
            plt.xlabel("Time(seconds)")

        if yLabel is "":
            plt.ylabel("Reconstructed Current(Amps)")

        plt.savefig("AllChannels.png")
        plt.show()

    def plotManyHistograms(self, xLabel, yLabel):
        import matplotlib as plt

        fig, ax = plt.subplots(4, 4)
        for i, ch in enumerate(chTDRs):
            filt = [c for c in ch if c > 304*33e-9]
            row = int(i/4)
            col = int(i%4)
            print(f"ch{i+1} have n pass: {len(filt)}")
            ax[row, col].hist(filt)
            ax[row, col].set_title('Ch:' + str(i+1), font='6')
            if xLabel is "":
                if yLabel is "":
                    ax[row, col].set('Seconds','# of Events')
                else:
                    ax[row, col].set(xlabel = 'Seconds', ylabel = yLabel)
            else:
                if yLabel is "":
                    ax[row, col].set(xlabel = xLabel, yLabel = '# of Events')
                else:
                    ax[row, col].set(xlabel = xLabel, ylabel = yLabel)

        fig.tight_layout()
        fig.savefig('binnedDeltaTsPerChannel')
