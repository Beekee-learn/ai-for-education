## APEX Phase 1 / ai-for-education.org
Beekee Learning By Doing projects as part of AI-for-Education.org

Purpose
=======

The purpose of APEX Phase 1 is to verify the feasibility and initial pedagogical value of making LLMs work offline on Single-Board Computers (e.g. Raspberry Pi or equivalents). 
If successful, this would suggest that applications of AI could be made available offline hence opening up access to AI on the edge in schools and locations in Low and Middle Income Countries (LMICs) where meaninful connectivity and power and is often lacking.

Executive Summary
=======
Our primary goal was to explore the feasibility and performance of generative AI models on low-capacity devices such as Raspberry Pi. We reached the following conclusions:

1.  Model Evaluation: We evaluated various quantized versions of the Llama-2 model (2-bit, 4-bit, 6-bit, and 8-bit) to determine their performance on Raspberry Pi 5. The models were assessed based on memory consumption, CPU load, power consumption, and CPU temperature.

2.  Implementation: We successfully implemented the Llama.cpp framework in C++ for efficient deployment of large-scale language models (LLM) on Raspberry Pi. This included developing Bash scripts to facilitate inference execution and data management.

3.  Performance Metrics: We defined and measured key performance metrics, including model loading time, input evaluation time, and response generation time. These metrics provided insights into the feasibility and efficiency of deploying text generation models on resource-limited devices.

4.  Applications Explored: We investigated various AI applications on Raspberry Pi, such as text generation, question-answering, document summarization, translation, and code generation. This exploration highlighted the versatility and potential of AI on low-capacity devices but raises a major concern on the validity, educational quality, and relevance for an 'out of of the box' usage.

Lessons Learned
=======
1.  We learned that a Single-Board Computer like the Raspberry Pi could be effectively used for lightweight generative Artificial Intelligence tasks, but only for a limited number of users -- realistically one. This defines the scope of application for offline AI initially for a teacher (1) or teaching supporting roles.

2.  We learned that to cope with the constraints in memory of Single-Board Computers, asynchronous paradigms should be further explored to enable more users (e.g. students) to benefit from offline AI models.

    1.  For instance, a first-in-first-out queue system with an estimated waiting time could be explored (similar to a ticket). For this approach to work, a substantial amount of upstream guidance and verification for submitting the prompt is required to avoid misuse of resources, affecting other users in the queue.

3.  We learned that **there's a very high presence of hallucination** when using directly the readily available models, which raises **concerns for educators and users who do not possess critical thinking skills**.

    1.  A techno-centric solution to this problem consists of the use of Retrieval-Augmented Generation, which remains to be practically explored a further stage project (APEX Phase 2)

    2.  A human-centered solution, which could be used in conjunction with RAGs, lies in providing training for teachers and learners not only about prompting but also about the limitations of generative lightweight offline AI, and by extension general AI. The fact that these systems are limited in their capacities also provides an opportunity for developing critical thinking skills for learners, who should judge the answer from AI systems based on discipline-specific criteria.

Explore more
=======
- [1. Setup](/1.Setup)
    - [1.1 Tasks](/1.Setup/Tasks.md)
    - [1.2 Models](/1.Setup/Models.md)
    - [1.3 Metrics](/1.Setup/Metrics.md)
    - [1.4 Methods](/1.Setup/Methods.md)
- [2. Measurements] (/2.Measurements)
    - [2.1 Temperature] (/2.Measurements/temperature.md)
    - [2.2 CPU] (/2.Measurements/cpu.md)
    - [2.3 Memory] (/2.Measurements/memory.md)
    - [2.4 Energy and Power] (/2.Measurements/energyPower.md)
    - [2.5 Inference time] (/2.Measurements/inferenceTime.md)
- [3. Datasets] (3./Dataset)
