# image_gen_ocr_eval

**Author:** Peter J. Bevan

**Date:** 15/12/23

This is a POC that calculates the normalised Levenshtein distance between prompted text and the text present in the generated image (as recognised by OCR).

To create a metric, we could create a dataset of prompts, each instructing to include some text in the image. We would also provide a column for ground truth generated text which contains only the instructed text. For each model to be evaluated, each of the prompts can be used to generate one or more images. The below script is then run on the generated images, comparing the target text with the actual text, outputting a score. This score is then averaged to give a benchmark score.

The dataset of prompts can be generated with by providing a template to an LLM and having it generate prompts.

**Note**: this is a distance metric, so 0 means the text is identical. We can also convert to a similarity with *1-distance*.

Currently I don't think there are any metrics that directly measure the text output of text-img generative models. Since this metric solely looks at text within the generated images and not image quality as a whole, this metric should be used alongside other benchmarks such as those in https://karine-h.github.io/T2I-CompBench/.
