from langchain_groq import ChatGroq

llm = ChatGroq(
        temperature =0,
        groq_api_key = "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",
        model_name= "llama-3.3-70b-versatile")

response = llm.invoke("Capital of india")
print(response.content)
