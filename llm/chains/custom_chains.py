from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

def get_jokes_chain() -> RunnableSequence:
    jokes_template = """
        Given information about someone from github {information}, I want you to make a joke from the information you get and intimidate them, like really intimidating (no nice words included). Do it in bahasa indonesia with Gen Z Jakarta accent and things. 
    """

    jokes_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=jokes_template
    )
    return jokes_prompt_template | llm