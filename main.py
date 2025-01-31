import json
from data_analysis import analysing_performance
from insights_generation import generating_insights, generating_recommendations, generating_student_persona
from visualisation import plotting_topic_accuracy, plotting_performance_over_time,plotting_accuracy_distribution

def main():
    # Loading the datasets (current and historical)
    with open('/Users/ananthpalreddykandhala/Documents/neet_quiz_data/data/current_data.json') as f:
        current_data_of_student = json.load(f)
    # current indicates the present performance of the student
    with open('/Users/ananthpalreddykandhala/Documents/neet_quiz_data/data/historical_data.json') as f:
        historical_data_of_student = json.load(f)
    # historical indicates the previous performance of the student
    
    # Analysing the datasets (current and historical data)
    current_analysis_of_student, historical_analysis_of_student = analysing_performance(current_data_of_student, historical_data_of_student)
    
    # Generating the  insights and recommendations of the student 
    insights_generated = generating_insights(current_analysis_of_student, historical_analysis_of_student)
    recommendations_generated = generating_recommendations(current_analysis_of_student, historical_analysis_of_student)
    student_persona_generated = generating_student_persona(current_analysis_of_student, historical_analysis_of_student)
    
    # Visualisation of the performance of student 
    plotting_topic_accuracy(current_analysis_of_student, historical_analysis_of_student)
    plotting_performance_over_time(historical_analysis_of_student)
    plotting_accuracy_distribution(current_analysis_of_student, historical_analysis_of_student)
    
    # Printing the output of insights and recommendations
    print("Insights:", insights_generated)
    print("Recommendations:", recommendations_generated)
    print("Student Persona:", student_persona_generated)
    
# Executing the main() function
if __name__ == "__main__":
    main()
