# Towards Optimal Sensor Placement for Travelling Agents in Two-Dimensional POMDPs
## Bachelor Project

*Refer to the paper for detailed information on the project.*

# OOP (Optimal Observability Problem)
This work provides a method that given a POMDP how should one change the POMDP's observation capabilities within a fixed budget such that its (minimal) expected reward remains below a given threshold.

# Motivation
Partially Observable Markov Decision Processes find applications in many fields of engineering and real-life scenarios due to their inherent ability to model decision making under uncertainty when the state of a system is not fully observable. POMDPs are especially useful in healthcare, where they can be applied to personalized healthcare systems where patient states are partially observable. They can help in decision-making processes for treatments and interventions by considering uncertain patient states and outcomes. Other applications include finance risk assessments or trading strategies, natural language processing, and supply chain management. Upon the rising interest regarding work surrounding the connection of Artificial Intelligence to MDPs over the most recent century, the field of reinforcement learning has now newfound applications in robotics and automata. Alongside this, interesting theoretical thought problems have arisen, one such is the novel Optimal Observability Problem.

The existing OOP solver developed in Alyzia et al., while optimal and deterministic, is very limited by the time complexity of the nature of the Optimal Observability Problem. Furthermore, it encounters restrictions when faced with some trivial solutions with low budgets, or non-evident and somewhat convoluted high budget solutions. The motivation behind this project is to determine if it is possible to analytically find ad-hoc solutions to specific configurations of the problem, determine if the solution is scalable, and contextualize the patterns that may arise. Another project goal is to reduce the time complexity and/or solve those problems for which the current Z3 solver is incapable of producing an output. Furthermore, a large part of the project time was dedicated to creating an interface to visualize and analyze the problem in a more effective way. One that hopefully can provide an incentive for future researchers to understand the problem in a more intuitive manner and provide a fast tool to explore problems and solutions.

# The research problem
Alyzia et al.'s Novel Optimal Observability Problem (OOP) and its variations are further developed in this work. Our objectives are to visualize the solver, improve its computational efficiency, and analyze emerging patterns. Additionally, we aim to scale the solution and formulate a conjecture based on our findings.

# Contributions
The project's contributions to the field are summarized as follows:

- Development of a visualizer for the tool described in Alyzia et al. for the Optimal Observability Problem (OOP), including variations such as the Sensor Selection Problem and encompassing all three models present in the original tool.
- Introduction of a heuristic approach to the OOP, aimed at improving the solver's running time complexity.
- Presentation of a novel approach for defining a utility function for the OOP.
- Exploration of pattern analysis on ad-hoc solutions to the OOP, to identify patterns between models, assess their scalability, and formulate a conjecture.
- Proposal of an optimization technique for pattern analysis using simulated annealing, which is extendable to future problems.

# Run the tool and server
Grant execution permissions for the quick launch (Linux / Macos):

```
chmod +x start.sh
```

Then run, 

```
./start.sh
```

# Perform pattern analysis
Run the notebook `Pattern Analysis.ipynb` to perform pattern analysis on the models.

To run the notebook, you need to have Jupyter installed. If you don't have it installed, you can install it using pip:

```
pip3 install jupyter
```

Then run the notebook using the following command:

```
jupyter notebook
```

Then go to the browser and open the notebook under "visualizer/notebooks/Pattern Analysis.ipynb".