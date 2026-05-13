# FactShield 🛡️
### AI-Powered Misinformation Detection Agent

![Google ADK](https://img.shields.io/badge/Google%20ADK-1.28.0-blue)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-purple)
![Cloud Run](https://img.shields.io/badge/Cloud%20Run-Deployed-green)
![Python](https://img.shields.io/badge/Python-3.12-yellow)

---

## 🌍 The Problem

3.6 billion people encountered misinformation in 2024. Existing fact-checkers like Snopes and PolitiFact are manual, slow, and human-operated — taking hours to verify a single claim. Meanwhile, false information spreads in minutes.

## ✅ The Solution

FactShield is a single AI agent that takes any claim as input and returns an instant, structured, evidence-backed verdict — **TRUE, FALSE, MISLEADING, or UNVERIFIED** — in seconds.


---

## ⚙️ How It Works
User Input → extract_core_claim() → Gemini 2.5 Flash → calculate_credibility_score() → JSON Verdict

1. User sends a claim via **HTTP POST**
2. `extract_core_claim()` FunctionTool cleans and isolates the claim
3. **Gemini 2.5 Flash** analyzes evidence from WHO, CDC, Reuters, peer-reviewed journals
4. `calculate_credibility_score()` FunctionTool scores the claim 0-100
5. Structured verdict returned via **Google Cloud Run**

---

## 📦 Example

**Input:**
"5G towers cause cancer"

**Output:**
FactShield Verdict
Claim: 5G towers cause cancer
Verdict: ❌ FALSE
Confidence: 95%
Category: Health
Evidence:

WHO: No adverse health effects confirmed from 5G exposure
FCC: No scientific evidence linking 5G to cancer
UK Health Security Agency: 5G levels below international guidelines

Reasoning: Major global health organizations including WHO, FCC and UK HSA
have extensively researched 5G and found no causal link to cancer.
5G uses non-ionizing radiation which cannot damage DNA.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | Google ADK 1.28.0 |
| AI Model | Gemini 2.5 Flash |
| Custom Tools | 2 Python FunctionTools |
| Deployment | Google Cloud Run |
| Region | asia-south1 |
| Dev Environment | Google Cloud Shell |

---

## 📁 Project Structure
factshield/
└── factshield_agent/
├── init.py      ← Agent module init
├── agent.py         ← Main agent + FunctionTools
└── .env.example     ← API key template
requirements.txt         ← Dependencies

---

## 🧠 ADK Features Used

- ✅ `LlmAgent` with Gemini 2.5 Flash
- ✅ Custom `FunctionTool 1` — `extract_core_claim()`
- ✅ Custom `FunctionTool 2` — `calculate_credibility_score()`
- ✅ Structured JSON output via dynamic prompt
- ✅ Deployed on Google Cloud Run with HTTP endpoint

---

## 🏃 Run Locally

```bash
# Clone the repo
git clone https://github.com/Arushi2301/factshield-agent.git
cd factshield-agent

# Install dependencies
pip install google-adk

# Add your API key
cp factshield_agent/.env.example factshield_agent/.env
# Edit .env and add your GOOGLE_GENAI_API_KEY

# Run the agent
export GOOGLE_GENAI_API_KEY=your_key_here
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
adk run factshield_agent
```

---

## 📊 Test Claims

| Claim | Expected Verdict |
|---|---|
| 5G towers cause cancer | ❌ FALSE |
| Vaccines reduced polio worldwide | ✅ TRUE |
| Sugar causes hyperactivity in children | ⚠️ MISLEADING |
| The Earth is flat | ❌ FALSE |
| Bitcoin is legal in El Salvador | ✅ TRUE |
