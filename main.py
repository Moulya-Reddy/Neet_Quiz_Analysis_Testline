import json
from data_analysis import analysing_performance
from insights_generation import generating_insights, generating_recommendations, generating_student_persona
from visualisation import plotting_topic_accuracy, plotting_performance_over_time

def main():
    # Load data (current and historical)
    with open('/Users/ananthpalreddykandhala/Documents/neet_quiz_data/data/current_data.json') as f:
        current_data_of_student = json.load(f)
    
    with open('/Users/ananthpalreddykandhala/Documents/neet_quiz_data/data/historical_data.json') as f:
        historical_data_of_student = json.load(f)
    
    # Analyze current and historical data
    current_analysis_of_student, historical_analysis_of_student = analysing_performance(current_data_of_student, historical_data_of_student)
    
    # Generate insights and recommendations
    insights_generated = generating_insights(current_analysis_of_student, historical_analysis_of_student)
    recommendations_generated = generate_recommendations(current_analysis_of_student, historical_analysis_of_student)
    student_persona_generated = generate_student_persona(current_analysis_of_student, historical_analysis_of_student)
    
    # Visualizations
    plotting_topic_accuracy(current_analysis_of_student, historical_analysis_of_student)
    plotting_performance_over_time(historical_analysis_of_student)
    
    # Output insights and recommendations
    print("Insights:", insights_generated)
    print("Recommendations:", recommendations_generated)
    print("Student Persona:", student_persona_generated)

if __name__ == "__main__":
    main()
