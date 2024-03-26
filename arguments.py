import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Image Generation Spelling Benchmark")
    parser.add_argument('--model_list', type=list, help='List of models', default=[
        # "DALLE2", "DALLE3", "Kandinsky", "DeepFloydIF", "Wuerstchen", "SD", "SDXL", "PlayGroundV2"
        "SDTypography"
        ])
    parser.add_argument('--num_samples_each_type', type=str, help='Number of images to generate and test from each prompt type', default=50)
    parser.add_argument('--DEBUG', action='store_true', help='DEBUG mode')

    args = parser.parse_args()

    return args