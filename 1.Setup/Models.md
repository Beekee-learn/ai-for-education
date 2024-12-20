# Introduction

At the initial phase of our project, we identified several frameworks that facilitate the use of Large Language Models (LLM). Here is a non-exhaustive list of these frameworks:

-   **LLama.cpp**: A C++ framework optimized for using LLM on CPUs.
-   **Ollama**: A framework that uses LLama.cpp to make it simpler to use.
-   **HuggingFace**: The go-to platform for using LLM. It offers Python frameworks that make it easy to utilize pre-trained models.
-   **PyTorch**: The benchmark framework for using LLM. It offers pre-trained models and tools to use them.
  
# Model Selection

For this project, we have decided to select models designed for text generation. The choice that quickly became evident is the **Llama-2** model, which is an open-source text generation model. This choice is explained by the fact that this model has been widely used for fine-tuning specialized models in a variety of tasks and is therefore very well documented. As a result, by testing the technical performance of this model on the Raspberry Pi, we can get an idea of the performance of more specialized models.

We have therefore selected the Llama-2 model fine-tuned for the chatbot task. This model is a text generation model that has been fine-tuned on a large number of chatbot data and is therefore capable of generating coherent responses to questions posed by a user.

The model exists in three sizes: 7B, 13B, and 70B. Obviously, the 70B model is the most powerful, but it is also the heaviest and cannot be used on the Raspberry Pi. The 13B model is already very powerful, but we chose to test the 7B model, which is lighter and should therefore be easier to run on the Raspberry Pi.

## LLama.cpp

From the beginning of our exploration, LLama.cpp proved to be a promising option among others for our project. Developed in C++, this framework stands out for its flexibility and its ability to offer excellent performance when deploying large-scale language models (LLM). Its comprehensive documentation and the presence of an active community are significant assets. Furthermore, its ease of use allowed us to make efficient progress in our work, although it was not the only framework that caught our interest in this initial phase.

LLama.cpp also offers the performance metrics that interest us for our project, namely model loading time, prompt evaluation time, and text generation time.

## Implementation

Although it's possible to use LLama.cpp via Python interfaces, we opted for a direct approach via the command line to maximize performance. **Bash scripts** were developed to facilitate inference execution and data management.

## Parameters and Configurations

LLama.cpp offers a wide range of configurable parameters. We mainly kept the default settings, with two specific modifications:

**\--mlock**: Activates memory locking of model data, thus preventing it from being swapped to disk and ensuring consistent performance at the cost of higher RAM consumption.

**\--no-mmap**: Disables memory mapping of the model, which normally loads the necessary segments on demand. This option, although it extends the initial loading time, helps to prevent performance drops during inference phases.

We plan to conduct tests without these parameters activated to evaluate their impact on model loading time.

## Model Quantization

The Llama-2 model, despite its capabilities in text generation, presents challenges in terms of size for deployment on low-capacity devices, such as Raspberry Pis. With an initial size requiring about 28 GB of RAM for optimal use, the 7 billion parameter model exceeds the limits of low-power devices.

The solution lies in quantization, which allows for reducing the model size by adjusting the precision of the weights, moving from 32 bits to smaller formats such as 2 or 4 bits. This reduction in memory footprint is crucial for execution on limited platforms.

Our choice to work with quantized versions aims to evaluate the efficiency of these models on constrained devices and to measure the impact of quantization on performance. The 2-bit and 4-bit versions represent an interesting balance between reduced size and quality preservation, which is particularly relevant for resource-limited contexts.

On the [**HuggingFace**](https://huggingface.co/ "https://huggingface.co") platform, we identified a contributor, [**TheBloke**](https://huggingface.co/TheBloke "https://huggingface.co/TheBloke"), who offers quantized versions of the Llama-2 7B model. These adapted models are particularly interesting for our experiments on Raspberry Pi, due to their various levels of quantization.

Here are the models we have decided to evaluate:

-   **Llama-2 7B at 2 bits**: \[HuggingFace link\]([https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q2\_K.gguf](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q2_K.gguf "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q2_K.gguf"))
-   **Llama-2 7B at 4 bits**: \[HuggingFace link\]([https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4\_K\_M.gguf](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf"))

The following versions are also available:

-   **Llama-2 7B at 6 bits**: \[HuggingFace link\]([https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q6\_K.gguf](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q6_K.gguf "https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q6_K.gguf"))
-   **Llama-2 7B at 8 bits**: \[HuggingFace link\]([https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q8\_0.gguf](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q8_0.gguf "https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q8_0.gguf"))

Our goal is to examine how these two levels of quantization affect performance on Raspberry Pi.

The expected memory consumption for each model is as follows:

-   At 2 bits: **5.33 GB**
-   At 4 bits: **6.58 GB**
-   At 6 bits: **8.03 GB**
-   At 8 bits: **9.66 GB**

For more details, this information is available on the [**HuggingFace**](https://huggingface.co/ "https://huggingface.co/") profile of [**TheBloke**](https://huggingface.co/TheBloke "https://huggingface.co/TheBloke") concerning the Llama-2 7B model.

## Model Format

In the realm of quantized models, we have several formats available, including GPTQ, AWK, and **GGUF**. While GPTQ and AWK are optimized for GPUs, GGUF is designed for **CPUs**.

We have chosen GGUF for our models, due to its good integration with CPUs, which is ideal for devices like Raspberry Pis. GGUF aims to improve efficiency on CPUs by reducing latency and managing resources better, which is essential to ensure good performance on devices with limited capacities.
