# SF Crimes

Spring 2015 NuPIC Hackathon

> **This hack is a shameless rip-off of [Austin Marshall's](http://github.com/oxtopus) [Shake Hack](https://github.com/oxtopus/shakehack) from the 2014 Fall NuPIC Hackathon.**

- Colors map to anomaly score
  - Red: High anomaly score
  - Green: Low anomaly score
- San Francisco crime data from 2003 until today
- Used coordinate encoder

## Requirements

- [NuPIC](https://github.com/numenta/nupic)
- [Redis](http://redis.io/) running locally
- Python, and [dependencies](requirements.txt)
- [Google Maps Javascript API Key](https://developers.google.com/maps/documentation/javascript/tutorial#api_key)

## Required Data

You also need to download [one huge JSON file](https://data.sfgov.org/api/views/tmnf-yvry/rows.json?accessType=DOWNLOAD) of crime data and run `python process_crimes.py` on it. This will produce a CSV file called `crimes.csv` in the current directory, which is expected for this program to work.

## Usage

- Start redis

  ```bash
  $ redis-server
  ```

- Start `run.py`

  ```bash
  $ python run.py
  ```

- Start webapp

  ```bash
  $ cd webapp
  $ python serve.py
  ```

- Open [http://localhost:8080](http://localhost:8080) in browser
