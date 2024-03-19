import os
import pandas as pd
import time
from collections import defaultdict
import imagen_hub
from imagen_hub.utils import save_pil_image, get_concat_pil_images

from imagen_hub.loader.infer_dummy import load_ocr_eval
from scorer import calculate_text_similarity
from arguments import parse_args

def generate_images(args):
    test_data = load_ocr_eval(get_one_data=args.DEBUG)#get_one_data=True)

    if args.DEBUG:
        filtered_test_data = [test_data]
    else:
        filtered_test_data = []
        type_counter = defaultdict(int)
        for item in test_data:
            if type_counter[item['type']] < args.num_samples_each_type:
                filtered_test_data.append(item)
                type_counter[item['type']] += 1

    instruction = """ All text is clearly visible on one line. \
    Only quoted text is present in image and only appears once. \
    All text is roughly horizontal and easily readable."""

    language_list = ["en"]
    scores = defaultdict(lambda: defaultdict(list))
    for model_name in args.model_list:
        responses = []
        print(f"Generating images for model: {model_name}")
        type_count = defaultdict(int)
        # Define a directory where you want to save the images
        output_dir = f"outputs/generated_images/{model_name}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        model = imagen_hub.load(model_name)
        for i, data in enumerate(filtered_test_data):
            task_type = data['type']
            # if type_count[task_type] < args.num_samples_each_type:
                # Increment the count for this type
            type_count[task_type] += 1
            prompt = data["prompt"] + instruction
            target_txt = data["quoted_text"]
            filename = f"{model_name}_generated_image_{task_type}_{i}.png"
            filepath = f"outputs/generated_images/{model_name}/{filename}"

            if not os.path.exists(filepath):
                output = model.infer_one_image(prompt=prompt, seed=42).resize((512,512))
                save_pil_image(output, output_dir, filename)
                print(f"Image saved to {os.path.join(output_dir, filename)}")
                if model_name in ["DALLE2","DALLE3"]:
                    time.sleep(20)  # Circumvent rate limiting
            else:
                print(f"Image {filename} already exists")

            spelling_score, generated_txt = calculate_text_similarity(filepath, target_txt)
            scores[model_name][task_type].append(spelling_score)
            responses.append({'image_filepath': image_filepath, 'model': model_name, 'task': task_type, 'target': target_txt, 'generated': generated_txt, 'score': spelling_score})
            
        responses_df = pd.DataFrame(responses)
        responses_df.to_csv(f"outputs/responses/{model_name}_responses.csv", index=False)


if __name__ == '__main__':
    logger = logging.getLogger('ppocr')
    logger.setLevel(logging.WARN)

    file = get_file_path("hf.env")
    hf_key = read_key_from_file(file)
    print(f"Read key from {file}")
    login(token=hf_key)

    args = parse_args()
    generate_images(args)
