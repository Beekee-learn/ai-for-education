# Methods

As said in the previous section, we chose different approaches to assess the performance of text generation on the Raspberry Pi:

-   **Model loading time**: To measure the time needed to load the model into memory, we used the command \`sudo sysctl vm.drop\_caches=3\` to clear the memory cache, then we timed the model loading. We repeated this operation several times to get an average.
-   **Input evaluation time**: To evaluate the time needed to process an input and start text generation, we used a set of texts ranging from 100 to 800 words that we submitted to the model. We then measured the time needed for the model to start generating a response.
-   **Response generation time**: To measure the time needed to produce the response, we submitted questions of varying complexity to the model and timed the response time after the input evaluation.
-   **RAM usage**: We used a script that reads the \`/proc/meminfo\` file to obtain the amount of memory used by the model. We selected the following metrics: MemTotal, MemFree, MemAvailable, Buffers, Cached, SwapTotal, SwapFree, Committed\_AS, Mlocked, Mapped.
-   **CPU load**: We used the \`mpstat\` command to obtain processor usage statistics. Here is the command used: \`mpstat -P all -o JSON 1\` which provides the average processor usage statistics of the 4 cores of the Raspberry Pi.
-   **Power consumption**: We used a wattmeter to measure the power consumption of the Raspberry Pi during the different inference phases.
-   **CPU temperature**: We used the \`vcgencmd measure\_temp\` command to measure the SoC temperature of the Raspberry Pi. We took measurements every second during the inference phases.
