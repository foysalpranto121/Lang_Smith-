from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
os.environ['LANGCHAIN_PROJECT'] = 'sequential_chain LLM APP'



load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI( model_name='gpt-4o', temperature=0.5, max_tokens=500)
model2 = ChatOpenAI( model_name='gpt-4o', temperature=0.4, max_tokens=500)
model3= ChatOpenAI( model_name='gpt-4o', temperature=0.25, max_tokens=500)




parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model2 | parser| model3 | parser

config = {
    'topic': 'Unemployment in bangladesh and its impact on the economy',
    'tags': ['economy', 'unemployment', 'bangladesh'],
    'metadata': {'author': 'John Doe', 'date': '2023-10-01'}    ,
    'paragraph': 'The unemployment rate in Bangladesh has been a growing concern for the government and economists alike. This report will explore the causes and effects of unemployment on the country\'s economy.'
}

result = chain.invoke(config)

print(result)
