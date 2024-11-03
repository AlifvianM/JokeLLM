from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from llm.chains.custom_chains import get_jokes_chain
from llm.third_parties.github import GithubAPI

load_dotenv()

def joke(
        user: str = "AlifvianM"
    ):
    github_data = GithubAPI(user=user).get_user()

    jokes_chain = get_jokes_chain()
    jokes = jokes_chain.invoke(
        input={
            "information":github_data
        }
    )
    return jokes

    
if __name__ == "__main__":
    a = joke()
    print(a.content)