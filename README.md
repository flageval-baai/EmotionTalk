# EmotionTalk: An Interactive Chinese Multimodal Emotion Dataset With Rich Annotations

[![Hugging Face Datasets](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Datasets-yellow)](https://huggingface.co/datasets/BAAI/Emotiontalk)
[![arXiv](https://img.shields.io/badge/arXiv-2502.18913-b31b1b.svg)](https://arxiv.org/pdf/2505.23018)
[![License: CC BY-NC-SA-4.0](https://img.shields.io/badge/License-CC%20BY--SA--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
## ⭐ Introduction

This repository contains the **EmotionTalk** dataset, an interactive Chinese multimodal emotion dataset with rich annotations. This dataset provides multimodal information from 19 actors participating in dyadic conversation settings, incorporating acoustic, visual, and textual modalities. It includes 23.6 hours of speech (19,250 utterances), annotations for 7 utterance-level emotion categories (happy, surprise, sad, disgust, anger, fear, and neutral), 5-dimensional sentiment labels (negative, weakly negative, neutral, weakly positive, and positive) and 4-dimensional speech captions (speaker, speaking style, emotion and overall). '

## 🚀 Dataset Details

This dataset contains 23.6 hours of spontaneous dialogue recordings. Key features of the dataset include:

* **Speakers:** 19 speakers.
* **Audio Format:**  WAV files with a 44.1kHz sampling rate. 
* **Label:**  Happy, angry, sad, disgusted, fear, surprise, neutral. 
* **Annotations:** The dataset includes annotations for each modality.
  * **Text modality:** `data` (each annotator's labeling results), `emotion_result`, `speaker_id`, `file_name` (file path), `content` (transcription).
  * **Audio modality:** `data` (each annotator's labeling results), `emotion_result`, `speaker_id`, `paragraphs` (timestamp), `sourceAttr` (caption), `file_name` (file path), `content` (transcription).
  * **Video modality:** `data` (each annotator's labeling results), `emotion_result`, `speaker_id`, `file_name` (file path).
  * **Multimodal:** `data` (each annotator's labeling results), `emotion_result`, `Continuous label_result`, `speaker_id`, `file_name` (file path).

### Dataset Statistics
The dataset is split into three subsets:
|          | Angry | Disgusted | Fearful | Happy | Neutral | Sad  | Surprised | Total  |
| :------- | :---- | :-------- | :------ | :---- | :------ | :--- | :-------- | :----- |
| Train    | 2950  | 1142      | 672     | 2986  | 5377    | 919  | 1367      | 15413  |
| Val(G01/G12) | 409   | 95        | 125     | 360   | 675     | 111  | 133       | 1908   |
| Test(G03/G15) | 339   | 134       | 125     | 246   | 801     | 123  | 161       | 1929   |
| **Total**| **3698**| **1371** | **922** | **3592**| **6853**| **1153**| **1661** | **19250**|

For more details, please refer to our paper [EmotionTalk](https://arxiv.org/pdf/2505.23018).

## 📐 Experiments

We conducted experiments on Unimodal Emotion Recognition, Multimodal Emotion Recognition / Sentiment Analysis and Emotional Speaker Style Captioning tasks to evaluate the dataset.

### 1️⃣ Unimodal Emotion Recognition Results
#### Speech modality
|      Model    | Speech(Four) | Multi(Four) | Speech(All) | Multi(All) | Mean  |
| :-------------- | :----------- | :--------------- | :---------- | :-------------- | :---- |
| Whisper-Base    | 71.03        | 60.44            | 56.61       | 48.47           | 59.14 |
| Whisper-Large   | 75.45        | 61.90            | 60.34       | 49.56           | 61.81 |
| WavLM-Base      | 72.50        | 62.96            | 59.72       | 53.14           | 62.08 |
| Wav2vec 2.0-Base| 77.31        | 63.85            | 62.16       | 50.96           | 63.57 |
| Wav2vec 2.0-Large| 76.22        | 64.68            | 63.14       | 51.06           | 63.78 |
| WavLM-Large     | 76.67        | 64.48            | 61.90       | 53.91           | 64.24 |
| Hubert-Base     | **82.88** | **73.69** | 66.15       | 61.12           | 70.96 |
| Hubert-Large    | 81.09        | 73.09            | **68.64** | **62.52** | **71.34** |
#### Text modality
|      Model      | Text(Four) | Multi(Four) | Text(All) | Multi(All) | Mean  |
| :-------------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| Vicuna-7B       | 55.24      | 46.26      | 45.57     | 43.91      | 47.75 |
| LERT-Base       | 59.68      | 51.36      | 46.09     | 38.26      | 48.85 |
| DeBERTa-Large   | 57.46      | 49.11      | 44.89     | 44.79      | 49.06 |
| BERT-Base       | 57.66      | 50.83      | 46.50     | 44.69      | 49.92 |
| Sentence-BERT   | 56.52      | 52.15      | 46.45     | 45.05      | 50.04 |
| BLOOM-7B        | 60.87      | 50.56      | 47.38     | 43.23      | 50.51 |
| ChatGLM2-6B     | **60.95**  | 55.47      | 46.19     | 41.16      | 50.94 |
| RoBERTa-Large   | 59.48      | 53.88      | 46.86     | 44.27      | 51.12 |
| RoBERTa-Base    | 60.15      | 50.96      | 48.11     | **45.52**  | 51.19 |
| Baichuan-7B     | 60.08      | **56.39**  | **48.21** | 41.84      | **51.63** |
#### Visual modality
|      Model    | Visual(Four) | Multi(Four) | Visual(All) | Multi(All) | Mean  |
| :-------------- | :----------- | :--------------- | :---------- | :-------------- | :---- |
| Datal2vec-Base  | 35.72        | 29.69            | 40.44       | 32.92           | 34.69 |
| VideoMAE-Base   | 54.18        | 47.51            | 54.33       | 46.29           | 50.58 |
| EVA-02-Base     | 69.87        | 54.27            | 58.84       | 38.88           | 55.47 |
| VideoMAE-Large  | 62.36        | 64.74            | 55.68       | 50.54           | 58.33 |
| CLIP-Base       | 71.38        | 63.95            | 59.51       | 49.09           | 60.98 |
| DINOv2-Large    | 70.60        | 68.99            | 60.96       | **54.59** | 63.79 |
| DINOv2-Giant    | 73.42        | 69.58            | 62.73       | 53.76           | 64.87 |
| CLIP-Large      | **77.81** | **73.96** | **64.75** | 54.17           | **67.67** |

### 2️⃣ Multimodal Emotion Recognition Results

| Features    | Algorithms | Fusion       | Multimodal(Four) | Multimodal(All) | Mean  |
| :---------- | :--------- | :----------- | :--------------- | :-------------- | :---- |
|             | MCTN       | Frame-level  | 65.34            | 47.80           | 56.57 |
|             | MFM        | Frame-level  | 75.94            | 59.51           | 67.73 |
| Hubert-Base | GMFN       | Frame-level  | 76.87            | 63.66           | 70.27 |
|             | MMIN       | Utterance-level | 78.93         | 64.54           | 71.74 |
| Baichuan-7B | MISA       | Utterance-level | 80.58         | 66.77           | 73.68 |
|             | TFN        | Utterance-level | 80.12         | 68.27           | 74.20 |
| CLIP-Large  | MulT       | Frame-level  | 82.17            | 66.67           | 74.42 |
|             | MFN        | Frame-level  | 80.38            | **69.31** | 74.85 |
|             | Attention  | Utterance-level | 82.11         | 68.17           | 75.14 |
|             | LMF        | Utterance-level | **81.31** | 69.10           | **75.21** |

### 3️⃣ Multimodal Sentiment Analysis Results

| # Top | Text         | Speech       | Visual      | Discrete(Four) | Discrete(All) | Continuous | Mean  |
| :---- | :----------- | :----------- | :---------- | :------------- | :------------ | :--------- | :---- |
| Top 1 | Baichuan-7B  | Hubert-Base  | CLIP-Large  | 81.31          | 69.10         | **93.35** | 81.25 |
| Top 2 | RoBERTa-Base | Hubert-Large | DINOv2-Giant| **83.23** | **69.21** | 93.16      | **81.87** |
| Top 3 | RoBERTa-Large| WavLM-Large  | DINOv2-Large| 78.13          | 65.01         | 93.10      | 78.75 |
| Top 4 | ChatGLM2-6B  | W2v 2.0-Large| CLIP-Base   | 73.82          | 63.50         | 92.26      | 76.53 |


### 4️⃣ Emotional Speaker Style Captioning Results

|          | Decoder         | BLEU₄ | ROUGE_L | METEOR | SPIDER | FENSE | BERTScore | CLAPScore |
| :------- | :-------------- | :---- | :------ | :----- | :----- | :---- | :-------- | :-------- |
| Speaker  | Transformer-based | 0.011 | 0.397   | 0.204  | 0.229  | 0.842 | 0.974     | 0.860     |
|          | GPT-2           | **0.020** | **0.430** | **0.212** | 0.256 | 0.765 | 0.976     | **0.899** |
|          | Qwen-2          | 0.009 | 0.414   | 0.205  | **0.258** | **0.846** | **0.977** | 0.878     |
| Style    | Transformer-based | 0.065 | 0.517   | 0.313  | 0.339  | 0.512 | 0.985     | 0.895     |
|          | GPT-2           | 0.075 | 0.510   | 0.298  | 0.350  | **0.611** | 0.987     | 0.850     |
|          | Qwen-2          | **0.127** | **0.564** | **0.339** | **0.482** | 0.523 | **0.988** | **0.912** |
| Emotion  | Transformer-based | 0.032 | 0.366   | 0.191  | 0.276  | 0.932 | 0.973     | 0.843     |
|          | GPT-2           | 0.014 | **0.399** | 0.147  | 0.235  | 0.903 | 0.972     | 0.818     |
|          | Qwen-2          | **0.058** | 0.361   | **0.199** | **0.353** | **0.942** | **0.975** | **0.853** |
| Overall  | Transformer-based | 0.018 | 0.469   | 0.233  | **0.230** | **0.921** | 0.980     | 0.878     |
|          | GPT-2           | 0.015 | 0.462   | 0.214  | 0.227  | 0.890 | 0.980     | 0.849     |
|          | Qwen-2          | **0.033** | **0.535** | **0.268** | 0.121  | 0.562 | **0.984** | **0.885** |


## 🤗 Dataset Download

You can access the ChildMandarin dataset on HuggingFace Datasets:

[https://huggingface.co/datasets/BAAI/Emotiontalk](https://huggingface.co/datasets/BAAI/Emotiontalk)



##  📚 Cite me
```
@article{sun2025emotiontalk,
  title={EmotionTalk: An Interactive Chinese Multimodal Emotion Dataset With Rich Annotations},
  author={Sun, Haoqin and Wang, Xuechen and Zhao, Jinghua and Zhao, Shiwan and Zhou, Jiaming and Wang, Hui and He, Jiabei and Kong, Aobo and Yang, Xi and Wang, Yequan and others},
  journal={arXiv preprint arXiv:2505.23018},
  year={2025}
}
```
