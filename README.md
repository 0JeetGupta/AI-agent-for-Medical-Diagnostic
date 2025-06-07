# 🧠 AI-Powered Multi-Agent Medical Diagnosis System

This project is a **Streamlit-based AI application** that simulates a team of medical experts—Cardiologist, Psychologist, and Pulmonologist—using **specialized AI agents** to analyze a patient's medical report and collaboratively produce a final diagnosis.

---

## 🚀 Features

- 🩺 **Domain-Specific AI Agents**: Each agent mimics a specialist's diagnostic approach.
- 🤝 **Multidisciplinary Team Agent**: Synthesizes outputs from all specialists to offer a unified diagnosis.
- 📄 **Medical Report Upload**: Accepts `.txt` reports as input.
- 🧪 **Google Gemini Integration**: Uses Gemini Pro (via `google.generativeai`) for medical reasoning.
- 🌐 **Streamlit Web UI**: Interactive, user-friendly frontend for uploading reports and viewing results.
- 💡 **Free-Tier Friendly**: No paid APIs or subscriptions needed.

---

## 📂 Project Structure

```
├── app.py                  # Streamlit frontend
├── utils/
│   └── agent.py            # AI agent logic (Cardiologist, Psychologist, etc.)
├── requirements.txt        # Python dependencies
├── .env                    # Your Gemini API key (not included in repo)
└── sample_report/          # Example patient reports (optional)
```

---

## 🧬 How It Works

1. Upload a patient’s medical report (`.txt` file).
2. Each AI agent analyzes the report from its specialty's perspective.
3. A final multidisciplinary diagnosis is generated and shown.
4. Result is saved to `results/final_diagnosis.txt`.

---

## 📦 Setup Instructions

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/medical-ai-agent.git
cd medical-ai-agent
pip install -r requirements.txt
```

Add your Gemini API key in a `.env` file:

```env
GOOGLE_API_KEY=your_key_here
```

Run the Streamlit app:

```bash
streamlit run app.py
```

> ⚠️ Replace `your_key_here` with your actual Gemini API key.

---

## 🧠 Why It Matters

This project showcases how **multi-agent AI systems** can emulate human expert collaboration, opening pathways for AI-assisted second opinions, clinical triage tools, and decision support in healthcare.

---

## 📬 Contributions

Pull requests, ideas, and feedback are welcome!
