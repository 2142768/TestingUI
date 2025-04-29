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


def metric_summarization_prompt(json_data):
    prompt = f"""

    You are an AI expert in compliance and responsible AI assurance. Your task is to analyze and merge duplicate responsible AI metrics in the provided {json_data}, which contains multiple metrics. 
    Merge only metrics that are duplicates, meaning they have identical or near-identical intent, purpose, or goal, with minimal semantic differences. Keep unique metrics unchanged.The merged metric should contain:

    Merged Metric Name: A logical combination of the duplicate metric names or the most representative name.
    Merged Metric Description: A cohesive description combining both metrics, preserving all essential information without redundancy.
    Validation Steps: A consolidated list of unique validation steps from the original metrics, omitting duplicates.
    Justification Reason: The original justifications for each metric, plus a rationale explaining why the metrics were merged due to their identical intent, purpose, or goal.


    For unique metrics with distinct intents, purposes, or goals, retain them individually with their original information.

    Output Format:
    The output must be in JSON format.
    For merged metrics, the justification_reason should include both original justifications and the rationale for merging.
    For unmerged metrics, retain the original format with their respective justification_reason.
    Return only the final JSON output with merged and unmerged metrics. No explanations or additional text.
  
    Instructions:
    Compare metric_name and metric_description to identify duplicates. Metrics are duplicates only if they have identical or near-identical intent, purpose, or goal (e.g., both measure "Scalability" with similar descriptions).
    Merge duplicate metrics by combining their names, descriptions, and validation steps, ensuring no critical information is lost.
    Retain unique metrics with distinct intents, purposes, or goals (e.g., "Privacy Protection" vs. "Data Accuracy") unchanged.
    Ensure merged metrics have unique validation steps, avoiding redundancy.
    Provide merged and unmerged metrics in JSON format, each with metric_name, metric_description, validation_steps, and justification_reason.
    STRICTLY merge metrics only if they are clear duplicates with near-identical intent, purpose, or goal.
    STRICTLY do not merge metrics with distinct intents, purposes, or goals, even if they share some similarities.
    Ensure all critical validation steps and justifications are retained in merged metrics, avoiding redundancy.


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
    # metric list
    metric_list =[]
    for item in json_data:
        metric_list.extend(item['metrices'])
    print("metric_list:", len(metric_list))
    final_response = metric_summarization_prompt(metric_list)
    print("\nFinal Response:")
    print(final_response)

# Run the script
if __name__ == "__main__":
    main()