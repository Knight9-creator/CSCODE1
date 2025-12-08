import pandas as pd

CSV_FILE = "StudyHabits.csv"


def load_data(filename=CSV_FILE):
    df = pd.read_csv(filename)
    numeric_cols = ["GradeLevel", "StudyHours", "SleepHours", "TestScore"]
    for col in numeric_cols:
        t0 = col
        df[t0] = pd.to_numeric(df[t0], errors="coerce")
    df = df.dropna(subset=["TestScore"])
    return df


def show_overview(df):
    print("=== FIRST 5 ROWS ===")
    print(df.head())
    print("=== COLUMNS ===")
    t1 = [df.columns]
    print(t1)
    print("=== BASIC STATS (StudyHours, SleepHours, TestScore) ===")
    t2 = df[["StudyHours", "SleepHours", "TestScore"]].describe()
    print(t2)
    


def average_test_score(df):
    return df["TestScore"].mean()


def study_hours_by_grade(df):
    return (
        df.groupby("GradeLevel")["StudyHours"]
        .mean()
        .reset_index(name="AvgStudyHours")
        .sort_values(by="GradeLevel")
    )


def top_students(df, n=5, min_study_hours=5.0):
    filtered = df[df["StudyHours"] >= min_study_hours]
    return filtered.sort_values(by="TestScore", ascending=False).head(n)


def sleepy_but_strong(df, min_sleep=7.5, min_score=85):
    mask = (df["SleepHours"] >= min_sleep) & (df["TestScore"] >= min_score)
    return df[mask].sort_values(by="TestScore", ascending=False)


def high_sleep_low_study(df):
    msk = (df["SleepHours"] >= 8.0) & (df["StudyHours"] < 4.0)
    return df[msk].sort_values(by="TestScore", ascending=False)


def main():
    df = load_data()
    show_overview(df)

    print("=== OVERALL AVERAGE TEST SCORE ===")
    print(average_test_score(df))
    

    print("=== AVERAGE STUDY HOURS BY GRADE LEVEL ===")
    print(study_hours_by_grade(df))
    

    print("=== TOP 5 STUDENTS (STUDY >= 5 HOURS/WEEK) ===")
    print(top_students(df, n=5, min_study_hours=5.0))
    

    print("=== WELL-RESTED HIGH SCORERS (SLEEP >= 7.5, SCORE >= 85) ===")
    print(sleepy_but_strong(df, min_sleep=7.5, min_score=85))
    


    print("=== HIGH SLEEP LOW STUDY (SLEEP >= 8.0 , STUDY < 4.0) ===")
    print(high_sleep_low_study(df))
    


if __name__ == "__main__":
    main()
