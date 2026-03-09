from jiwer import wer
from sentence_transformers import SentenceTransformer, util

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_wer(reference, transcript):
    return wer(reference.lower(), transcript.lower())


def semantic_similarity(reference, llm_output):
    emb1 = model.encode(reference, convert_to_tensor=True)
    emb2 = model.encode(llm_output, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2)

    return float(score)


def hallucination_detect(reference, llm_output):

    ref_words = set(reference.lower().split())
    out_words = set(llm_output.lower().split())

    extra_words = out_words - ref_words

    if len(extra_words) > 5:
        return True

    return False