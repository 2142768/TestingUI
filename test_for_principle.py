import os
import json
from langchain_community.chat_models import AzureChatOpenAI
from pprint import pprint

# Set environment variables
os.environ["OPENAI_API_KEY"] = "6ffhCm6wvgxD2LRD7wNZI5sHgqHn4lqYOY7xn8Ycdg7vHvZ8qyujJQQJ99BCACYeBjFXJ3w3AAABACOGwuFA"
os.environ["OPENAI_API_VERSION"] = "2024-05-01-preview"

# Initialize Azure OpenAI GPT model
def initialize_chat_model(temperature=0.0):
    return AzureChatOpenAI(
        deployment_name="gpt-4o",
        azure_endpoint="https://tcoeaiteamgpt4o.openai.azure.com/",
        temperature=temperature
    )


def principles_summarization_prompt(json_data):
    prompt = f"""

             You are an AI expert in compliance and responsible AI assurance. Your task is to analyze the provided {json_data} containing multiple `fast_principles` entries and produce a consolidated list by merging duplicate entries while retaining unique ones. Duplicates are entries with the same `principle_name` or highly similar `principle_desc` or `principle_guide` in terms of intent, purpose, or ethical goal (e.g., both address fairness, transparency, or privacy). The output must account for all input entries, either by merging duplicates or retaining unique entries.

              **Merging Duplicates**:
              For entries identified as duplicates, merge them into a single entry with:
              - **Merged Principle Name**: Select the most descriptive `principle_name` or create a combined name that reflects the shared intent.
              - **Merged Principle Description**: Integrate `principle_desc` entries into a cohesive summary, preserving all critical details without redundancy.
              - **Merged Principle Guide**: Combine `principle_guide` entries into a unified set of best practices, ensuring no essential steps are omitted.
              - **Principle Reason**: Combine the original `principle_reason` entries, explaining their original purposes and including a clear rationale for merging based on shared intent, purpose, or ethical goal.
              

              **Retaining Unique Entries**:
              For entries that are unique (not duplicates or highly similar), retain them in their original form, preserving all fields (`principle_name`, `principle_desc`, `principle_guide`, `principle_reason`) without modification.

              **Validation**:
              - Ensure all input entries are accounted for in the output, either as part of a merged entry or as a unique entry.
              - Validate that no entries are omitted or incorrectly merged by comparing the input and output counts.
              - Entries are duplicates only if they target the same ethical or design objective (e.g., fairness, transparency, privacy). Distinct objectives (e.g., fairness vs. accountability) must remain separate.

              **Output Format**:
              - Return a JSON array containing all entries (merged and unique).
              - For merged entries, include a `combine_reason` field to explain the merger.
              - For unique entries, retain the original structure without a `combine_reason` field.
              - Ensure the output contains exactly the number of entries resulting from merging duplicates and retaining unique ones, with no entries omitted.
              - Return only the final JSON output with no additional explanations or text.

              **Notes**:
              - Prioritize clarity, conciseness, and completeness in merged descriptions, guides, and reasons.
              - Explicitly validate that no input entry is omitted or incorrectly merged.
              - Focus on ethical and design objectives, ensuring merged entries reflect the shared intent of the principles.


    """

    chat_model = initialize_chat_model()
    response = chat_model.call_as_llm(prompt)

    return response


# Function to load JSON data from a file
def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# Main execution
def main():
    # json file path
    json_file_path = 'C:/Users/SVNDSWFST/Desktop/genai_chatbot/qea_responsible_ai/advisory_agent_results.json'

    # Load JSON data
    json_data = load_json_data(json_file_path)
    fast_principles_list = []
    for item in json_data:
        fast_principles_list.extend(item['fast_principles'])
    print("fast_principles_list:", len(fast_principles_list))

    # Process the output
    final_response = principles_summarization_prompt(fast_principles_list)
    print("\nFinal Response:")
    print(final_response)


# Run the script
if __name__ == "__main__":
    main()
