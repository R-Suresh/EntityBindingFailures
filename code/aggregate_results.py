import argparse
import os
import pandas as pd

METRICS = [
    "task_success",
    "safe_success",
    "wrong_tool",
    "wrong_entity",
    "entity_correct",
    "ambiguity_detected",
    "over_clarification",
    "risk_weighted_wrong_entity",
]


def summarize(df, group_cols, out_path):
    summary = df.groupby(group_cols)[METRICS].mean().reset_index()
    summary.to_csv(out_path, index=False)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", default="tables")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    df = pd.read_csv(args.input)

    by_method = summarize(df, ["method"], f"{args.outdir}/summary_by_method.csv")
    summarize(df, ["model", "method"], f"{args.outdir}/summary_by_model_method.csv")
    summarize(df, ["ambiguity", "method"], f"{args.outdir}/summary_by_ambiguity_method.csv")
    summarize(df, ["risk", "method"], f"{args.outdir}/summary_by_risk_method.csv")

    print(by_method.to_string(index=False))


if __name__ == "__main__":
    main()
