# Developing Dash Applications

This repo will introduce the development of dash applications to visualise sensor data.

It assumes that one has successfully completed [this repo](https://github.com/ciiram/indaba-maker-session-2019) which describes the development of software to collect data from sensors connected to the [NUCLEO F446RE](https://os.mbed.com/platforms/ST-Nucleo-F446RE/) board.

With the python script described in the *Writing Data to a Database* section running and writing to a database, we will access this database and display current sensor values in an app.

To work on this repo, create a virtual environment and activate it.

1. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
`python3 -m venv dash-viz`
1. Activate it
On Linux
`source dash-viz/bin/activate`
On Windows
`dash-viz\Scripts\activate.bat`
1. Install the requirements
`pip install -r requirements.txt`

## Dash Tutorial
Follow the official tutorial [here](https://dash.plot.ly/)
1. Follow the installation instructions [here](https://dash.plot.ly/installation)
1. Run the example applications

## Displaying Current Temperature
Here we will build a basic app that queries the database for the most recent measurement and displays the temperature value.

To get the most recent measurement we call

`SELECT last(Temperature) FROM "Indaba Session"`

This is incorporated in the file `temp-app.py`. Run this program and not the temperature displayed.

## Next step
1. Explore ploting the daily average temperature
1. Explore selecting the parameter to be displayed. Temperature, humidity and soil moisture
1. Build a webpage that looks visually appealing according to your taste
