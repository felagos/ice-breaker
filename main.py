from langchain.chains.llm import LLMChain
from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

if __name__ == "__main__":
    summary_template = """
    Given the information {information} about a person I want to create:
    1. A short summary
    2. Two interesting facts about them
    """
    
    information = """
    Name: John Doe
    Age: 35
    Occupation: Software Engineer
    """

    summary_prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )

    chain = LLMChain(llm = llm, prompt = summary_prompt)
    res = chain.invoke(input = {"information": information})