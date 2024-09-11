import json
import os
import time

import jsbeautifier
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader
from langchain_openai import ChatOpenAI
from src.analysing.config import analysing_config
from src.analysing.prompt_strength import fn_strength_analysis, system_prompt_strength
from src.analysing.prompt_weakness import fn_weakness_detection, system_prompt_weakness

def output2json(output):
    """GPT Output Object >>> json"""
    opts = jsbeautifier.default_options()
    return json.loads(jsbeautifier.beautify(output["function_call"]["arguments"], opts))

def load_pdf(file_url):
    loader = PyPDFLoader(file_url)
    content = ""
    documents = loader.load_and_split()
    for page in documents:
        content += page.page_content

    return content


def analysing_strength(cv_content):
    llm = ChatOpenAI(model=analysing_config.MODEL_NAME, temperature=0.5, openai_api_key=os.getenv(key="OPENAI_API_KEY2"))
    completion = llm.predict_messages(
        [
            SystemMessage(content=system_prompt_strength),
            HumanMessage(content=cv_content),
        ],
        functions=fn_strength_analysis,
    )
    
    output_analysis = completion.additional_kwargs
    json_output = output2json(output=output_analysis)
    
    return json_output

def analysing_weakness(cv_content):
    llm = ChatOpenAI(model=analysing_config.MODEL_NAME, temperature=0.5, openai_api_key=os.getenv(key="OPENAI_API_KEY2"))
    completion = llm.predict_messages(
        [
            SystemMessage(content=system_prompt_weakness),
            HumanMessage(content=cv_content),
        ],
        functions=fn_weakness_detection,
    )
    
    output_analysis = completion.additional_kwargs
    json_output = output2json(output=output_analysis)
    
    return json_output