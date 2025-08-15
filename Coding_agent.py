from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv



load_dotenv()

def main():

  code_agent=Agent(
  name="Code Agent",
  description="This is the agent for searching codes ",
  tools=[DuckDuckGo()],
  model=Groq(id="llama-3.3-70b-versatile"),  #Use your required & funtional model here 

  #instructions are the basic prompt which will provide instructions to the agent that how should it act or interact with the user 
  instructions=["Alaways include the source , Don't give answer to any questions which is not related with coding or Computer . Strictly follow this instructions and if user ask to try to ask any other question , just give the user -> I am very Sorry 🥹 , It is not from my domain , Please ask me about some coding related stuffs 🤗"],
  show_tool_calls=False,
  markdown=True,
  debug_mode=False,
  )



  while True:
    question = input("\nEnter your question (or type 'exit' to quit: ):").strip()
    if question.lower() in ["exit" , "quit"]:
      print("Goodbye! See you soon !!🤗👋")
      break

    code_agent.print_response(question , stream= True)

if __name__ == "__main__":
  main()
