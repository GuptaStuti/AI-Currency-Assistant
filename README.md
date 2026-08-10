# 💱 AI Currency Assistant

An AI-powered currency assistant built using **LangChain, LangGraph, Hugging Face, and Streamlit**.
The application uses an LLM with tool-calling capabilities to understand currency-related requests, select the appropriate tool, retrieve exchange-rate information, perform currency conversions, and maintain conversational context across multiple interactions.
This project is **Version 1 – Learning Version**, created to gain hands-on experience in building an AI application using LangChain, LangGraph, tool calling, and agentic workflows.

---

## 🚀 Features

- 💱 Currency conversion
- 📈 Exchange-rate lookup
- 🌍 Currency information lookup
- 🤖 LLM-powered tool calling
- 🔄 LangGraph-based agent workflow
- 🧠 Conversational memory
- 🧵 Thread-based conversation management
- 💬 Multi-turn conversations
- 🖥️ Streamlit chat interface
- 🗑️ Clear conversation functionality
- ⚡ Exchange-rate caching
- 📝 Application logging
- 🔐 Environment-based API configuration

---

## 🏗️ Architecture

The application follows a modular architecture separating the UI, agent workflow, tools, configuration, and utilities.


                         User
                           │
                           ▼
                    Streamlit UI
                           │
                           ▼
                    LangGraph Agent
                           │
                           ▼
                          LLM
                           │
                    ┌──────┴──────┐
                    │             │
              Tool Required   Direct Response
                    │
                    ▼
                 ToolNode
                    │
          ┌─────────┼─────────┐
          │         │         │
          ▼         ▼         ▼
     Exchange    Currency   Currency
       Rate      Converter    Info
       Tool        Tool        Tool
          │         │         │
          └─────────┼─────────┘
                    │
                    ▼
             External API
                    │
                    ▼
              Tool Response
                    │
                    ▼
                    LLM
                    │
                    ▼
              Final Response
                    │
                    ▼
                   User


##🧠 **LangGraph Workflow**

LangGraph is used to orchestrate the interaction between the LLM and the available tools.

```text
User Input
    │
    ▼
Agent / LLM
    │
    ├── No tool required ──► Final Response
    │
    └── Tool required
             │
             ▼
          ToolNode
             │
             ▼
        Execute Tool
             │
             ▼
       Return Tool Result
             │
             ▼
          Agent / LLM
             │
             ▼
       Final Response


## 🛠️ Tech Stack
-- **Python**	            Application development\br
-- **LangChain**	        LLM and tool integration
-- **LangGraph**	        Agent workflow orchestration
--**Hugging Face**	      LLM provider
-- **Streamlit**	        User interface
-- **Exchange Rate API**	Exchange-rate data
-- **Requests**	          API communication
-- **python-dotenv**	    Environment variable management


⚙️ Setup
1. Clone the repository
git clone https://github.com/<your-username>/ai-currency-assistant.git

Navigate to the project:

cd ai-currency-assistant
