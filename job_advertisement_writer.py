from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages(
    [
        ("user", """You are a job posting expert. Given the following details:

        - Company Domain: {company_domain}
        - Company Description: {company_description}
        - Hiring Needs: {hiring_needs}
        - Specific Benefits: {specific_benefits}

        Please create a professional and compelling job posting that highlights the company's strengths, attracts potential candidates, and clearly outlines the job responsibilities, requirements, and offered benefits.
        """),
    ],
)

chain = prompt | ChatOpenAI() | StrOutputParser()

chain.invoke({
    "company_domain": "careers.wbd.com",
    "company_description": "Warner Bros. Discovery is a premier global media and entertainment company, offering audiences the world’s most differentiated and complete portfolio of content, brands and franchises across television, film, sports, news, streaming and gaming.",
    "hiring_needs": "Production Assistant for a TV production set in Los Angeles, June 2025",
    "specific_benefits": "Weekly Pay, Employee Meals, Healthcare"
})
