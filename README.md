# WCBR<sup>2</sup>
## Weekly Comic Book Roundup Roundup

This project scrapes information from comicbookroundup.com to figure out what the highest rated comic books of the week are.

### Contents

- wcbrr.ipynb: A Jupyter notebook with all the web scraping code needed and a simple visualization of the week's top 10 highest rated comic books

### Roadmap

- Apache Airflow DAG to run pipeline weekly to scrape comic data and load into one or more data destinations
- Apache Airflow docker-compose.yml file and instructions for running Dockerized Airflow instance