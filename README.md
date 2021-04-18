# Mutant detect API

Mutant detect API. Is an API to identify DNA mutations created to fit the Magneto's requirements. You can get stats from the historical sequences processed by the API

The API has the following features:
* HTTP is used between the browser or client. 
* Process DNA sequences.
* Get historical stats for the sequences processed.

## Resources

### Mutant

Service to detect Mutants


### Endpoints
<br />

| Name         | Method | Description                        |
|--------------|--------|------------------------------------|
| /api/v1/mutant | POST   | Process DNA sequences if valid is correspond to a mutant |

<br />

### Input Parameters
<br />

| Name                          | Data Type | Required / optional | Description                                                                     |
|-------------------------------|-----------|---------------------|---------------------------------------------------------------------------------|
| DNA | List of string    | Required            | Used to validate the sequences                                               |

<br />

### Example value

```json
{"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}
```

<br />

### Stats

Get historical stats based on the historical sequences validated.

<br />
### Endpoints
<br />

| Name         | Method | Description                        |
|--------------|--------|------------------------------------|
| /api/v1/stats | GET   | Stats with the ratio between humans and mutants |
<br />


### Output Parameters

<br />

| Name          | Data Type     | Required / optional | Description      |
|---------------|---------------|---------------------|------------------|
| count_mutant_dna   | Integer        | Required            | Count mutant DNA |
| count_human_dna   | Integer        | Required            | Count human DNA |
| ration   | Float        | Required            | Ratio |

<br />

### Example value

```json
{
  "count_mutant_dna": 0,
  "count_human_dna": 1,
  "ratio": 0
}
```

#Setup

## Run Locally

### Install libraries:
- ``` pip install requirements.txt ```

### Install a redis server

### Review the setting_dev.yaml and fill with your REDIS_HOST and REDIS_PORT.

### To run the API using flask:
- ``` python manage.py run ```
- ``` go to http://127.0.0.1:5000/ ```

### To run the API using gunicorn:
- ``` python manage.py gunicorn ```
- ``` go to http://0.0.0.0:8080/ ```


### To executes test with pytest:
- ``` python -m pytest -vv  ```

### To create a coverage report:
- ``` python -m pytest --cov=. --cov-report html:coverage ```
- ``` go to coverage folder and open the index.html to get a complete report```


#Live API

### This API was deployed using the Google Cloud Run

### Access to the Swagger documentation using the next url:
- ``` https://mutant-jrn2udeqnq-uc.a.run.app/  ```

### To access directly to the endpoints, use:
- ``` https://mutant-jrn2udeqnq-uc.a.run.app/api/v1/mutant  ```
- ``` https://mutant-jrn2udeqnq-uc.a.run.app//api/v1/stats  ```
