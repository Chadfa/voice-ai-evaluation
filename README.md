# Voice AI Evaluation Pipeline

## Overview
This project implements a deterministic evaluation framework for voice AI assistants.

Pipeline:
Audio → Whisper Transcription → LLM Response (Ollama) → Evaluation Metrics

## Architecture

Audio Input
   ↓
Whisper (Speech-to-Text)
   ↓
LLM (Ollama / llama3)
   ↓
Evaluation Engine
   ↓
Metrics + JSON Report

## Metrics

- Latency: End-to-end processing time
- WER (Word Error Rate): Transcription accuracy
- Semantic Similarity: Embedding cosine similarity
- Hallucination Detection: Extra information detection

## Determinism

The evaluation pipeline ensures deterministic scoring using fixed random seeds.

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Start Ollama

ollama serve

3. Run evaluation

python run_evaluation.py

## Output

Evaluation results are stored in:

reports/evaluation_report.json