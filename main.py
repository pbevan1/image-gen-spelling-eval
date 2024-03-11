import logging
from huggingface_hub import login
from imagen_hub.utils.file_helper import get_file_path, read_key_from_file


def main(args):
    generate_images(args)
    calculate_scores(args)


if __name__ == '__main__':
    logger = logging.getLogger('ppocr')
    logger.setLevel(logging.WARN)

    file = get_file_path("hf.env")
    hf_key = read_key_from_file(file)
    print(f"Read key from {file}")
    login(token=hf_key)

    args = parse_args()
    main(args)