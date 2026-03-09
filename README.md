# Voice AI Evaluation Pipeline

## Overview

This project implements a **deterministic evaluation framework for Voice AI systems**.
It evaluates the performance of a voice assistant pipeline consisting of speech recognition, LLM reasoning, and response generation.

The framework measures multiple evaluation metrics and generates **structured JSON reports** for reproducible benchmarking.

---

## System Architecture

```
Audio Input
    ↓
Whisper Speech-to-Text
    ↓
Transcription
    ↓
Local LLM (Ollama / Llama3)
    ↓
Generated Response
    ↓
Evaluation Engine
    ↓
Metrics + JSON Report
```

---

## Key Features

* **Speech Recognition:** Uses Whisper for accurate audio transcription.
* **Local LLM Integration:** Uses Ollama with Llama3 for deterministic inference.
* **Evaluation Metrics:** Measures system quality using multiple metrics.
* **Deterministic Evaluation:** Fixed seeds and controlled parameters ensure reproducible results.
* **Modular Architecture:** Each component is isolated for easy experimentation and testing.
* **JSON Reporting:** Evaluation results are automatically saved for analysis.

---

## Evaluation Metrics

### 1. Latency

Measures end-to-end processing time for the full pipeline.

```
Audio → Transcription → LLM Response
```

### 2. Word Error Rate (WER)

Evaluates transcription accuracy.

WER = (Substitutions + Deletions + Insertions) / Total Words

### 3. Semantic Similarity

Uses sentence embeddings to measure how closely the LLM response matches the expected answer.

Model used:

* `sentence-transformers/all-MiniLM-L6-v2`

### 4. Hallucination Detection

Detects when the model generates unsupported information compared to the expected answer.

A deterministic rule flags hallucinations when the response introduces excessive new tokens not present in the reference.

---

## Project Structure

```
voice-ai-evaluation
│
├── audio
│   └── sample.mp4
│
├── pipeline
│   ├── config.py
│   ├── transcription.py
│   ├── llm_interface.py
│   ├── metrics.py
│   └── evaluator.py
│
├── reports
│
├── run_evaluation.py
├── requirements.txt
└── README.md
```

---

## Determinism Guarantees

The evaluation pipeline is designed to produce **consistent results across runs**.

Techniques used:

* Fixed random seeds
* Deterministic evaluation logic
* Controlled LLM generation parameters

Example configuration:

```
temperature = 0
top_p = 1
random_seed = 42
```

---

## How to Run

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Start the Local LLM Server

```
ollama serve
```

Ensure the Llama3 model is installed:

```
ollama run llama3
```

### 3. Run the Evaluation Pipeline

```
python run_evaluation.py
```

---

## Example Output

```
{
  "transcript": "What is the status of my loan application?",
  "llm_output": "...",
  "latency": 43.57,
  "wer": 0.0,
  "semantic_similarity": 0.79,
  "hallucination": true
}
```

The report is saved to:

```
reports/evaluation_report.json
```

---

## Future Improvements

Potential extensions for this framework:

* Multi-sample batch evaluation
* Advanced hallucination detection using retrieval grounding
* Confidence scoring for LLM outputs
* Visualization dashboards for evaluation metrics

---

## Technologies Used

* Python
* Whisper
* Ollama
* Llama3
* Sentence Transformers
* JiWER
* NumPy

---

## Author

**Sheik Fareedh S**

AI / ML / Generative AI Internship Candidate
