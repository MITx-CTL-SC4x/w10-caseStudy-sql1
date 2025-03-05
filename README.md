# SC4x | Week 10 | Case Study | SQL 1

## Overview
The app uses an AI API (OpenAI, Gemini, or Claude) to evaluate and provide feedback on a SQL query to calculate the number of customers in the dataset from the city of 'sao paulo'.

## Prerequisites
- Python 3.6 or later
- pip
- virtualenv (optional but recommended)
- OpenAI, Claude, and/or Google Gemini API key(s)

## Local Setup Instructions

Navigate to a location where you'd like to run this app from, and clone the repo:

```bash
git clone https://github.com/MITx-CTL-SC4x/w10-caseStudy-sql1.git
```

Navigate to your project directory in the terminal:
```bash
cd w10-caseStudy-sql1
```

## Running the App Locally

### 1. Create a Virtual Environment

It's recommended to isolate the project's dependencies using a virtual environment. You can utilize tools like venv or virtualenv to achieve this. Refer to official documentation for specific commands based on your chosen tool. Here is the command from a mac shell:
```bash
python3 -m venv venv
```

Finally, activate your virtual environment:
```bash
source venv/bin/activate
```

### 2. Install Requirements
Activate your virtual environment and install the required packages using pip:
```bash
pip3 install -r requirements.txt
```

### 3. Running the App

API key(s): Set your API keys in .env ... see .env_sample

Navigate to your project directory in the terminal and execute the following command to launch the Streamlit app:
```bash
streamlit run main.py
```

This will open the App in your web browser, typically at http://localhost:8501.

## Deploying on Streamlit for the First Time

1. Sign into share.streamlit.io
2. Click 'Deploy an app' and then paste in your GitHub URL
3. Put API keys in Advanced Settings (see instructions below)

Instructions for API key management are at https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management

### Updating the Streamlit App

After changes are committed to the repository, reboot the app from the Streamlit dashboard at https://share.streamlit.io/

## Credit
This app is based on the 'AI MicroApp (Assistant)' by John Swope found at https://github.com/jswope00/AI-Microapp-Template-Assistant/tree/main
