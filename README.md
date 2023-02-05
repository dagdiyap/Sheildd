# Data Poisoning Attacks Against Federated Learning Systems

Code for the ESORICS 2020 paper: Data Poisoning Attacks Against Federated Learning Systems

## Installation

1) Create a virtualenv (Python 3.7)
2) Install dependencies inside of virtualenv (```pip install -r requirements.pip```)
3) If you are planning on using the defense, you will need to install ```matplotlib```. This is not required for running experiments, and is not included in the requirements file

## Instructions for execution

Using this repository, you can replicate all results presented at ESORICS. We outline the steps required to execute different experiments below.

### Setup

Before you can run any experiments, you must complete some setup:

1) ```python3 generate_data_distribution.py``` This downloads the datasets, as well as generates a static distribution of the training and test data to provide consistency in experiments.
2) ```python3 generate_default_models.py``` This generates an instance of all of the models used in the paper, and saves them to disk.

### Experiments - Label Flipping Attack Feasibility

Running an attack: ```python3 label_flipping_attack.py```

### Experiments - Attack Timing in Label Flipping Attacks

Running an attack: ```python3 attack_timing.py```

### Experiments - Malicious Participant Availability

Running an attack: ```python3 malicious_participant_availability.py```

### Experiments - Defending Against Label Flipping Attacks

Running the defense: ```python3 defense.py```

### Experiment Hyperparameters

Recommended default hyperparameters for CIFAR10 (using the provided CNN):
- Batch size: 10
- LR: 0.01
- Number of epochs: 200
- Momentum: 0.5
- Scheduler step size: 50
- Scheduler gamma: 0.5
- Min_lr: 1e-10

Recommended default hyperparameters for Fashion-MNIST (using the provided CNN):
- Batch size: 4
- LR: 0.001
- Number of epochs: 200
- Momentum: 0.9
- Scheduler step size: 10
- Scheduler gamma: 0.1
- Min_lr: 1e-10

