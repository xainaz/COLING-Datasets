import os
import json

# Use after download data from hugging face 

folder_path = './data'
output_folder = './data/modified'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder_path):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as jsonl_file:
            with open(os.path.join(output_folder, filename), 'w') as modified_file:
                for line in jsonl_file:
                    data = json.loads(line)
                    
                    if "messages" in data:
                        # Filter out None values and join non-None content
                        input_text = " ".join(msg["content"] for msg in data["messages"] if msg.get("content") is not None)
                        output_data = {k: v for k, v in data.items() if k != "messages"}
                        
                        modified_data = {
                            "input": input_text,
                            "output": output_data
                        }
                        
                        modified_file.write(json.dumps(modified_data) + '\n')
