# Inter IIT Tech Meet 11 GradCapital 

## Problem Statement

#### To create a novel deeptech startup that tackles real world problems from a new technical perspective.

## Solution 

### Our solution is a product-based software application that protects companies from ML attacks aimed at stealing their models, data or changing the logic of the ML system, by
### &emsp; &emsp; ● Scoring models based on their vulnerability to attacks
### &emsp; &emsp; ● Recommending defense mechanism against the attacks
### &emsp; &emsp; ● Implementing the defense mechanisms for the organization

###

# Approach

#### 1) Learn Differnt ART attacks from resarch papers and IBM art tools

#### 2) Fedrated Learning was chosen to preform the attacks for this project 

#### 3) Trained custom image recognition models to preform to be used in the project 

#### 4) Implemnted code to courrupt a random subset of given dataset 

#### 5) Created scripts to messure the impact of the attacks 

<br/>




## Working

1) Create a virtualenv (Python 3.7)
2) Install dependencies inside of virtualenv (```pip install -r requirements.pip```)
3) If you are planning on using the defense, you will need to install ```matplotlib```. This is not required for running experiments, and is not included in the requirements file

### Setup

Before you can run any experiments, you must complete some setup:

1) ```python generate_data_distribution.py``` This downloads the datasets, as well as generates a static distribution of the training and test data to provide consistency in experiments.
2) ```python generate_default_models.py``` This generates an instance of all of the models used in the paper, and saves them to disk.

### Label Flipping Attack Feasibility

Running an attack: ```python label_flipping_attack.py```

### Attack Timing in Label Flipping Attacks

Running an attack: ```python attack_timing.py```

### Malicious Participant Availability

Running an attack: ```python malicious_participant_availability.py```

### Defending Against Label Flipping Attacks

Running the defense: ```python defense.py```

### Hyperparameters

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

# Achivement

### The Project Recived Silver Medal 

# Result

### A platform was successfully presented software application that protects companies from ML attacks, by scoring thier models and also locating its most weekest spot, leading to Silver Medal in Grad Capital PS-4 of Inter IIT Tech Meet 11 helping Institute to bag an overall Silver Medal among the best tecnical institues of India.

## Link to project proposal : https://drive.google.com/file/d/1-isEPgu8q5lQzDZtPQ_hxOea3DDIWPO5/view?usp=sharing 
