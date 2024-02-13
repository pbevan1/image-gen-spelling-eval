import pandas as pd

df = pd.read_csv("prompts/image_gen_ocr_evaluation_prompts.csv")

df['quoted_text'] = df['prompt'].str.extract(r'"([^"]*)"')

df = df[['prompt', 'quoted_text', 'type']]

df.to_csv("prompts/image_gen_ocr_evaluation_prompts_gt.csv", index=False)

print(df)