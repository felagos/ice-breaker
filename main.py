import os
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from third_parties import linkedin
from agents import linkedin_lookup_agent

if __name__ == "__main__":
    load_dotenv()

    profile = linkedin.scrape_profile()

    linkedin_lookup_agent.lookup("some name")

    information = """
    Name: John Doe
    Age: 35
    Occupation: Software Engineer
    """
    
    summary_template = """
    Given the information {information} about a person I want to create:
    1. A short summary
    2. Two interesting facts about them
    """
    
    summary_prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOpenAI(
        organization=os.getenv('OPENAI_ORG'),
        temperature=0,
        model_name="gpt-3.5-turbo",
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt)
    res = chain.invoke(input={"information": information})

    print(res)

    """ summary_prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOpenAI(
        organization = os.getenv('OPENAI_ORG'),
        temperature = 0,
        model_name = "gpt-3.5-turbo",
    )

    chain = LLMChain(llm = llm, prompt = summary_prompt)
    res = chain.invoke(input = {"information": information})

    print(res) """
