from sklearn.linear_model import LinearRegression
import numpy as np


def calculate_insights(df):

    if len(df) == 0:

        return {
            "avg_ats": 0,
            "avg_match": 0,
            "best_ats": 0,
            "total": 0,
            "prediction": 0
        }

    avg_ats = round(
        df["ats_score"].mean(),
        2
    )

    avg_match = round(
        df["match_percentage"].mean(),
        2
    )

    best_ats = int(
        df["ats_score"].max()
    )

    total = len(df)

    prediction = avg_ats

    if len(df) > 2:

        X = np.arange(
            len(df)
        ).reshape(-1, 1)

        y = df["ats_score"]

        model = LinearRegression()

        model.fit(X, y)

        prediction = round(
            model.predict(
                [[len(df)]]
            )[0],
            2
        )

    return {
        "avg_ats": avg_ats,
        "avg_match": avg_match,
        "best_ats": best_ats,
        "total": total,
        "prediction": prediction
    }