import weave
from weave import Dataset
import pandas as pd
import run
from tqdm import tqdm
import time

weave.init('benchmark')

def load_test_data(benchmark_name):
    # Load the test data
    retrieved_dataset = weave.ref(benchmark_name).get()
    return retrieved_dataset

def run_benchmark(benchmark_name, test_name, run_function, rag_ip, batch_size=50, batch_no=0):
    """Runs a benchmark test by generating responses for a batch of prompts and logs the results.
        benchmark_name (str): The name of the benchmark to run.
        test_name (str): The name of the test, should be formatted as benchmark_name + "-" + model_user + "-" + run_function + "-" + where_it_runs.
        run_function (callable): The function used to generate responses for the prompts.
        batch_size (int, optional): The number of prompts to process in each batch. Defaults to 50.
        last_run (int, optional): The index of the last run, used to calculate the starting index for the current batch. Defaults to 0.
    _summary_
    """
    
    # Load the benchmark dataset
    test_dataset = load_test_data(benchmark_name)
    retrieved_dataset = []
    start_index = batch_no * batch_size
    end_index = start_index + batch_size
    start_time = time.time()
    for i in tqdm(range(start_index, min(end_index, len(test_dataset.rows)))):
        prompt = test_dataset.rows[i]['prompt']
        if run_function == "rag_sierra_5" or run_function == "rag_sierra_2":
            response, questions, answers = run.generate_response(prompt, run_function, rag_ip)
            data = {
                "id": i,
                "prompt": prompt,
                "response": response,
                "questions": questions,
                "answers": answers
            }
        else:
            response = run.generate_response(prompt, run_function, rag_ip)
            data = {
                "id": i,
                "prompt": prompt,
                "response": response
            }
        retrieved_dataset.append(data)

    # Publish the dataset
    dataset = Dataset(name=test_name+"-batch"+str(batch_no + 1)+"-"+str(batch_size), rows=retrieved_dataset)
    weave.publish(dataset)
    
    # Add log data    
    log_data = {
        "benchmark_name": benchmark_name,
        "run_function": run_function,
        "batch_size": batch_size,
        "batch_no": batch_no,
        "duration": time.time() - start_time
    }
    print("--------------------------------------------------")
    print("END OF TEST : ", test_name+"-batch"+str(batch_no + 1)+"-"+str(batch_size))
    print("Logged data: ", log_data)

