import os
import pandas as pd
from collections import defaultdict

from arguments import parse_args

def calculate_scores(args):
    all_responses = []
    # Loop through each model's responses file and append to a single DataFrame
    for model_name in args.model_list:
        filepath = f"outputs/{model_name}_responses.csv"
        if os.path.exists(filepath):
            model_responses = pd.read_csv(filepath)
            all_responses.append(model_responses)

    if not all_responses:
        print("No response data found.")
        return

    combined_responses = pd.concat(all_responses, ignore_index=True)
    scores = defaultdict(lambda: defaultdict(list))

    for _, row in combined_responses.iterrows():
        model_name = row['model']
        task_type = row['task']
        score = row['score']
        scores[model_name][task_type].append(score)

    # Calculate average scores from the populated dictionary
    data_for_df = defaultdict(dict)
    for model_name, task_types in scores.items():
        total_score = 0
        total_count = 0
        for task_type, scores_list in task_types.items():
            average_score = sum(scores_list) / len(scores_list)
            data_for_df[model_name][task_type] = average_score
            total_score += sum(scores_list)
            total_count += len(scores_list)
        overall_average = total_score / total_count if total_count else 0
        data_for_df[model_name]['Overall'] = overall_average

    df = pd.DataFrame.from_dict(data_for_df, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Model'}, inplace=True)
    df.to_csv("outputs/final_scores.csv", index=False)
    print(df)


if __name__ == '__main__':
    args = parse_args()
    calculate_scores(args)