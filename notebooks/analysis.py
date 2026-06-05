import os
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. Define file paths
# ------------------------------------------------------------

DATA_PATH = "../data/coded_scores.csv"
FIGURES_DIR = "../figures"

os.makedirs(FIGURES_DIR, exist_ok=True)


# ------------------------------------------------------------
# 2. Load coded score data
# ------------------------------------------------------------

scores = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")
print("Number of rows:", len(scores))
print("\nColumns:")
print(list(scores.columns))

print("\nAgent type counts:")
print(scores["agent_type"].value_counts())


# ------------------------------------------------------------
# 3. Basic data validation
# ------------------------------------------------------------

expected_rows = 22

if len(scores) != expected_rows:
    print(f"\nWarning: Expected {expected_rows} rows, but found {len(scores)} rows.")
else:
    print("\nRow count check passed: 22 responses found.")

required_columns = [
    "response_id",
    "prompt_id",
    "agent_type",
    "style_consistency",
    "instruction_following",
    "controllability",
    "empathy",
    "analytical_clarity",
    "rule_violation",
]

missing_columns = [col for col in required_columns if col not in scores.columns]

if missing_columns:
    print("\nWarning: Missing columns:")
    print(missing_columns)
else:
    print("Column check passed: all required columns found.")


# ------------------------------------------------------------
# 4. Descriptive statistics
# ------------------------------------------------------------

score_columns = [
    "style_consistency",
    "instruction_following",
    "controllability",
    "empathy",
    "analytical_clarity",
]

print("\nDescriptive statistics:")
print(scores[score_columns].describe())


# ------------------------------------------------------------
# 5. Mean scores by agent type
# ------------------------------------------------------------

mean_scores = scores.groupby("agent_type")[score_columns].mean()

print("\nMean scores by agent type:")
print(mean_scores)


# ------------------------------------------------------------
# 6. Figure 1: Average scores by agent type
# ------------------------------------------------------------

mean_scores.T.plot(kind="bar", figsize=(10, 6))

plt.title("Average Evaluation Scores by Agent Type")
plt.ylabel("Average Score")
plt.xlabel("Evaluation Dimension")
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 5.5)
plt.tight_layout()

figure_path = os.path.join(FIGURES_DIR, "average_scores_by_agent_type.png")
plt.savefig(figure_path, dpi=300)
plt.close()

print(f"\nSaved figure: {figure_path}")


# ------------------------------------------------------------
# 7. Figure 2: Average empathy by agent type
# ------------------------------------------------------------

empathy_scores = scores.groupby("agent_type")["empathy"].mean()

empathy_scores.plot(kind="bar", figsize=(6, 4))

plt.title("Average Empathy Score by Agent Type")
plt.ylabel("Average Empathy Score")
plt.xlabel("Agent Type")
plt.ylim(0, 5.5)
plt.tight_layout()

figure_path = os.path.join(FIGURES_DIR, "average_empathy_by_agent_type.png")
plt.savefig(figure_path, dpi=300)
plt.close()

print(f"Saved figure: {figure_path}")


# ------------------------------------------------------------
# 8. Figure 3: Average analytical clarity by agent type
# ------------------------------------------------------------

clarity_scores = scores.groupby("agent_type")["analytical_clarity"].mean()

clarity_scores.plot(kind="bar", figsize=(6, 4))

plt.title("Average Analytical Clarity by Agent Type")
plt.ylabel("Average Analytical Clarity Score")
plt.xlabel("Agent Type")
plt.ylim(0, 5.5)
plt.tight_layout()

figure_path = os.path.join(FIGURES_DIR, "average_analytical_clarity_by_agent_type.png")
plt.savefig(figure_path, dpi=300)
plt.close()

print(f"Saved figure: {figure_path}")


# ------------------------------------------------------------
# 9. Figure 4: Controllability scores across prompts
# ------------------------------------------------------------

controllability_table = scores.pivot(
    index="prompt_id",
    columns="agent_type",
    values="controllability",
)

controllability_table.plot(kind="bar", figsize=(10, 6))

plt.title("Controllability Scores Across Prompts")
plt.ylabel("Controllability Score")
plt.xlabel("Prompt ID")
plt.ylim(0, 5.5)
plt.xticks(rotation=45)
plt.tight_layout()

figure_path = os.path.join(FIGURES_DIR, "controllability_across_prompts.png")
plt.savefig(figure_path, dpi=300)
plt.close()

print(f"Saved figure: {figure_path}")

# ------------------------------------------------------------
# 10. Figure 5: Empathy vs Analytical Clarity
# ------------------------------------------------------------

comparison = mean_scores[["empathy", "analytical_clarity"]]

comparison.plot(kind="bar", figsize=(8, 5))

plt.title("Empathy and Analytical Clarity by Agent Type")
plt.ylabel("Average Score")
plt.xlabel("Agent Type")
plt.ylim(0, 5.5)
plt.xticks(rotation=0)
plt.tight_layout()

figure_path = os.path.join(FIGURES_DIR, "empathy_vs_analytical_clarity.png")
plt.savefig(figure_path, dpi=300)
plt.close()

print(f"Saved figure: {figure_path}")

# ------------------------------------------------------------
# 11. Preliminary findings
# ------------------------------------------------------------

print("\nPreliminary findings:")
print(
    """
1. Both agent profiles maintained high style consistency across the tested prompts.
2. The high-mechanical-intelligence agent showed high analytical clarity and low empathy scores.
3. The high-social-intelligence agent showed high empathy scores while maintaining moderate-to-high analytical clarity.
4. The P10 case is especially informative because the mechanical agent refused to shift into a more extroverted and supportive style, suggesting strong prompt-based style control.
5. These findings are exploratory because the dataset is small and the coding was conducted by one evaluator.
"""
)