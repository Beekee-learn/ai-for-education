## Identification of Potential Tasks

In the initial phase, our project explored a range of tasks suitable for the Raspberry Pi, encompassing various aspects of artificial intelligence and natural language processing. Among these, we considered:

-   **Text generation**, to automatically produce written content.
-   **Question-answering processing**, to provide precise answers to specific inquiries.
-   **Document analysis and interpretation**, to extract and synthesize key information.
-   **Document summarization**, to condense long texts into essential points.
-   **Translation between languages**, to facilitate multilingual communication.
-   **Text-to-text transformation**, to rephrase or adapt content.
-   **Text-to-speech conversion**, to generate a vocal output from written text.
-   **Image production based on textual descriptions**, to visualize concepts or ideas.
-   **Text recognition in images**, to extract and process written information on visual media.
-   **Completion of masked text segments**, to predict missing words or phrases.
-   **Image classification**, to identify and categorize visual elements.
-   **Object detection in images**, to locate and recognize specific objects.
-   **Development of conversational agents**, to simulate natural dialogues.
-   **Automatic code generation**, to convert natural language descriptions into executable computer code.
-   **Text evaluation**, to assess the quality of written responses.

These tasks represent a wide array of AI application possibilities on compact devices, highlighting the potential of the Raspberry Pi in various contexts.

## Focus on Text Generation

We chose to focus on text generation, a task both versatile and suited to many contexts. It can be used to create automatic responses, summaries, translations, or even code from descriptions. This task also presents an interesting challenge in terms of computational resources, making it an excellent candidate to test performance.

## Model Selection: Llama-2

For this project, we have decided to select models designed for text generation. The choice that quickly became evident is the Llama-2 model, which is an open-source text generation model. This choice is explained by the fact that this model has been widely used for fine-tuning specialized models in a variety of tasks and is therefore very well documented. As a result, by testing the technical performance of this model on the Raspberry Pi, we can get an idea of the performance of more specialized models.

We have therefore selected the Llama-2 model fine-tuned for the chatbot task. This model is a text generation model that has been fine-tuned on a large number of chatbot data and is therefore capable of generating coherent responses to questions posed by a user.

The model exists in three sizes: 7B, 13B, and 70B. Obviously, the 70B model is the most powerful, but it is also the heaviest and cannot be used on the Raspberry Pi. The 13B model is already very powerful, but we chose to test the 7B model, which is lighter and should therefore be easier to run on the Raspberry Pi.

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

## Metrics

To assess the effectiveness of text generation on a Raspberry Pi, we defined the following criteria:

-   **Model loading time**: Duration to load the model into memory.
-   **Input evaluation time**: Duration to process the input and start text generation.
-   **Response generation time**: Time required to produce the response.

In parallel, to measure the impact on the Raspberry Pi, we took into account:

-   **RAM usage**: Amount of memory used.
-   **CPU load**: Processor usage level.
-   **Power consumption**: Energy and power used during the operation.
-   **CPU temperature**: Temperature evolution during the process.

These indicators will help us understand the feasibility and efficiency of deploying text generation models on limited capacity devices.

## Methods

As said in the previous section, we chose different approaches to assess the performance of text generation on the Raspberry Pi:

