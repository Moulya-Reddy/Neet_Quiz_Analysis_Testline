import json
from data_analysis import analyze_performance
from insights_generation import generate_insights, generate_recommendations, generate_student_persona
from visualisation import plot_topic_accuracy, plot_performance_over_time

def main():
    # Load data (current and historical)
    with open('/Users/ananthpalreddykandhala/Documents/neet_quiz_data/data/current_data.json') as f:
        current_data = json.load(f)
    
    with open('/Users/ananthpalreddykandhala/Documents/neet_quiz_data/data/historical_data.json') as f:
        historical_data = json.load(f)
    
    # Analyze current and historical data
    current_analysis, historical_analysis = analyze_performance(current_data, historical_data)
    
    # Generate insights and recommendations
    insights = generate_insights(current_analysis, historical_analysis)
    recommendations = generate_recommendations(current_analysis, historical_analysis)
    student_persona = generate_student_persona(current_analysis, historical_analysis)
    
    # Visualizations
    plot_topic_accuracy(current_analysis, historical_analysis)
    plot_performance_over_time(historical_analysis)
    
    # Output insights and recommendations
    print("Insights:", insights)
    print("Recommendations:", recommendations)
    print("Student Persona:", student_persona)

if __name__ == "__main__":
    main()
