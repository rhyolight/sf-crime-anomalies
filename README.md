# Shake Hack

Fall 2014 NuPIC Hackathon

![Earthquakes in California](http://oxtopus.github.io/shakehack/map.jpg "Earthquakes in California")

[See the video!](https://drive.google.com/a/numenta.com/file/d/0B7hpsypiwZ_UNFRPNUFiaGZGejQ/view?usp=sharing)

## Requirements

- [NuPIC](https://github.com/numenta/nupic)
- [Redis](http://redis.io/) running locally
- Python, and [dependencies](requirements.txt)
- [Google Maps Javascript API Key](https://developers.google.com/maps/documentation/javascript/tutorial#api_key)

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
  $ API_KEY=<insert API key here> python serve.py
  ```

- Open [http://localhost:8080](http://localhost:8080) in browser
