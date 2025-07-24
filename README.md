# 🚀 Airflow ETL Pipelines with Astronomer

Welcome to my Apache Airflow project! This repo was created using the Astronomer CLI and is designed for building, testing, and running real-world data pipelines using the modern TaskFlow API and Dockerized Airflow setup.

---

## 🧠 What’s Inside

This project is built using [Astronomer's Runtime](https://www.astronomer.io/docs/astro/runtime), a production-grade distribution of Apache Airflow.

### 📁 Key Folders

- **`dags/`**  
  All DAGs (Directed Acyclic Graphs) live here. Each DAG is a Python file defining a data pipeline.

- **`example_astronauts.py`**  
  A sample DAG that fetches astronauts currently in space and prints a dynamic message for each. (For learning TaskFlow API + dynamic mapping)

- **`requirements.txt`**  
  Add your Python packages here (e.g., `pandas`, `requests`, `apache-airflow`).

- **`Dockerfile`**  
  Defines the image for the local Airflow environment.

- **`airflow_settings.yaml`**  
  Use this to pre-load Variables, Connections, and Pools into your local Airflow.

---

## ▶️ Getting Started Locally

Make sure you have Docker and the [Astronomer CLI](https://docs.astronomer.io/astro/cli/install-cli) installed.

Then run:

```bash
astro dev start
