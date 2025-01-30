def create_recommendations(insights):
    """
    Creates actionable recommendations based on insights.
    """
    recommendations = []

    # Recommendations for weak topics
    if insights['weak_topics']:
        recommendations.append(f"Focus on these weak topics: {', '.join(insights['weak_topics'])}.")

    # Recommendations for improvement trends
    if insights['improvement_trends']:
        recommendations.append(insights['improvement_trends'][0])

    # Recommendations for performance gaps
    if insights['performance_gaps']:
        recommendations.append(insights['performance_gaps'][0])

    return recommendations

if __name__ == "__main__":
    from insights_generation import generate_insights
    from data_analysis import analyze_performance, load_data
    current_data, historical_data = load_data()
    if current_data and historical_data:
        current_analysis, historical_analysis = analyze_performance(current_data, historical_data)
        insights = generate_insights(current_analysis, historical_analysis)
        recommendations = create_recommendations(insights)
        print("Recommendations:", recommendations)
