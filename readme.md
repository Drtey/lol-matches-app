# lol-matches-app

This project aims to take care of ingesting data from Leagues of Legends´s matches thanks to [Riot Games´s API](https://developer.riotgames.com/apis) and display those statistics in graphs, making prediction, advanced analytics, etc...

REST API developed with [Python](https://www.python.org/) && [FastAPI](https://fastapi.tiangolo.com)

### Run project
```
$ uvicorn <directory>.<filename>:<namevariable> --reload
$ uvicorn app.main:app --reload
```

### Create virtual environment
```
$ python3 -m venv <name_of_environment>
$ source <name_of_environment>/bin/activate
```

### Install dependencies
```
$ pip install -r requirements.txt
```

### API DOCS
http://127.0.0.1:8000//docs & http://127.0.0.1:8000//redoc 