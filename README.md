# COLING-Datasets

This repository provides test datasets from various resources to benchmark LLM agents across multiple domains. One of the key datasets used in this benchmark is **MMAU**.
## MMAU Dataset Access and Benchmarking
The MMAU dataset is used to evaluate LLM agent capabilities across multiple domains, including tool use, math, and coding challenges.

Quick Start
1. Clone the Repository
bash
Copy code
git clone https://github.com/apple/axlearn.git
cd axlearn
2. Install Dependencies
bash
Copy code
pip install ".[mmau]"
3. Dataset Preparation
Download from Google Cloud (Coming Soon):

bash
Copy code
mkdir -p ./data/
gsutil -m cp -r "gs://axlearn-public/datasets/mmau/20240712/*" ./data/
Download from Hugging Face (Coming Soon):

bash
Copy code
huggingface-cli download apple/mmau --local-dir ./data --repo-type dataset
