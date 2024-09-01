import os
from pydantic_settings import BaseSettings


class CandidateConfig(BaseSettings):
    MODEL_NAME: str = "gpt-3.5-turbo-16k"


candidate_config = CandidateConfig()