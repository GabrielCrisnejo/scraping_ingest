# Web Scraping and Data Ingestion

This document provides a comprehensive overview of the architecture and functionality of the web scraping project. It outlines the process of collecting news articles from an online source, processing the data, storing it in BigQuery for structured querying, and deploying the entire pipeline to Google Cloud Run. The document covers each phase of the project, from data extraction using Selenium to the final deployment steps on Google Cloud, ensuring a seamless integration for continuous operation in a cloud environment.

This project automates the process of scraping news articles from Yogonet International, processing the scraped data, and uploading it to Google BigQuery. The pipeline is containerized using Docker and deployed on Google Cloud Run for easy scalability and management.

## General considerations

Ensure your Google Cloud account has the necessary permissions to access Cloud Run, BigQuery and Artifact Registry. Create a project on Google Cloud Platform and a Docker repository in Google Artifact Registry called,

```
my-docker-repo
```

## Project Structure

The project is organized into the following structure, where each file and directory serves a specific purpose in the web scraping, data processing, and deployment pipeline:

```
.
├── deploy.sh                # Deployment script for Google Cloud Run
├── Dockerfile               # Dockerfile for containerizing the application
├── main.py                  # Entry point for running the application
├── README.md                # Project documentation and setup instructions
├── requirements.txt         # Python dependencies for the project
├── .env                     # Environment variables setting
├── docs                     # Documentation
|   ├── user_manual.pdf          # User manual
├── src                      # Source code directory
|   ├── bigquery.py          # Module for uploading data to BigQuery
|   ├── post_processing.py   # Module for post-processing scraped data
|   ├── scraping.py          # Module for scraping data from the target website
|   ├── settings.py          # Configuration settings for the project
├── webscrapingproject-451423-bfb0a6dca447.json  
                             # Google Cloud service account credentials
```

## Installation and Setup

To run the project locally, follow these steps:

```
# Clone the repository
$ git clone https://github.com/GabrielCrisnejo/scraping_ingest.git
$ cd scraping_ingest

# Create a virtual environment and activate it (optional)
$ python -m venv venv
$ source venv/bin/activate

# Install the required dependencies
$ pip install -r requirements.txt

# Run the project locally
$ python main.py
```

## Deploying on Google Cloud Run
To deploy the project on Google Cloud Run, follow these steps:

```
# Make sure you have the deploy script executable
$ chmod +x deploy.sh

# Deploy the application to Cloud Run
$ ./deploy.sh
```

## Interacting with the Service
After the deployment is successful, the service will be accessible via the Cloud Run URL. You can interact with the service using the following steps:

### Check the service status:

To check if the service is up and running, send a GET request to the root endpoint (\texttt{/}):

```
$ curl https://<your-cloud-run-url>/
```
For example,
```
$ curl https://web-scraper-challenge-109720451514.us-central1.run.app
``` 
This will return the status of the service, confirming if it’s running or encountering any issues.

### Trigger the service:

To trigger the main functionality of the application, send a GET request to the \texttt{/run} endpoint:

```
$ curl https://<your-cloud-run-url>/run
```
For example, 
```
$ curl https://web-scraper-challenge-109720451514.us-central1.run.app/run
```
This will initiate the scraping and processing tasks, and the response will confirm the operation has started or provide an error message.

### Note

If you run the application locally, it will run on the localhost so we need to do the following to interact with the service,
```
$ curl https://http://127.0.0.1:8080/
$ curl https://http://127.0.0.1:8080/run
```

## Conclusion
This document provides a detailed guide on the project's functionality, installation, execution, and deployment on Google Cloud Run. By following these steps, you can easily deploy the application and interact with it via HTTP requests. Additionally, ensure that all necessary permissions and configurations are set up in Google Cloud to guarantee smooth deployment and operation.