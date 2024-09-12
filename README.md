# COLING-Datasets

This repository provides test datasets from various resources to benchmark LLM agents across multiple domains. One of the key datasets used in this benchmark is **MMAU**.

## MMAU Dataset

The **MMAU** dataset provides diverse tasks designed to evaluate agent capabilities such as understanding, reasoning, planning, problem-solving, and self-correction. It consists of over 3,000 distinct prompts from 20 different tasks sourced from:

- **In-house Tool-use Data**: Tasks under tool use and Directed Acyclic Graph (DAG) QA.
- **Kaggle Datasets**: Rewritten for Data Science and Machine Learning (DS & ML) coding tasks.
- **CodeContest**: Advanced programming challenges for contest-level coding.
- **DeepMind Math Dataset**: Rigorous mathematical problems for evaluating computational abilities.

### Quick Start

To get started with the **MMAU** dataset:

### 1. Clone the Repository

Start by cloning the official MMAU repository to access the dataset and tools for evaluation:

```bash
git clone https://github.com/apple/axlearn.git
cd axlearn
```

### 2. Install Dependencies

Install the necessary dependencies for the MMAU dataset:

```bash
# Install all dependencies required for MMAU metrics.
pip install ".[mmau]"
```

If you're only interested in generator tasks, you can install with:

```bash
pip install ".[open_api]"
```

### 3. Dataset Preparation

Currently, the dataset can be downloaded from the following locations:

#### Download from Google Cloud (Coming Soon)

```bash
mkdir -p ./data/
gsutil -m cp -r "gs://axlearn-public/datasets/mmau/20240712/*" ./data/
```

#### Download from Hugging Face (Coming Soon)

```bash
huggingface-cli download apple/mmau --local-dir ./data --repo-type dataset
```

### 4. Running Benchmarks

#### Generate Responses

To generate responses from the target client (e.g., OpenAI), use the following example:

```bash
export OPENAI_API_KEY=<your_openai_key>
MODEL=gpt-3.5-turbo-0125
EVAL_SET=tool_use_single_step_20240712.jsonl
CLIENT_NAME=openai
python3 -m axlearn.open_api.generator \
  --model $MODEL \
  --client_name $CLIENT_NAME \
  --input_file ./data/$EVAL_SET \
  --output_file ./generated_data/$MODEL/$EVAL_SET \
  --decode_parameters '{"temperature": 0.0, "max_tokens": 1024}'
```

This will generate responses based on the input data using the OpenAI client.

#### Evaluate Responses

To evaluate the generated responses, run the following command:

```bash
EVAL_SET=tool_use_single_step_20240712.jsonl
MODEL=gpt-3.5-turbo-0125
python3 -m axlearn.open_api.evaluator \
  --input_file ./generated_data/$MODEL/$EVAL_SET \
  --output_file ./metrics/$MODEL/$EVAL_SET \
  --metric_name tool_use_execution
```

You can change the `--metric_name` parameter for different benchmarks, such as:

- `tool_use_plan`
- `math`
- `code_contests`
- `code_kaggle`

### Additional Benchmarks

You can also set up benchmarks for different clients, including **Gemini** and **Anthropic**. For example, to use **Gemini**, modify the commands as follows:

```bash
export VERTEX_AI_PROJECT=<your_project_name>
export VERTEX_AI_LOCATION=<your_project_location>
MODEL=gemini-1.0-pro
CLIENT_NAME=gemini
```

For **Anthropic**, use:

```bash
export ANTHROPIC_API_KEY=<sk-xxxx>
MODEL=claude-3-haiku-20240307
CLIENT_NAME=anthropic
```

### TODO

- Add a script to launch all benchmarks.
- Integrate additional Open API clients.
- Enable Hugging Face dataset loading directly.

### Citation

If you use the **MMAU** dataset in your research, please cite:

```plaintext
@article{patil2024mmau,
  title={MMAU: A Holistic Benchmark of Agent Capabilities Across Diverse Domains},
  author={Guoli Yin, Felix Bai, Shuang Ma, Zirui Wang, et al.},
  year={2024},
  url={https://github.com/apple/axlearn/docs/research/mmau},
  journal={https://arxiv.org/abs/2407.18961},
}
```

---

## Other Datasets

In addition to **MMAU**, this repository includes other datasets for testing and benchmarking LLM agent performance across various domains. Detailed instructions for setting up and using these datasets will be added as more resources are integrated.
