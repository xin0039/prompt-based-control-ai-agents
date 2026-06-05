# Evaluating Prompt-Based Control in AI Agents

## Project Overview

This repository presents a small-scale AI agent functionality testing project. The project evaluates whether two differently designed AI agents can maintain distinct interaction styles across repeated user prompts while following prompt-based control rules.

The two agent profiles are:

1. **High-mechanical-intelligence agent**: task-oriented, structured, concise, procedural, and low-emotion.
2. **High-social-intelligence agent**: empathetic, supportive, emotionally aware, adaptive, and human-centred.

The project is designed as a personal research portfolio related to **collaborative AI**, **human–AI interaction**, **adaptive AI behavior**, and **prompt-based control**.

## Research Question

Can AI agents maintain distinct interaction styles while following prompt-based control rules across repeated task and interpersonal contexts?

## Motivation

As AI agents are increasingly used in decision support, education, travel planning, academic support, and interpersonal communication tasks, it is important to understand whether their behavior can be reliably shaped by user-defined prompts.

This project explores prompt-based control as a lightweight mechanism for shaping AI-agent behavior. It focuses on whether different agent profiles can remain consistent across neutral, emotional, practical, and multi-turn interaction tasks.

## Agent Profiles

### High-Mechanical-Intelligence Agent

The mechanical agent was designed to demonstrate:

* Accuracy
* Efficiency
* Structured reasoning
* Procedural clarity
* Task completion
* Low emotional expression
* Neutral and direct communication

When the user expresses stress, frustration, uncertainty, or concern, the mechanical agent is instructed to avoid emotional reassurance and instead translate the user’s concern into a practical issue, risk, decision problem, or action plan.

### High-Social-Intelligence Agent

The social agent was designed based on the Big Five Personality framework, with emphasis on:

* High openness
* High conscientiousness
* Moderately high extraversion
* High agreeableness
* Low neuroticism / high emotional stability

The social agent is instructed to respond with empathy, warmth, emotional awareness, interpersonal adaptability, and supportive task completion.

## Dataset

The dataset contains 11 user prompts and 22 AI responses:

```text
11 user prompts × 2 agent profiles = 22 responses
```

The prompts cover different task contexts, including:

* Travel planning
* Laptop decision-making
* Research proposal feedback
* Delayed delivery problem-solving
* Teamwork communication
* Budget planning
* Solo travel safety anxiety
* Request for more supportive communication
* Pre-departure checklist generation

The raw outputs include:

* Full conversation records in `data/raw_outputs/agent_conversation_outputs.docx`
* Long-form PDF outputs for Kyoto and Milan itinerary tasks
* Structured response summaries in `data/responses.csv`
* Manually coded evaluation scores in `data/coded_scores.csv`

## Repository Structure

```text
prompt-based-control-ai-agents/
├── README.md
├── data/
│   ├── prompts.csv
│   ├── responses.csv
│   ├── coded_scores.csv
│   └── raw_outputs/
│       ├── agent_conversation_outputs.docx
│       ├── P01_mechanical_kyoto.pdf
│       ├── P01_social_kyoto.pdf
│       ├── P06_mechanical_milan.pdf
│       └── P06_social_milan.pdf
├── docs/
│   └── coding_scheme.md
├── figures/
│   ├── average_scores_by_agent_type.png
│   ├── average_empathy_by_agent_type.png
│   ├── average_analytical_clarity_by_agent_type.png
│   ├── controllability_across_prompts.png
│   └── empathy_vs_analytical_clarity.png
└── notebooks/
    └── analysis.py
```

## Evaluation Dimensions

Each response was manually coded using the following dimensions:

| Dimension             | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| Style consistency     | Whether the response matched the assigned agent profile                   |
| Instruction following | Whether the response followed the prompt-based task rules                 |
| Controllability       | Whether the agent behavior appeared shaped by the prompt                  |
| Empathy               | Whether the response showed emotional acknowledgement and supportive tone |
| Analytical clarity    | Whether the response showed clear structure and task-oriented reasoning   |
| Rule violation        | Whether the response clearly violated assigned rules                      |

Scores were assigned on a 1–5 scale, except for rule violation, which was coded as 0 or 1.

## Analysis

The analysis was conducted using Python. The script `notebooks/analysis.py` performs the following steps:

1. Loads the coded response scores from `data/coded_scores.csv`
2. Checks the dataset structure and row count
3. Computes descriptive statistics
4. Compares average scores between the two agent profiles
5. Generates visualizations and saves them to the `figures/` folder

The analysis uses:

* `pandas` for data loading and summary statistics
* `matplotlib` for visualization

## Preliminary Findings

The descriptive analysis suggests that both agent profiles maintained high style consistency across the tested prompts.

The high-mechanical-intelligence agent showed higher analytical clarity and lower empathy scores. This aligns with its intended design as a structured, procedural, and low-emotion agent.

The high-social-intelligence agent showed substantially higher empathy scores while maintaining moderate-to-high analytical clarity. This suggests that the social agent was able to combine emotional acknowledgement with practical task support.

The P10 case is especially informative. When the user explicitly requested the mechanical agent to become more extroverted and supportive, the mechanical agent refused to shift away from its assigned style. This suggests that strict prompt-based control may preserve agent behavior even when the user requests a different interaction style.

Overall, the results suggest that prompt-based control can shape differentiated AI-agent interaction styles. However, the findings should be interpreted as exploratory.

## Limitations

This project is a small-scale exploratory functionality test, not a formal experimental study.

The main limitations are:

* The dataset includes only 22 responses.
* The coding was conducted by one evaluator.
* No human participants were involved.
* The scoring is manually assigned and therefore subjective.
* The results should not be generalized without larger-scale testing and multiple coders.

Future work could expand the dataset, involve multiple evaluators, test more agent profiles, and examine user perceptions of trust, control, usefulness, and decision confidence.

## Relevance

This project is relevant to research on:

* Collaborative AI
* Human–AI interaction
* Adaptive AI behavior
* Prompt-based control
* User modelling
* AI-agent evaluation
* Trust and controllability in AI systems

It demonstrates a small-scale workflow for transforming AI-agent interaction data into a structured dataset, applying a coding scheme, conducting Python-based analysis, and visualizing behavioral differences between agent profiles.
