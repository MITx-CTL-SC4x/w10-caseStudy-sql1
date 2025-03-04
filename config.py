########  GENERAL APP INFORMATION  ##############

APP_TITLE = None
# APP_TITLE = "SC4x | Week 10 | Case Study | SQL 1"

APP_INTRO = None
# APP_INTRO = """The app evaluates and provides feedback on a single SQL query using an AI API (OpenAI, Gemini, or Claude)."""

APP_HOW_IT_WORKS = None
# APP_HOW_IT_WORKS = """ """

SHARED_ASSET = {}
# SHARED_ASSET = {
#     "name":"NAME",
#     "path":"FILE.pdf",
#     "button_text":"Read this PDF first"
# }

HTML_BUTTON = {}

COMPLETION_MESSAGE = "Thank you for submitting a response!"
COMPLETION_CELEBRATION = False

SCORING_DEBUG_MODE = False

 ####### PHASES INFORMATION #########

PHASES = {
    "attempt1": {
        "type": "text_area",
        "height": 200,
        "label": """Question 1: Please enter your query in the text box below.""",
        "instructions": """ The correct answer to this question:
    SELECT count(DISTINCT customer_id)
    FROM Customers
    WHERE customer_city = 'sao paulo';
Provide compare the following student submission with the correct answer above. Please provide feedback on the student submission. Do not provide the correct answer. Instead, provide guidance to help the student identify where they might be missing something in their code. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
    "attempt2": {
        "type": "text_area",
        "height": 200,
        "label": """Do you want to try again?""",
        "instructions": """ The correct answer to this question:
    SELECT count(DISTINCT customer_id)
    FROM Customers
    WHERE customer_city = 'sao paulo';
Provide compare the following student submission with the correct answer above. Please provide feedback on the student submission. Do not provide the correct answer. Instead, provide guidance to help the student identify where they might be missing something in their code. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
}

######## AI CONFIGURATION #############

########## AI ASSISTANT CONFIGURATION #######
ASSISTANT_NAME = "sc4x_wk10_CaseStudy_SQL"
ASSISTANT_INSTRUCTIONS = """ You are an expert in SQL and overseeing a course where students are learning the basics of SQL. """

LLM_CONFIGURATION = {
    "gpt-4-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4-turbo",
        "temperature":0,
        "price_per_1k_prompt_tokens":.01,
        "price_per_1k_completion_tokens": .03
    },
    "gpt-4o":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4o",
        "temperature":0,
        "price_per_1k_prompt_tokens":.0025,
        "price_per_1k_completion_tokens": .010
    },
    "gpt-3.5-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-3.5-turbo-0125",
        "temperature":0,
        "price_per_1k_prompt_tokens":0.0005,
        "price_per_1k_completion_tokens": 0.0015
    }
}

ASSISTANT_THREAD = ""
ASSISTANT_ID_FILE = "assistant_id.txt"