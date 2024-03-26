from huggingface_hub import HfApi, Repository
import shutil

# Define your model name and path to the .safetensors file
model_name = "pbevan11/stable-diffusion-2-typography"
model_path = "sd-scripts/stable-diffusion-2-typography"

# Path to the local clone of your model repository
local_repo_path = "./hf_repos"

# Clone the repository from Hugging Face
repo = Repository(local_repo_path, clone_from=f"https://huggingface.co/{model_name}")

shutil.copy(model_path, repo.local_dir)

# Commit and push the .safetensors file to your Hugging Face repository
repo.git_add()
repo.git_commit("Add fine-tuned Stable Diffusion model")
repo.git_push()

print(f"Model uploaded successfully. Check it at https://huggingface.co/{model_name}")
