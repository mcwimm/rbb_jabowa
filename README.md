# Reusable Building Block
## 1. The name of the RBB [_*_]

Jabowa plant growth

## 2. The author(s) names [_*_] & affiliation(s)

Marie-Christin Wimmler<sup>1)</sup>, 
Uta Berger<sup>1)</sup>

<sup>1)</sup> Institute of Forest Growth and Computer Sciences, Technische Universität Dresden, Germany

## 3. Keywords [_*_]

Additional terms that suggest what the topic of the RBB is about. They may also include words and phrases that are closely related to your topic and help interested modellers find your RBB easily. For example, if the RBB is about random walk, use phrases like animal movement, animal behaviour, food search, etc.

## 4.	The purpose of the RBB [_*_]

A narrative description of what mechanism or process the RBB is representing and in what environments or systems. What kind of questions has the RBB already been used to address and what other questions could it be relevant to? Preferably include references to relevant publications.

## 5.	Concepts

A description of the theoretical concepts the RBB is building on, e.g., a specific standard description of a certain behaviour such as symmetric competition or the informed user. This helps to classify the building block and to find a link to others that could be grouped in one category.

## 6.	An overview of the RBB and its use [_*_]

This section follows the rationale of the Overview part of the ODD protocol (see supplement S1 of Grimm et al. 2020). RBBs are typically relatively short procedures that describe a certain process affecting a certain entity, e.g., an agent. For example, a plant uses water, or competes with other plants, a buyer buys something, or a farmer is affecting the way other farmers use their land. Note that the calling and affecting agents can be the same. The following information should thus be provided:

### Entity [_*_]:

- What entity, or entities, are running the submodel or are involved (e.g., by providing 
information)? What state variables does the entity need to have to run this RBB?
- Which variables describe the entities?

### Context, model parameters & patterns: 

- What global variables (e.g., parameters characterising the environment) or data structures (e.g., a gridded spatial environment) does the use of the RBB require?
- Does the RBB directly affect global variables or data structures?
- What parameters does the RBB use? Preferably a table including parameter name, meaning, default value, range, and unit (if applicable).

### Patterns and data to determine parameters and/or to claim that the RBB is realistic enough for its purpose:

- Which of the variables (or parameters) can be set independent of the model/RBB, using direct measurement, other models (e.g., regression), etc.? 
- Which variables or parameters can only be estimated within the context of the model or require calibration?
- Which data or patterns can be used for calibration?
- Are pre-existing datasets available to users already exist (references)?

###	Interface - A list of all inputs and outputs of the RBB [_*_]

A table which specifies:
- Which input variables that the RBB requires from an external, calling entity and in which units?
- What specific outputs does it produce and how does this update the state variables of the calling entity?

###	Scales [_*_]:

On which spatio-temporal scales is the RBB valid, i.e., what are the possible range of resolutions and extents of the spatial and temporal scale?

## 7.	Pseudocode, a Flowchart or other type of graphical representation [_*_]

We consider this as semi-optional information since the suitability of each tool strongly depends on the complexity of the RBB. The author should ensure, however, that a reader understands what the RBB code is doing and in which sequence.

## 8.	The program code [_*_]

- A well commented code. [_*_] 
- Information on the programming language, operation system, development environments incl. any required software package or library, version etc.  [_*_]. 
- If possible, the code should be provided for different programming languages. If an author contributes their RBB in one programming language only, it could be an option that other authors provide a new implementation in a different programming language or environment. Thus, this list could be broadened over time.

## 9.	Example analyses of a simulation output, test cases and benchmarks [_*_]

Results obtained with the example implementation providing insights into how - under different settings - the RBB performs, including extreme scenarios. For a linear output at least two test cases should be provided, for a curved one as many as required to capture the behaviour of the RBB over the full range of input values. Benchmarks should provide outputs for standardised scenarios. They are the base for evaluating re-implementations.

## 10.	Version control [_*_]

A version control is already included if GitHub is used. If the RBB is provided via a different platform, an individual version control would help to document the history. At least it should be provided:
- Publish Date 
- Last Updated

## 11.	Status info

- Peer Review: yes/no. In case of a double open reviewing process, the name(s) of the reviewer(s) could be provided. This would increase the transparency of the process and acknowledge the effort of the reviewer for the ABM community. 
- Licence (if relevant): For example, GNU Lesser General Public Licence, General Public License (GPL) etc.

## 12.	Citation of the RBB

Any information on how the RBB should be referenced when reused. If the RBB is already tested and received a DOI, this is the place to find it.

## 13.	Example implementation of the RBB to demonstrate its use

It should be a demonstration program specifically written for the purpose of demonstrating the RBB in action with minimal superfluous content (like the code examples provided in the NetLogo library). It must be in a format that is readable by compilers or development environments commonly used by agent-based modellers (like NetLogo, GAMA etc.). Complex model structures should be avoided to reduce the risk of obsolescence over time and to prevent the actual mechanics of the RBB being obscured by unimportant model details. The following information should be provided:

- An executable demonstration program (including its code) that demonstrates how the RBB is working and allows users to play with its inputs and parameters.

## 14.	Use history

What is the history of the RBB? Is it entirely new or based on earlier submodels, or an implementation of an existing submodel? Has the RBB, or its predecessors, been used in literature? Reference list of publications, where the RBB was successfully used.

## 15.	A manual and/or tutorial, in particular for more complex  RBBs

Optional because of the effort, but it would be worthwhile particularly if the RBB is complex.

## 16.	Relationship to other RBBs

Sometimes an RBB belongs to a family of others. For example:
- The Field-Of-Neighbourhood (FON), which describes competition or facilitation among 
neighbouring plants, is an extension of the Zone-of-Influence (ZOI).
- The perfectly-rational optimizer (PRO) serves as a NULL model for the Theory of Planned Behaviour (TPB).

## 17.	References 

Any external reference (not included in bullet point 11) if required.
