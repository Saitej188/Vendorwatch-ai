import pandas as pd
from ml.insights import generate_insights


def generate_report(df: pd.DataFrame):

    insights = generate_insights(df)

    return {
        "summary": f"""
VendorWatch AI Market Report

Total Jobs: {insights.get('total_jobs', 0)}
Remote Ratio: {insights.get('remote_ratio', 0)}
Senior Ratio: {insights.get('senior_ratio', 0)}

Top Company: {list(insights.get('top_companies', {}).keys())[0] if insights.get('top_companies') else 'N/A'}
Top Skill: {list(insights.get('top_skills', {}).keys())[0] if insights.get('top_skills') else 'N/A'}
""",
        "raw": insights
    }