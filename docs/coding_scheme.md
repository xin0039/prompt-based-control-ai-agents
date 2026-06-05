# Coding Scheme

Each AI response was evaluated on a 1–5 scale across five dimensions. The purpose of this coding scheme is to assess whether AI agents can maintain distinct interaction styles while following explicit prompt-based output-control rules.

## 1. Style Consistency

This dimension measures whether the response matches the assigned agent profile.

1 = The response does not match the assigned profile.
2 = The response weakly matches the assigned profile.
3 = The response partially matches the assigned profile.
4 = The response mostly matches the assigned profile.
5 = The response strongly matches the assigned profile.

## 2. Instruction Following

This dimension measures whether the response follows the explicit output-control rules, including word limit, tone, and required structure.

1 = The response violates most output-control rules.
2 = The response follows only a few rules.
3 = The response follows some rules but misses important constraints.
4 = The response follows most rules with minor issues.
5 = The response fully follows the output-control rules.

## 3. Controllability

This dimension measures whether the agent behavior appears clearly shaped by prompt-based control.

1 = The response appears weakly controlled by the prompt.
2 = The response shows limited evidence of prompt-based control.
3 = The response is partially shaped by the prompt.
4 = The response is mostly shaped by the prompt rules.
5 = The response is clearly shaped by explicit prompt rules.

## 4. Empathy

This dimension measures emotional acknowledgement, supportive tone, and user-sensitive communication.

1 = No emotional acknowledgement.
2 = Minimal emotional sensitivity.
3 = Some emotional sensitivity.
4 = Clear emotional acknowledgement and supportive tone.
5 = Strong emotional awareness and supportive communication.

## 5. Analytical Clarity

This dimension measures logical structure, clarity, and task-oriented reasoning.

1 = Poor structure and unclear reasoning.
2 = Limited clarity and weak organization.
3 = Moderately clear structure and reasoning.
4 = Clear and mostly well-organized reasoning.
5 = Clear, logical, and well-organized reasoning.

## 6. Rule Violation

This variable records whether the response violates at least one major output-control rule.

0 = No major violation.
1 = At least one major violation, such as exceeding the word limit, giving the wrong number of suggestions, or using an inappropriate tone.

## Coding Notes

The high-mechanical-intelligence agent is expected to score higher in analytical clarity and lower in empathy.

The high-social-intelligence agent is expected to score higher in empathy and may show a more relational communication style.

A high score in style consistency does not mean the response is better overall. It only means the response matches the assigned agent profile.

A high controllability score means the response appears to follow the user-defined prompt rules in a clear and observable way.
