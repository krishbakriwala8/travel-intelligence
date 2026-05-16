# ✈️ Multi-Agent Travel Intelligence System

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-Multi--Agent-orange.svg)](https://google.github.io/adk-docs/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3%2070B-green.svg)](https://console.groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A multi-agent AI system that answers complex travel queries by coordinating specialized agents using **Google ADK** and **Groq LLaMA 3.3 70B**. Built as part of a Mercedes-Benz GenAI Internship assignment.

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────────────┐
│     ORCHESTRATOR        │  ← coordinates all agents
│   (LLaMA 3.3 70B)       │
└─────────────────────────┘
       │         │         │
       ▼         ▼         ▼
┌──────────┐ ┌────────┐ ┌───────────┐
│ Weather  │ │ Budget │ │ Transport │
│  Agent   │ │ Agent  │ │   Agent   │
└──────────┘ └────────┘ └───────────┘
       │         │         │
   wttr.in   Groq LLM  Local DB
             exchange    + LLM
              rate API  knowledge
       │         │         │
       └────────┬──────────┘
                ▼
        Final Travel Report
```

---

## 🤖 Agents

| Agent | Role | Tools |
|---|---|---|
| **Orchestrator** | Reads user query, delegates to right agents, combines results | sub_agents |
| **Weather Agent** | Gets real-time weather for any city | `get_weather` → wttr.in API |
| **Budget Agent** | Estimates minimum trip cost from Germany + currency conversion | `get_flight_estimate`, `get_exchange_rate` |
| **Transport Agent** | Explains local transport at destination city | `get_local_transport` |

---

## ✨ Features

- **Real-time weather** — live data from wttr.in for any city in the world
- **Intelligent budget estimation** — LLM-powered flight price estimates + real exchange rates
- **Global transport coverage** — verified data for major cities, LLM knowledge for others
- **Natural language queries** — ask anything in plain English
- **Interactive UI** — Streamlit dashboard with example queries
- **100% free** — no paid APIs required

---

## 🛠️ Tech Stack

- **Google ADK** — multi-agent orchestration framework
- **Groq + LLaMA 3.3 70B** — free, fast LLM inference
- **LiteLLM** — adapter layer connecting ADK to Groq
- **wttr.in** — free real-time weather API (no key needed)
- **exchangerate-api.com** — free live currency conversion
- **Streamlit** — interactive web UI
- **Python 3.11+**

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/krishbakriwala8/travel-intelligence
cd travel-intelligence
```

### 2. Install dependencies
```bash
pip install google-adk google-genai litellm groq requests streamlit python-dotenv
```

### 3. Get your free Groq API key
Go to [console.groq.com](https://console.groq.com) → Sign up → API Keys → Create key

### 4. Set up environment variables
```bash
cp .env.example .env
```
Edit `.env` and add your key:
```
GROQ_API_KEY=your_groq_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

## 📁 Project Structure

```
travel-intelligence/
├── agents/
│   ├── __init__.py
│   ├── orchestrator.py      # root agent + sub_agents
│   ├── weather_agent.py     # weather specialist
│   ├── budget_agent.py      # budget specialist
│   └── transport_agent.py   # transport specialist
├── tools/
│   ├── __init__.py
│   ├── weather_tool.py      # wttr.in API call
│   ├── budget_tool.py       # LLM flight estimate + exchange rate
│   └── transport_tool.py    # local transport data
├── app.py                   # Streamlit UI
├── runner.py                # ADK Runner setup
├── .env                     # GROQ_API_KEY (never commit)
├── .env.example             # example environment file
├── requirements.txt
└── README.md
```

---

## 💬 Example Queries

```
"I'm traveling from Frankfurt to Tokyo for 5 days.
 What's the weather, budget and local transport?"

"What's the minimum budget to travel from Germany to Iceland for 10 days?"

"I want to travel from Germany to Morocco for 7 days.
 Give me weather, budget and local transport info."

"How do I get around in Delhi?"

"Calculate the budget for 7 days in Dubai and show me the cost in AED."
```

---

## 🎯 Design Decisions

**Why separate agents instead of one LLM?**
Each agent has one job and its own tools. This makes the system modular — improving the budget logic doesn't touch the weather or transport agents. It also improves accuracy because each agent is focused on one task.

**Why LiteLLM instead of Gemini directly?**
Google ADK is designed for Gemini by default. The Gemini free tier returned a quota error in Germany (429 — limit 0). LiteLLM acts as a universal adapter, connecting ADK to Groq's LLaMA 3.3 70B which is completely free. Switching back to Gemini is a one-line change.

**Why run agents separately in runner.py?**
When using sub_agents, the orchestrator LLM sometimes calls only one agent and stops. Running each agent independently in runner.py guarantees all three always run and results are reliably combined.

**Why mock + LLM for flight prices instead of a real API?**
No truly free real-time flight API exists. I use LiteLLM to ask the LLM for realistic price estimates based on its training knowledge — works for any city worldwide, not just hardcoded destinations.

---

## 🔧 What I Would Improve

- **Real flight API** — swap Groq LLM estimates with Amadeus API (free tier available)
- **Accommodation tiers** — budget, mid-range, luxury options per city
- **Conversation memory** — persist session so users can ask follow-up questions
- **Parallel agent execution** — use Google ADK's `ParallelAgent` to run all agents simultaneously
- **More cities** — expand verified transport data beyond current cities

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Built by [Krish Bakriwala](https://github.com/krishbakriwala8) · M.Sc. AI · Brandenburg University of Technology**
