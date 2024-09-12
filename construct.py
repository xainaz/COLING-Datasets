import json
from datasets import load_dataset

samples = []

def sample_dataset(dataset_name, sample_size):
    dataset = load_dataset(dataset_name, split='train', streaming=True)
    sampled_data = []

    for item in dataset:
        sampled_data.append(item)
        if len(sampled_data) >= sample_size:
            break

    for item in sampled_data:
        question_text = item.get("question", {}).get("text", "No question text found")

        annotations = item.get("annotations", [])
        long_answer = "No long answer found"
        if annotations and isinstance(annotations[0], dict) and "long_answer" in annotations[0]:
            long_answer_candidate_index = annotations[0]["long_answer"].get("candidate_index", "No index")
            long_answer = f"Long answer candidate index: {long_answer_candidate_index}"
        
        samples.append({"input": question_text, "output": long_answer})

sample_dataset("natural_questions", 25)

with open("nq_sample_data.json", "w") as f:
    json.dump(samples, f, indent=2)

print("Sample data saved to nq_sample_data.json")
