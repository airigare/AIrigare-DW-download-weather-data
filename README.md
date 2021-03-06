# download-weather-data

App to download the actual weather data from MeteoSuisse (https://www.meteoschweiz.admin.ch/home.html?tab=overview)

## Run locally

1. Install [Python](http://docs.python-guide.org/en/latest/starting/installation/)
1. Install Setuptools and pip (see guide above)
1. Install Virtualenv (acconplish this by running `pip install virtualenv`)
1. Run `virtualenv venv`
1. Run `source venv/bin/activate` on Mac OS X/Linux or`venv\Scripts\activate.bat` on windows
1. Run `pip install -r requirements.txt`
1. Run `python app.py`
1. Visit [http://localhost:3000](http://localhost:3000)

## Run in the cloud

1. Install the [cf CLI](https://github.com/cloudfoundry/cli#downloads)
1. Run `cf push download-weather-data -m 128M -n download-weather-data -u none`
1. Visit the given URL
