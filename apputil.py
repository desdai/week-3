import seaborn as sns
import pandas as pd


# update/add code below ...
def fib(n: int) -> int:
    """Return the nth Fibonacci number using recursion.

    Args:
        n (int): The index of the Fibonacci sequence (0-based).

    Returns:
        int: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# def fib(n: int) -> int:
#     """Return the nth Fibonacci number using iteration.

#     Args:
#         n (int): The index of the Fibonacci sequence (0-based).

#     Returns:
#         int: The nth Fibonacci number.
#     """
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

def to_binary(n: int) -> str:
    """Convert a non-negative integer to its binary representation using recursion.

    Args:
        n (int): The integer to convert.

    Returns:
        str: Binary representation of n.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)

# def to_binary(n: int) -> str:
#     """Convert a non-negative integer to its binary representation iteratively.

#     Args:
#         n (int): The integer to convert.

#     Returns:
#         str: Binary representation of n.
#     """
#     if n < 0:
#         raise ValueError("Input must be a non-negative integer.")
#     if n == 0:
#         return "0"

#     binary_digits = []
#     while n > 0:
#         binary_digits.append(str(n % 2))
#         n //= 2

#     # Reverse the list since we build it backwards
#     return "".join(reversed(binary_digits))

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

# print(df_bellevue.head())
# print(df_bellevue.gender.value_counts())

def task_1():
    """Return list of column names sorted by ascending missing values."""
    # Clean gender column (normalize to upper case, fix 'w' -> 'F')
    df = df_bellevue.copy()
    df["gender"] = df["gender"].astype(str).str.strip().str.upper()
    df["gender"] = df["gender"].replace({"W": "F"})

    missing_counts = df.isna().sum()
    return missing_counts.sort_values().index.tolist()

def task_2():
    """Return DataFrame with year and total admissions per year."""
    df = df_bellevue.copy()
    df["year"] = pd.to_datetime(df["date_in"], errors="coerce").dt.year

    admissions = (
        df.dropna(subset=["year"])
        .groupby("year")
        .size()
        .reset_index(name="total_admissions")
        .astype({"year": "int"})
        .sort_values("year")
    )
    return admissions


def task_3():
    """Return Series with average age by gender, using M: male and F: female."""
    df = df_bellevue.copy()

    # Normalize
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()

    # Map valid values only
    mapping = {"m": "M", "w": "F"}
    df["gender"] = df["gender"].map(mapping)

    # Coerce age to numeric
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    return df.groupby("gender")["age"].mean()


def task_4():
    """Return list of top 5 most common professions."""
    df = df_bellevue.copy()
    professions = (
        df["profession"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace({"": pd.NA, "nan": pd.NA})
    )
    return professions.value_counts().head(5).index.tolist()

print("Task 1:", task_1())

print("Task 2:\n", task_2())

print("Task 3:\n", task_3())

print("Task 4:", task_4())
