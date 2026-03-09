import json
from pipeline.config import set_seed
from pipeline.evaluator import run_evaluation

set_seed()

audio_file = "audio/sample.mp4"

reference_transcript = "What is the status of my loan application?"

expected_answer = "Your loan application status can be checked through the bank portal."

report = run_evaluation(audio_file, reference_transcript, expected_answer)

print(report)

with open("reports/evaluation_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("Evaluation report saved.")