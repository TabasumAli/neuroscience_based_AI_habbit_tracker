import plotly.express as px
import pandas as pd

def plot_habits(logs):
    if not logs:
        return px.bar(title="No Data Available")

    data = [(log.habit.habit_name, log.date, log.status, log.habit.streak) for log in logs]
    df = pd.DataFrame(data, columns=["Habit", "Date", "Status", "Streak"])
    df["Date"] = pd.to_datetime(df["Date"])

    # Aggregate to count occurrences per date and habit
    agg_df = df.groupby(["Date", "Habit", "Status"]).size().reset_index(name="Count")

    fig = px.bar(
        agg_df,
        x="Date",
        y="Count",
        color="Status",
        barmode="stack",
        title="Habit Completion Over Time",
        labels={"Count": "Number of Logs", "Date": "Date"},
        color_discrete_map={"Done": "#2ecc71", "Skip": "#e74c3c"},
        text_auto=True
    )
    fig.update_layout(xaxis=dict(tickangle=45))

    # Add streak annotations for the latest date
    latest_date = df["Date"].max()
    latest_logs = df[df["Date"] == latest_date]
    for _, row in latest_logs.iterrows():
        fig.add_annotation(
            x=row["Date"],
            y=agg_df[agg_df["Date"] == latest_date]["Count"].sum() + 0.5,
            text=f"Streak: {row['Streak']}",
            showarrow=False,
            font=dict(size=10, color="black"),
            xshift=10
        )
    return fig