-   **Model loading time**: To measure the time needed to load the model into memory, we used the command \`sudo sysctl vm.drop\_caches=3\` to clear the memory cache, then we timed the model loading. We repeated this operation several times to get an average.
-   **Input evaluation time**: To evaluate the time needed to process an input and start text generation, we used a set of texts ranging from 100 to 800 words that we submitted to the model. We then measured the time needed for the model to start generating a response.
-   **Response generation time**: To measure the time needed to produce the response, we submitted questions of varying complexity to the model and timed the response time after the input evaluation.
-   **RAM usage**: We used a script that reads the \`/proc/meminfo\` file to obtain the amount of memory used by the model. We selected the following metrics: MemTotal, MemFree, MemAvailable, Buffers, Cached, SwapTotal, SwapFree, Committed\_AS, Mlocked, Mapped.
-   **CPU load**: We used the \`mpstat\` command to obtain processor usage statistics. Here is the command used: \`mpstat -P all -o JSON 1\` which provides the average processor usage statistics of the 4 cores of the Raspberry Pi.
-   **Power consumption**: We used a wattmeter to measure the power consumption of the Raspberry Pi during the different inference phases.
-   **CPU temperature**: We used the \`vcgencmd measure\_temp\` command to measure the SoC temperature of the Raspberry Pi. We took measurements every second during the inference phases.

## Introduction

At the initial phase of our project, we identified several frameworks that facilitate the use of Large Language Models (LLM). Here is a non-exhaustive list of these frameworks:

-   **LLama.cpp**: A C++ framework optimized for using LLM on CPUs.
-   **Ollama**: A framework that uses LLama.cpp to make it simpler to use.
-   **HuggingFace**: The go-to platform for using LLM. It offers Python frameworks that make it easy to utilize pre-trained models.
-   **PyTorch**: The benchmark framework for using LLM. It offers pre-trained models and tools to use them.

## LLama.cpp

From the beginning of our exploration, LLama.cpp proved to be a promising option among others for our project. Developed in C++, this framework stands out for its flexibility and its ability to offer excellent performance when deploying large-scale language models (LLM). Its comprehensive documentation and the presence of an active community are significant assets. Furthermore, its ease of use allowed us to make efficient progress in our work, although it was not the only framework that caught our interest in this initial phase.

LLama.cpp also offers the performance metrics that interest us for our project, namely model loading time, prompt evaluation time, and text generation time.

### Implementation

Although it's possible to use LLama.cpp via Python interfaces, we opted for a direct approach via the command line to maximize performance. **Bash scripts** were developed to facilitate inference execution and data management.

### Parameters and Configurations

LLama.cpp offers a wide range of configurable parameters. We mainly kept the default settings, with two specific modifications:

**\--mlock**: Activates memory locking of model data, thus preventing it from being swapped to disk and ensuring consistent performance at the cost of higher RAM consumption.

**\--no-mmap**: Disables memory mapping of the model, which normally loads the necessary segments on demand. This option, although it extends the initial loading time, helps to prevent performance drops during inference phases.

We plan to conduct tests without these parameters activated to evaluate their impact on model loading time.

## Text Evaluation

An intriguing avenue for exploration is the application of models dedicated to text evaluation. These models, capable of assessing responses against a set of criteria, hold immense potential for the educational sector. By automating the evaluation process, we can provide immediate feedback to learners, thereby enhancing the learning experience. A example of this application involves evaluating students' explanations of complex concepts, comparing their responses with reference answers, and grading them based on a predefined rubric. This not only streamlines the assessment process but also ensures consistency and objectivity in evaluations.

## Local Translation

Another promising direction involves the integration of automatic translation models. Tailoring these models to function autonomously on devices with limited computing power, such as Raspberry Pis, can revolutionize communication within isolated multilingual communities. This capability would enable the seamless translation of essential documents, facilitate communication in medical or emergency situations, and support educational initiatives in multiple languages.

## Code Generation

Exploring the potential of code generation models represents a significant leap forward. Enabling these models to generate code from natural language descriptions on less powerful devices could democratize programming education and software development, especially in regions with limited internet access. This approach could empower individuals to learn new programming languages and bring their ideas to life, fostering innovation and creativity.

## Diversified Model Architectures

A logical progression for this project involves evaluating the performance of models with different architectures, such as Mistral models, or those designed for tasks other than text generation. Understanding how these varied architectures and specializations perform in our targeted environment could lead to more tailored and effective AI applications. This exploration is crucial for identifying models that offer the best balance between performance and resource efficiency.

## Framework Exploration

Continuing our project, a deep dive into the capabilities and offerings of platforms like **HuggingFace** becomes essential. **HuggingFace**, known for its extensive range of pre-trained models and user-friendly tools, can serve as a valuable resource for expanding our project's scope. By leveraging the platform's models and tools, we can experiment with a wider array of applications and potentially discover new ways to enhance our project's effectiveness and reach.
