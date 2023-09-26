def data_plot(file_name: str, show: bool = False) -> None:
    """
    Plots the S parameters data from a CSV file.

    Args:
        file_name (str): The name of the CSV file.
        min_freq (float, optional): The minimum frequency to include in the plot. Defaults to None.
        max_freq (float, optional): The maximum frequency to include in the plot. Defaults to None.
        show (bool, optional): Whether to display the plot or save it to a file. Defaults to False.
    """
    # Read the CSV file
    data = pd.read_csv(file_name)

    if min_freq is not None:
        # Filter the data by minimum frequency
        data = data[data['freq (GHz)'] >= min_freq]
    if max_freq is not None:
        # Filter the data by maximum frequency
        data = data[data['freq (GHz)'] <= max_freq]

    # Extract the frequency
    freq = data['freq (GHz)']

    # Create the plot
    plt.rcParams['text.usetex'] = True
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.set_xlabel("Frequency (GHz)", family="serif", fontsize=12)
    ax1.set_ylabel("S-parameter (dB)", family="serif", fontsize=12)

    plt.plot(freq, data['S21dB (1)'], color='seagreen', label=r'$S_{21}$')

    if 'full_sweep' in file_name:
        ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
    
    # Set the minor tick marks
    ax1.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax1.tick_params(axis='both', which='major', direction="out", top="on", right="on", bottom="on", length=8, labelsize=8)
    ax1.tick_params(axis='both', which='minor', direction="out", top="on", right="on", bottom="on", length=5, labelsize=8)

    # Adjust the plot layout
    fig.tight_layout()
    plt.legend()
    plt.grid(True)

    if show:
        # Display the plot
        plt.show()
    else:        
        # Save the plot to a file
        if 'Experimental' in file_name:
            plt.savefig(file_name.replace('.csv', '.png').replace('S parameters', 'Plots/S parameters'), dpi=1000, format="png")
        elif 'S parameters' in file_name:
            plt.savefig(file_name.replace('.csv', '.png').replace('S parameters', 'Plots'), dpi=1000, format="png")
        elif 'S-parameters' in file_name:
            plt.savefig(file_name.replace('.csv', '.png').replace('S-parameters', 'Plots'), dpi=1000, format="png")
        plt.close()