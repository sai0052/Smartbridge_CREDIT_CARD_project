import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

plt.style.use("ggplot")

# -----------------------------
# 1. Approval Distribution
# -----------------------------
plt.figure(figsize=(6,4))
df["Approved"].value_counts().plot(kind="bar", color=["red","green"])
plt.title("Credit Card Approval Distribution")
plt.xlabel("Approved")
plt.ylabel("Count")
plt.xticks([0,1],["Rejected","Approved"], rotation=0)
plt.tight_layout()
plt.savefig("approval_distribution.png")
plt.show()


# -----------------------------
# 2. Credit Score Distribution
# -----------------------------
plt.figure(figsize=(6,4))
plt.hist(df["CreditScore"], bins=20)
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Customers")
plt.tight_layout()
plt.savefig("credit_score_distribution.png")
plt.show()


# -----------------------------
# 3. Income vs Debt
# -----------------------------
plt.figure(figsize=(6,5))
plt.scatter(df["Income"], df["Debt"], alpha=0.6)
plt.title("Income vs Existing Debt")
plt.xlabel("Annual Income")
plt.ylabel("Existing Debt")
plt.tight_layout()
plt.savefig("income_vs_debt.png")
plt.show()


# -----------------------------
# 4. Employment Status Count
# -----------------------------
plt.figure(figsize=(6,4))
df["EmploymentStatus"].value_counts().plot(kind="bar")
plt.title("Employment Status")
plt.xlabel("Status")
plt.ylabel("Customers")
plt.tight_layout()
plt.savefig("employment_status.png")
plt.show()


# -----------------------------
# 5. Approval by Previous Default
# -----------------------------
approval = pd.crosstab(df["PreviousDefault"], df["Approved"])

approval.plot(kind="bar", figsize=(6,4))
plt.title("Previous Default vs Approval")
plt.xlabel("Previous Default")
plt.ylabel("Count")
plt.legend(["Rejected","Approved"])
plt.tight_layout()
plt.savefig("default_vs_approval.png")
plt.show()

print("✅ All charts generated successfully.")