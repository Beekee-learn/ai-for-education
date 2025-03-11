import sys
import evaluate

def get_benchmark_name():
    mapping = {
        "1": "gsm8k",
        "2": "mmlu",
        "3": "Winogrande"
    }
    user_input = input("Enter benchmark number (1.gsm8k, 2.mmlu, 3.Winogrande) > ")
    if user_input in mapping:
        return mapping[user_input]
    else:
        print("Invalid benchmark number")
        sys.exit(1)

def get_run_function():
    mapping = {
        "1": "classic",
        "2": "rag_sierra_2",
        "3": "rag_sierra_5"
    }
    user_input = input("Enter run function (1.classic, 2.RAG context 2, 3.RAG context 5) > ")
    if user_input in mapping:
        return mapping[user_input]
    else:
        print("Invalid run function")
        sys.exit(1)

def main():
    benchmark_name = get_benchmark_name()
    run_function = get_run_function()

    if len(sys.argv) < 4:
        print("Usage: python run_benchmark.py <model> <batch_no> <ip_rag>")
        sys.exit(1)

    try:
        # Note: model and batch_size are both set from sys.argv[1] in the original code.
        model = int(sys.argv[1])
        batch_size = int(sys.argv[1])
        batch_no = int(sys.argv[2])
    except ValueError:
        print("Model, batch_size, and batch_no must be integers")
        sys.exit(1)

    ip_rag = sys.argv[3] if sys.argv[3] != "0.0.0.0" else "0.0.0.0"

    model_run_on = "llama_cpp"
    device = "raspberry_5"
    
    test_name = f"{benchmark_name}-{model_run_on}-{model}-{run_function}-{device}"
    
    evaluate.run_benchmark(
        benchmark_name=benchmark_name,
        test_name=test_name,
        run_function=run_function,
        batch_size=batch_size,
        batch_no=batch_no,
        rag_ip=ip_rag
    )

if __name__ == "__main__":
    main()
