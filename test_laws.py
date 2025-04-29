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


def laws_summarization_prompt(json_data):
    prompt = f"""

          You are an AI expert in compliance and responsible AI assurance. Your task is to analyze the provided {json_data} containing multiple `article_laws` entries and produce a consolidated list by merging duplicate entries while retaining unique ones. Duplicates are entries that pertain to the same `law` and have highly similar `article`, `title`, or `description` in terms of intent, purpose, or compliance goal (e.g., both address transparency or data protection). The output must account for all input entries, either by merging duplicates or retaining unique entries.

          **Merging Duplicates**:
          For entries identified as duplicates, merge them into a single entry with:
          - **Merged Law**: The common `law` of the merged entries.
          - **Merged Article**: Combine the article numbers (e.g., "Articles 9 and 13") or select the most representative article if they serve the same purpose.
          - **Merged Title**: Create a combined title that reflects the shared intent or select the most descriptive title.
          - **Merged Description**: Integrate descriptions into a cohesive summary, preserving all critical details without redundancy.
          - **Reason**: Combine the original reasons, explaining their original purposes and including a clear rationale for merging based on shared intent, purpose, or compliance goal.
          - **Applicability**: Select the highest applicability level or justify a new level based on the merged scope.
          - **Applicability Reason**: Combine      Combine applicability reasons, ensuring alignment with the merged entry’s purpose.
          - **Combine Reason**: Explicitly state why the entries are duplicates, focusing on their shared intent, purpose, or compliance goal (e.g., both address transparency or data protection).

          **Retaining Unique Entries**:
          For entries that are unique (not duplicates or highly similar), retain them in their original form, preserving all fields (`law`, `article`, `title`, `description`, `reason`, `applicability`, `applicability_reason`) without modification.

          **Validation**:
          - Ensure all input entries are accounted for in the output, either as part of a merged entry or as a unique entry.
          - Validate that no entries are omitted or incorrectly merged by comparing the input and output counts.
          - Entries are duplicates only if they target the same compliance aspect (e.g., transparency, data protection) or have overlapping goals. Distinct aspects (e.g., transparency vs. accountability) must remain separate.

          **Output Format**:
          - Return a JSON array containing all entries (merged and unique).
          - For merged entries, include a `combine_reason` field to explain the merger.
          - For unique entries, retain the original structure without a `combine_reason` field.
          - Ensure the output contains exactly the number of entries resulting from merging duplicates and retaining unique ones, with no entries omitted.
          - Return only the final JSON output with no additional explanations or text.
          - Make sure it contain all the article laws from the input given.

          **Notes**:
          - Prioritize clarity, conciseness, and completeness in merged descriptions, titles, and reasons.
          - If applicability levels differ in merged entries, choose the highest or justify a new level.
          - Explicitly validate that no input entry is omitted or incorrectly merged.
          - Focus on legal and compliance objectives, ensuring merged entries reflect the shared regulatory intent.



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
    json_file_path ='C:/Users/SVNDSWFST/Desktop/genai_chatbot/qea_responsible_ai/advisory_agent_results.json'

    # Load JSON data
    json_data = load_json_data(json_file_path)
    article_laws_list = []
    for item in json_data:
        article_laws_list.extend(item['article_laws'])
    print("article_laws:", len(article_laws_list))

    # Process the output 
    final_response = laws_summarization_prompt(article_laws_list)
    print("\nFinal Response:")
    print(final_response)


# Run the script
if __name__ == "__main__":
    main()