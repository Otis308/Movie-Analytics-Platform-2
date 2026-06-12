# CineAnalytics Platform

## Milestone 1 - Raw Data Ingestion

### Features

* Extract movie data from TMDB API
* Pagination support
* Raw JSON backup layer
* PostgreSQL loading using DLT
* Incremental merge strategy
* Environment variable management

### Architecture

TMDB API
→ Raw JSON Layer
→ DLT Pipeline
→ PostgreSQL

### Status

* [x] Project setup
* [x] Database schema design
* [x] Raw ingestion pipeline
* [ ] Monitoring
* [ ] Data quality checks
* [ ] Airflow orchestration
* [ ] dbt transformations
* [ ] Kafka streaming
* [ ] Spark processing
