
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

