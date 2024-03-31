import os
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from third_parties import linkedin
from agents import linkedin_lookup_agent

from output_parser import person_intel_parser

if __name__ == "__main__":
    load_dotenv()
    
    linkedin_lookup_agent.lookup("some name")

    profile = linkedin.scrape_profile()

    information = f"""
    Name: {profile['first_name']}
    Occupation: {profile['occupation']}
    """
    
    summary_template = """
    Given the information {information} about a person I want to create:
    1. A short summary
    2. Two interesting facts about them
    \n{format_instructions}
    """
    
    summary_prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": person_intel_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(
        organization=os.getenv('OPENAI_ORG'),
        temperature=0,
        model_name="gpt-3.5-turbo",
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt)
    res = chain.invoke(input={"information": information})

    print(res)