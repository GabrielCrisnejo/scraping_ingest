from flask import Flask, jsonify
import threading
import time
from src.scraping import scrape_data
from src.post_processing import process_data
from src.bigquery import upload_to_bigquery

app = Flask(__name__)

@app.route("/")
def health_check():
    return "Container is running!", 200

@app.route("/run", methods=["GET"])
def run_pipeline():
    try:

        print("Starting web scraping...")
        scrape_data()
        print("Scraping completed. Processing data...")
        process_data()
        print("Processing completed. Uploading data to BigQuery...")
        upload_to_bigquery()
        print("Uploading data to BigQuery completed.")

        return jsonify({"message": "Data pipeline completed successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False), daemon=True).start()

    while True:
        time.sleep(3600)
