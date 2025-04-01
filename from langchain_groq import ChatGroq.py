from langchain_groq import ChatGroq

llm = ChatGroq(
        temperature =0,
        groq_api_key = <your api key here>,
        model_name= "llama-3.3-70b-versatile")

response = llm.invoke("Capital of india")
print(response.content)
