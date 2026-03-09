import time

from pipeline.transcription import transcribe_audio
from pipeline.llm_interface import query_llm
from pipeline.metrics import compute_wer, semantic_similarity, hallucination_detect


def run_evaluation(audio_path, reference_text, expected_answer):

    start_time = time.time()

    transcript, latency = transcribe_audio(audio_path)

    llm_output = query_llm(transcript)

    total_latency = time.time() - start_time

    wer_score = compute_wer(reference_text, transcript)

    similarity = semantic_similarity(expected_answer, llm_output)

    hallucination = hallucination_detect(expected_answer, llm_output)

    report = {
        "transcript": transcript,
        "llm_output": llm_output,
        "latency": total_latency,
        "wer": wer_score,
        "semantic_similarity": similarity,
        "hallucination": hallucination
    }

    return report