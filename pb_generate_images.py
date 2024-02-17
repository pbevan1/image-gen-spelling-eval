import os
import imagen_hub
from imagen_hub.loader.infer_dummy import load_ocr_eval
from imagen_hub.utils import save_pil_image, get_concat_pil_images
from huggingface_hub import login
from imagen_hub.utils.file_helper import get_file_path, read_key_from_file


file = get_file_path("hf.env")
hf_key = read_key_from_file(file)
print(f"Read key from {file}")
login(token=hf_key)

dummy_data = load_ocr_eval(get_one_data=True)
instruction = """All text is clearly visible with no obstruction. \
Only the quoted text is visible. \
No other text should be visible in the image. \
There is only one instance of the requested text in the image."""

model_list = ["SD", "SDXL", "DALLE2", "DALLE3", "StableUnCLIP", "DeepFloydIF", "DreamBooth", 
"DreamBoothLora", "Kandinsky", "PixArtAlpha", "TextualInversion", "UniDiffuser"]
language_list = ["en"]
for model_name in model_list:
    # Define a directory where you want to save the images
    output_dir = f"generated_images/{model_name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    model = imagen_hub.load(model_name)
    # for i, data in enumerate(dummy_data):
    prompt = dummy_data["prompt"] + instruction
    output = model.infer_one_image(prompt=prompt, seed=42).resize((512,512))
    filename = f"{model_name}_generated_image_1.png"
    save_pil_image(output, output_dir, filename)

    print(f"Image saved to {os.path.join(output_dir, filename)}")
