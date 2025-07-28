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

We conducted experiments on Automatic Speech Recognition (ASR) and Speaker Verification (SV) tasks to evaluate the dataset.

### 1️⃣ ASR Results

#### Models Trained from Scratch

| Encoder     | Loss       | # Params | Greedy | Beam  | Attention | Attention Rescoring |
| :---------- | :--------- | :------- | :----- | :---- | :-------- | :------------------ |
| Transformer | CTC+AED    | 29M      | 34.55  | 34.4  | 40.61     | 32.15               |
| Conformer   | CTC+AED    | 31M      | 28.73  | 28.72 | 31.60     | 27.38               |
| Conformer   | RNN-T+AED  | 45M      | 37.11  | 37.14 | 33.84     | 37.14               |
| Paraformer  | Paraformer | 30M      | 31.86  | 28.94 | -         | -                   |

#### Fine-tuned Pre-trained Models

| Model           | # Params | Zero-shot | Fine-tuning |
| :-------------- | :------- | :-------- | :---------- |
| CW              | 122M     | 18.05     | 13.66       |
| Whisper-tiny    | 39M      | 67.63     | 28.78       |
| Whisper-base    | 74M      | 51.49     | 23.33       |
| Whisper-small   | 244M     | 37.99     | 17.45       |
| Whisper-medium  | 769M     | 28.55     | 18.97       |
| Whisper-large-v2| 1,550M   | 29.43     | -           |


#### More Pre-trained Models

| Model           | # Params | Zero-shot | 
| :-------------- | :------- | :-------- | 
| Qwen-Audio      |  7.7B   | 20.39     | 
| Qwen2-Audio    |  8.2B   | 11.54     | 
| SenseVoice (Small)    |   234M   | 11.89     | 


### 2️⃣ SV Results
|      Model      | # Params | Dim | Dev (%) | EER (%) | minDCF | EER (%) | minDCF  |
|:---------------:|:--------:|:---:|:-------:|:-------:|:------:|:-------:|:-------:|
|    x-vector    |   4.2M   | 512 |   75.4  |  8.91  | 0.7198 |  25.92 |  0.9780  |
|  ECAPA-TDNN   |  20.8M   | 192 |   84.6  | 13.72 | 0.8697 | 27.77  | 0.9490 |
| ResNet-TDNN |   15.5M  |  256  |  91.9  |   9.57  | 0.6597 | 22.11  | 0.9044 |



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
