| <img width="200" alt="Coding_agent_logo" src="https://github.com/Prabrit/Coding-Agent/blob/main/Coding_agent.png"> | <h2>Coding Agent - A terminal-based AI assistant designed to help developers search, generate, and understand code quickly.</h3>
:---:|:---|

## Features 
- **Code-Only Focus** – Only answers programming and computer-related questions.
- **Source-Backed Results** – Every answer includes a source link for verification.
- **Web-Integrated** – Uses **DuckDuckGo** for real-time code search.
- **Strict Domain Control** – Rejects non-coding questions politely.

## Tech Stack
- **[Agno](https://github.com/agno-ai)** – AI agent orchestration.
- **[Groq](https://groq.com/)** – High-performance large language model inference.
- **[DuckDuckGo Search Tool](https://duckduckgo.com/)** – Retrieves real-time coding resources.
- **Python** – Core programming language.
- **dotenv** – For environment variable management.
  
---

##  Installation & Setup  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Prabrit/Coding-Agent.git
cd coding-agent
```
2️⃣ **Python environment Setup**
```bash
python3 -m .venv venv
```
3️⃣ **Install dependencies**
- All the dependencies are given in the requirements.txt file with it's version . Just run the     command bellow in your terminal to install them .
  
```bash
  pip install -r requirements.txt
```
4️⃣ **Set up environment variables**
- Replace the fields shown bellow in the .env file with your API keys:

```ini
  PHI_DATA_KEY="PROVIDE YOUR PHIDATA API KEY HERE"
  GROQ_API_KEY="PROVIDE YOUR GROQ API KEY HERE"
  AGNO_API_KEY="PROVIDE YOUR AGNO API KEY HERE"
  EXA_API_KEY="PROVIDE YOUR EXA API KEY HERE"
```
5️⃣ **Run the Coding Agent**

```bash
python3 Coding_agent.py
```
## Usage
Once running, you can ask any coding-related question:

```lua
Enter your question (or type 'exit' to quit):
```
If you ask a non-coding question:

```pgsql
I am very Sorry 🥹 , It is not from my domain , Please ask me about some coding related stuffs 🤗
```
## Example Screenshots
- Solving Leetcode 50 using agent

  <img src="https://github.com/Prabrit/Coding-Agent/blob/main/Example1.png" alt="Draw" width="1000" height="1000" />

- Now giving it a non coding question
  
  <img src="https://github.com/Prabrit/Coding-Agent/blob/main/Example2.png" alt="Draw" width="1000" height="1000" />

## 📜 License

This project is licensed under the MIT License – feel free to use and modify it.
  
  
  




   


