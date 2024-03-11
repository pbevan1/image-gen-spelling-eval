from paddleocr import PaddleOCR
import Levenshtein


def calculate_text_similarity(generated_image_path, target_txt):
  target_txt = target_txt.lower()
  ocr = PaddleOCR(use_gpu=True, lang='en')

  result = ocr.ocr(generated_image_path, cls=True)

  try:
    words, confidences = zip(*[(item[1][0], item[1][1]) for item in result[0]])

    generated_txt = ' '.join(words).lower()
    average_confidence = sum(confidences) / len(confidences)
  except TypeError as te:
    print(te)
    generated_txt = ''
  print(f"Target text: {target_txt}\nGenerated text: {generated_txt}")
  # Calculate the Levenshtein distance
  normalised_levenshtein_distance = Levenshtein.distance(target_txt, generated_txt) / max(len(target_txt), len(generated_txt))
  normalised_levenshtein_similarity = 1-normalised_levenshtein_distance
  print(f"Normalised Levenshtein similarity: {normalised_levenshtein_similarity}")

  return normalised_levenshtein_similarity, generated_txt
