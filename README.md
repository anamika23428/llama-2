# Llama-2-7B-Chat Model

This repository contains the Llama-2-7B-Chat model files, specifically the quantized version optimized for performance.

## Model Description

- **Model Name:** Llama-2-7B-Chat
- **Type:** Quantized model
- **Usage:** Suitable for various chat applications and scenarios.

## Download Link

You can download the model file from the following link:

[Download Llama-2-7B-Chat Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin)

## How to Use

To use this model, you can follow these steps:

1. **Download the model** using the link above.
2. **Load the model** in your application using the appropriate libraries (e.g., Hugging Face Transformers).
3. **Utilize the model** for your chat applications.

## License

Please check the model's license on the Hugging Face page to ensure compliance with usage rights.

## Acknowledgments

This model is part of the Llama series developed by [Hugging Face](https://huggingface.co/).

For more information, you can visit the [Hugging Face Model Hub](https://huggingface.co/models).
# Blog Generator App

## Overview
The **Blog Generator** app is a web application built using **Streamlit** and **LangChain**. It allows users to generate blogs on any topic by specifying the number of words and the desired writing style. The app uses a **Llama-2** language model for text generation, implemented via `CTransformers`. This app is ideal for users who want to quickly generate text based on specific prompts.

## Features
- **Interactive User Interface**: Users can input a blog topic, select the number of words, and choose the writing style.
- **Dynamic Prompting**: A customizable prompt template that adjusts based on user input to generate high-quality text.
- **Llama-2 Model**: The app leverages the Llama-2 model to generate coherent and meaningful blog content based on the provided input.

## Installation

### Prerequisites
- **Python 3.8+** installed.
- Basic knowledge of Python and Streamlit is beneficial.
- Ensure you have access to the necessary model binaries.

### Step 1: Clone the Repository
Begin by cloning the repository to your local environment:
```bash
git clone <repository-url>
```
### step 2: Install Dependencies
Navigate to the project directory and install all the required Python packages:

```
pip install streamlit langchain ctransformers
```
### Step 3: Download the Model
Download the Llama-2 model and place it in a directory named model/. Ensure the binary is named llama-2-7b-chat.ggmlv3.q8_0.bin.


### Step 4: Run the Application
Start the Streamlit app using the following command:

```
streamlit run blog_generation.py
```
This will launch the app in your default web browser. You should now be able to generate blogs based on your input.
