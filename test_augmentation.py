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


def aug_summarization_prompt(json_data):
    prompt = f"""

        You are an AI expert in compliance and responsible AI assurance. Your task is to analyze and merge duplicate responsible AI augmentations in the provided {json_data}, which contains multiple augmentations. The goal is to identify and combine augmentations that are duplicates or highly similar in intent, purpose, or goal, while retaining unique augmentations as they are. For each pair or group of augmentations identified as duplicates, merge them into a single augmentation with the following details:

        - **Merged Augmentation Name**: Select the most descriptive name or create a combined name that logically represents the merged augmentations.
        - **Merged Augmentation Description**: Combine the descriptions into a cohesive summary that preserves all essential information without redundancy.
        - **Augmentation Examples**: Merge examples from the augmentations, ensuring no critical example is omitted and removing redundant examples.make sure origial ,augumented and parameter is added.
        - **Combine Reason**: Explain why the augmentations are considered duplicates, focusing on their shared intent, purpose, or goal.
        - **Justification Reason**: Combine the original justification reasons, ensuring the merged reason aligns with the purpose of the augmentations.
        - **Applicability**: Select the highest applicability level from the merged augmentations or justify a new level if appropriate.
        - **Applicability Reason**: Combine the applicability reasons, ensuring clarity and alignment with the merged augmentation’s purpose.

        For augmentations that are unique (not duplicates or highly similar), retain them in their original form without modification.

        **Output Format**:
        - Return a JSON array containing all augmentations.
        - For merged augmentations, include the `combine_reason` field to explain the merger.
        - For unique augmentations, retain the original structure without a `combine_reason` field.
        - Ensure the output includes only the final JSON with merged and unique augmentations, with no additional explanations or text.

        **Notes**:
        - Augmentations are considered duplicates if they target the same aspect of testing (e.g., audio noise, speech variation, text ambiguity) or have overlapping goals (e.g., simulating real-world conditions, testing robustness).
        - When merging, prioritize clarity, conciseness, and completeness in descriptions and examples.
        - If applicability levels differ, choose the highest or justify a new level based on the merged scope.
        - Do not modify the structure of unique augmentations.
        - STRICTLY include all the augmentations.

    """

    # prompt = f"""
    # You are an AI expert in compliance and responsible AI assurance. Your task is to analyze and merge the responsible AI augmentations in the following {json_data}, which contains multiple augmentations. For each pair of augmentations that align with the same intent, purpose, or goal, merge them into a single augmentation. The merged augmentation should contain:
    #
    # Merged Augmentation Name: The name of the merged augmentation (choose the most appropriate or combine them logically).
    #
    # Merged Augmentation Description: A combined description of both augmentations, ensuring that the essential information is not lost and is presented cohesively.
    #
    # Augmentation Examples: Combine the examples from both augmentations, ensuring no critical example is omitted.
    #
    # Combine Reason: Explain why these two augmentations are being combined. Focus on the alignment of their goals, purpose, or the specific intent they measure. Provide a clear rationale for the combination.
    #
    # Justification Reason: Include the justification for each augmentation as provided in the original input, ensuring that the reason for the combination aligns with the original purpose of each augmentation.
    #
    # If augmentations are not combined, retain them individually with their original information.
    #
    # Output format:
    # If augmentations are combined, the output should be in JSON format, with the combine_reason explaining the combination, and keep the structure as augment_name and augment_description as in the input.
    #
    # If augmentations are not combined, they should remain in the original format.
    # Return only the final JSON output with merged augmentations. No explanations or additional text.
    #             """

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
    augmentations_list = []
    for item in json_data:
        augmentations_list.extend(item['augmentations'])
    print("(augmentations:", len(augmentations_list))

    final_response = aug_summarization_prompt(augmentations_list)
    print("\nFinal Response:")
    print(final_response)


# Run the script
if __name__ == "__main__":
    main()