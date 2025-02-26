# SC4x | Week 10 | Case Study | Testing v1

## Overview
The app is designed for initial development and testing that evaluates and provides feedback on a single SQL query.

## Prerequisites
- Python 3.6 or later
- pip
- virtualenv (optional but recommended)
- OpenAI, Claude, and/or Google Gemini API key(s)

## Local Setup Instructions

### 1. Clone the repository

Navigate to a location where you'd like to run this app from, and clone the repo:

```bash
git clone https://github.com/MITx-CTL-SC4x/w10-caseStudy-q1.git
```

### 2. Create a Virtual Environment

To create a virtual environment, navigate to your project directory in the terminal:
```bash
cd w10-caseStudy-q1
```

It's recommended to isolate the project's dependencies using a virtual environment. You can utilize tools like venv or virtualenv to achieve this. Refer to official documentation for specific commands based on your chosen tool. Here is the command from a mac shell:
```bash
python3 -m venv venv
```

Finally, activate your virtual environment:
```bash
source venv/bin/activate
```

### 3. Install Requirements
Activate your virtual environment and install the required packages using pip:
```bash
pip3 install -r requirements.txt
```

## Running the App

### Running Locally

API key(s): Set your API keys in .env

Navigate to your project directory in the terminal and execute the following command to launch the Streamlit app:
```bash
streamlit run main.py
```

This will open the App in your web browser, typically at http://localhost:8501.

### Running on Streamlit

*TODO: Set up API key credentials as described at https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management*

1. Sign into share.streamlit.io
2. Click 'Deploy an app' and then paste in your GitHub URL
3. TBD: API key management (see above)

## Credit
This app is based on the 'AI MicroApp (Assistant)' by John Swope found at https://github.com/jswope00/AI-Microapp-Template-Assistant/tree/main
