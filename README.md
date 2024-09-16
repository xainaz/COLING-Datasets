
# COLING-Datasets

## MMAU Dataset Access and Benchmarking

The **MMAU** dataset evaluates LLM agent capabilities across multiple domains, including tool use, math, and coding challenges.

### Steps to Get Started:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/apple/axlearn.git
    cd axlearn
    ```

2. **Install Dependencies**

    ```bash
    pip install ".[mmau]"
    ```

3. **Dataset Preparation**

    - **Google Cloud** (Coming Soon):
      ```bash
      mkdir -p ./data/
      gsutil -m cp -r "gs://axlearn-public/datasets/mmau/20240712/*" ./data/
      ```

    - **Hugging Face** (Coming Soon):
      ```bash
      huggingface-cli download apple/mmau --local-dir ./data --repo-type dataset
      ```

---

## Mind2Web

Mind2Web provides a structured dataset to evaluate cross-domain generalization.

### Access the Dataset

- **Training Set**: Available on [Hugging Face](https://huggingface.co/datasets/osunlp/Mind2Web)

    ```bash
    git clone git@hf.co:datasets/osunlp/Mind2Web
    ```
- ** Test Set**: Available [here](https://buckeyemailosu-my.sharepoint.com/:u:/g/personal/deng_595_buckeyemail_osu_edu/EUkdc16xUC1EplDiXS1bvSEBOddFLgOyJNkWJOxdltNEGA?e=8N1D9S)
### Data Splits:

- **Train**: 1,009 instances
- **Test**:
    - **Cross Task**: 252 instances (tasks from the same website seen during training)
    - **Cross Website**: 177 instances (websites not seen during training)
    - **Cross Domain**: 912 instances (entire domains not seen during training)

### Data Fields:

- `annotation_id` (str): Unique ID for each task
- `website` (str): Website name
- `domain` (str): Website domain
- `subdomain` (str): Website subdomain
- `confirmed_task` (str): Task description
- `action_reprs` (list[str]): Human-readable representation of the action sequence
- `actions` (list[dict]): List of actions (steps) to complete the task
- `action_uid` (str): Unique ID for each action (step)
- `raw_html` (str): Raw HTML of the page before the action is performed
- `cleaned_html` (str): Cleaned HTML of the page before the action is performed
- `operation` (dict): Operation to perform
    - `op` (str): Operation type (CLICK, TYPE, SELECT)
    - `original_op` (str): Original operation type, containing HOVER and ENTER mapped to CLICK
    - `value` (str): Optional value for the operation (e.g., text to type)
- `pos_candidates` (list[dict]): Ground truth elements after preprocessing
- `tag` (str): Tag of the element
- `is_original_target` (bool): Whether the element is the original target labeled by the annotator
- `is_top_level_target` (bool): Whether the element is a top-level target found by the algorithm
- `backend_node_id` (str): Unique ID for the element
- `attributes` (str): Serialized attributes of the element (use `json.loads` to convert back to dict)
- `neg_candidates` (list[dict]): Other candidate elements in the page after preprocessing


## Natural Questions (NQ) Dataset Access

**Natural Questions (NQ)** is designed for training and evaluating question-answering systems, using real user queries and Wikipedia answers.

### Steps to Access the Dataset

1. **Visit the Dataset Page**:
   Access the official dataset and leaderboard:
   - [Natural Questions Dataset](http://ai.google.com/research/NaturalQuestions)

2. **Download the Dataset**:
   You can download the dataset directly from the official page linked above, which provides:
   - **Training Set**: 307,372 examples
   - **Development Set**: 7,830 examples
   - **Test Set**: 7,842 examples (hidden)

3. **Use Preprocessing Tools**:
   The repository provides preprocessing utilities and functions to simplify the dataset format. Use the `simplify_nq_example` function found in `data_utils.py` to transform the dataset into a more accessible format.

---

## TriviaQA Dataset Access

**TriviaQA** is a reading comprehension dataset containing over **650K** question-answer-evidence **triples**. TriviaQA includes **95K** question-answer pairs authored by trivia enthusiasts and independently gathered evidence documents, **six** per question on average, that provide high quality distant supervision for answering the questions.

### Steps to Access the Dataset

1. **Visit the TriviaQA Website**:
   Download the dataset directly from the official website:
   - [TriviaQA Website](http://nlp.cs.washington.edu/triviaqa/)

2. **Requirements**:
   Ensure you have the following installed:
   - Python 3
   - Python packages: `tensorflow` (if using BiDAF), `nltk`, `tqdm`

3. **Evaluate the Dataset**:
   To evaluate a model using the TriviaQA dataset, use the following command:

   ```bash
   python3 -m evaluation.triviaqa_evaluation --dataset_file samples/triviaqa_sample.json --prediction_file samples/sample_predictions.json
   ```
---

## GSM8K Dataset Access

**GSM8K (Grade School Math 8K)** is a dataset of 8.5K linguistically diverse grade school math word problems, designed to support question answering tasks that require multi-step reasoning.

### Steps to Access the Dataset

1. **Visit the Dataset Page**:
   You can access the GSM8K dataset directly on Hugging Face:
   - [GSM8K Dataset on Hugging Face](https://huggingface.co/datasets/openai/gsm8k)

2. **Install the Hugging Face Datasets Library**:
   To use the dataset, first install the `datasets` library:
   ```bash
   pip install datasets
   ```

3. **Load the Dataset**:
   After installing the library, you can load the dataset with the following code:
   ```python
   from datasets import load_dataset
   dataset = load_dataset("openai/gsm8k")
   ```

4. **Dataset Structure**:
   - **Training Set**: 7,473 examples
   - **Test Set**: 1,319 examples
   - Each example contains a math problem and a multi-step reasoning solution.

---

