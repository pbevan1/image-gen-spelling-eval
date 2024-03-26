
# image-gen-spelling-eval

**Author:** Peter J. Bevan

**Date:** 15/12/23

<a target="_blank" href="https://colab.research.google.com/github/pbevan1/image_gen_ocr_eval/blob/main/image_gen_ocr_evaluation.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

---
*Table 1: Normalised Levenshtein similarity scores between instructed text and text present in image (as identified by OCR)*

| Model | object | signage | natural | long | Overall |
| --- | --- | --- | --- | --- | --- |
| DALLE3 | 0.62 | 0.62 | 0.62 | 0.58 | 0.61 |
| DeepFloydIF | 0.57 | 0.56 | 0.66 | 0.39 | 0.54 |
| DALLE2 | 0.44 | 0.35 | 0.42 | 0.22 | 0.36 |
| SDTypography | 0.33 | 0.35 | 0.39 | 0.26 | 0.33 |
| SDXL | 0.3 | 0.33 | 0.4 | 0.21 | 0.31 |
| SD | 0.28 | 0.26 | 0.32 | 0.22 | 0.27 |
| PlayGroundV2 | 0.19 | 0.23 | 0.17 | 0.2 | 0.2 |
| Wuerstchen | 0.14 | 0.19 | 0.19 | 0.19 | 0.18 |
| Kandinsky | 0.13 | 0.2 | 0.18 | 0.17 | 0.17 |

---

This is a POC that calculates the normalised Levenshtein similarity between prompted text and the text present in the generated image (as recognised by OCR).

To us this to create a metric, we create a dataset of prompts, each instructing to include some text in the image. We also provide a column for ground truth generated text which contains only the instructed text. The below scorer is then run on the generated images, comparing the target text with the actual text, outputting a score. The scores are then averaged to give a benchmark score. A score of 1 indicates a perfect match to the text.

You can find the dataset at https://huggingface.co/datasets/pbevan11/image_gen_ocr_evaluation_data

Since this metric solely looks at text within the generated images and not image quality as a whole, this metric should be used alongside other benchmarks such as those in https://karine-h.github.io/T2I-CompBench/.

---

![Image generation model spelling comparison](examples/model_comparison.png)


```
@misc{image-gen-ocr-eval,
  title = {image_gen_ocr_eval},
  author = {Peter Bevan},
  year = {2024},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://huggingface.co/datasets/pbevan11/image_gen_ocr_evaluation_data}},
}
```