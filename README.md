# Kubernetes Preemptive Pod Calculator

This tool calculates and visualizes the distribution of preemptive pods needed across failure domains for Kubernetes autoscaling. It helps ensure that there are enough preemptive pods in each failure domain to trigger the autoscaler, allowing stateful workloads to scale up efficiently.

## Features

- Calculates the total number of preemptive pods needed across all failure domains based on the node capacity and preemptive pod resource requests.
- Visualizes the distribution of preemptive pods across failure domains.
- Customizable parameters for node capacity, preemptive pod resource requests, autoscaler scale-up threshold, and number of failure domains.

## Requirements

- Python 3
- Matplotlib (for visualization)
- Pipenv (for package management)

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/gabeduke/preemptive-pod-calculator.git
   cd your-repository-directory
   ```

2. **Setup the environment with `pipenv`:**

   If you haven't installed `pipenv`, install it globally with:

   ```
   pip install pipenv
   ```

   Then, create a `Pipfile` in your project directory and specify Python 3 as the required version:

   ```
   [requires]
   python_version = "3"
   ```

   Initialize the pipenv environment:

   ```
   pipenv --python 3
   pipenv install matplotlib
   ```

   This will create a `Pipfile` and `Pipfile.lock` and install `matplotlib` within the virtual environment.

## Usage

To use the script, you can simply run it with Python. By default, it uses predefined values for the calculation but you can customize these as needed:

```
pipenv run python preemptive_pod_calculator.py [OPTIONS]
```

### Options

- `--cpu` - Node CPU capacity (default: 16 cores)
- `--memory` - Node memory capacity in GB (default: 32 GB)
- `--pod_cpu` - Preemptive pod CPU request (default: 2 cores)
- `--pod_memory` - Preemptive pod memory request in GB (default: 6 GB)
- `--scale_up_threshold` - Autoscaler scale-up threshold (as a fraction of 1, default: 0.8)
- `--failure_domains` - Number of failure domains (default: 3)
- `--visualize` - Whether to visualize the distribution of preemptive pods (default: True)

### Example

Run the script with default values and visualize the output:

```
pipenv run python preemptive_pod_calculator.py
```

Customize the calculation:

```
pipenv run python preemptive_pod_calculator.py --cpu 32 --memory 64 --pod_cpu 1 --pod_memory 2 --scale_up_threshold 0.75 --failure_domains 4 --visualize
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.
