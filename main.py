import pandas as pd
import matplotlib
import urllib.request
import os
import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
years = ["2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"]
stations = ["Augspurger", "BiddleButte", "ButlerGradeLvl1", "ButlerGradeLvl2", "ButlerGradeLvl3", "ForestGrove",
            "GoodnoeHillsLvl1", "GoodnoeHillsLvl2", "HoodRiver", "HorseHeaven", "KennewickLvl1", "KennewickLvl2",
            "MarysPeak", "Megler", "MtHebo", "NaselleRidge", "Roosevelt", "SevenMileHillLvl1", "SevenMileHillLvl2",
            "Shaniko", "Sunnyside", "Tillamook", "Troutdale", "Wasco"]

stations_data = {}
year_list = []


def create_folders():
    try:
        os.mkdir("Meterological_Data")
    except FileNotFoundError:
        pass
    try:
        os.mkdir("Output")
    except FileNotFoundError:
        pass



def file_download():
    for station in stations:
        for year in years:
            for i in range(1, 13):
                month = str(i).rjust(2, '0')
                url = f"https://transmission.bpa.gov/Business/Operations/Wind/MetData/Monthly/{station}/{station}_{year}_{month}.csv"
                # print(url)
                # urllib.request.urlretrieve(url, f"Meteorological_Data/{station}_{year}_{month}.csv")
                try:
                    urllib.request.urlretrieve(url, f"Meteorological_Data/{station}/{station}_{year}_{month}.csv")
                    print(f"Download Complete: {station} {year} {month}")
                except FileNotFoundError:
                    os.mkdir(f"Meteorological_Data/{station}")
                except urllib.error.HTTPError:
                    print(f"Download Failed: {station} {year} {month}")


def data_retrieval(station, year, month, url):
    try:
        df = pd.read_csv(url, header=6)
        # stations_data[station] = {year: year_list.append(df)}
        stations_data[station].update({year: year_list.append(df)})
        print(f"Data Retrieved: {station} {year} {month}")
    except urllib.error.HTTPError:
        print(f"Data Retrieval Failed: {station} {year} {month}")


def generate_all_dataframes():
    stations_data.clear()
    for station in stations:
        stations_data[station] = {}
        for year in years:
            year_list.clear()
            for i in range(1, 13):
                month = str(i).rjust(2, '0')
                url = f"https://transmission.bpa.gov/Business/Operations/Wind/MetData/Monthly/{station}/{station}_{year}_{month}.csv"
                data_retrieval(station, year, month, url)


def generate_selected_dataframes():
    station_list = input("Enter the desired stations seperated by a space. If all stations desired, enter 'all' ").split()
    if station_list[0] == "all":
        station_list = stations
    year_list = input("Enter the desired years seperated by a space. If all years desired, enter 'all' ").split()
    if year_list[0] == "all":
        year_list = years
    month_list = input("Enter the desired months seperated by a space. If all years desired, enter 'all' ").split()
    if year_list[0] == "all":
        month_list = months
    stations_data.clear()
    for station in station_list:
        for year in year_list:
            year_list.clear()
            for month in month_list:
                month = months.index(month.capitalize()) + 1
                month = str(month).rjust(2, '0')
                url = f"https://transmission.bpa.gov/Business/Operations/Wind/MetData/Monthly/{station}/{station}_{year}_{month}.csv"
                data_retrieval(station, year, month, url)
    print(stations_data)


def data_accuracy(station, year, month):
    month = months.index(month) + 1
    month = str(month).rjust(2, '0')
    url = f"https://transmission.bpa.gov/Business/Operations/Wind/MetData/Monthly/{station}/{station}_{year}_{month}.csv"
    try:
        df = pd.read_csv(url, header=6)
        print(f"Data Retrieved: {station} {year} {month}")
    except urllib.error.HTTPError:
        print(f"Data Retrieval Failed: {station} {year} {month}")
    # print(len(df.index))
    columns = list(df)
    for i in columns:
        print(df[i][2])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # pd.set_option("display.max_rows", None, "display.max_columns", None)
    # df = pd.read_csv("Meteorological_Data/Augspurger_2018_01.csv", header=6)
    # df.plot.line(x="Date/Time (UTC)", y="Temperature (F)", subplots=True)
    # matplotlib.pyplot.show()
    # df.to_csv("out.csv")
    # generate_all_dataframes()
    # generate_selected_dataframes()
    # file_download()
    create_folders()
    data_accuracy("Augspurger", "2017", "April")
