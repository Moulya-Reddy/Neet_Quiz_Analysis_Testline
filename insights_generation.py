def generating_insights(current_analysis_of_student, historical_analysis_of_student):
    current_accuracy = (current_analysis_of_student['correct_answers'] / current_analysis_of_student['total_questions']) * 100 if current_analysis_of_student['total_questions'] > 0 else 0
    topic_accuracies = {topic: (current_analysis_of_student['topics'][topic] / current_analysis_of_student['total_questions']) * 100 for topic in current_analysis_of_student['topics']}
    
    weak_topics = [topic for topic, accuracy in topic_accuracies.items() if accuracy < 50]
    improvement_trends = []  # Can be expanded with time-based improvements accordingly
    performance_gaps = [f"Focus on improving {topic}." for topic in weak_topics]
    
    insights_of_student = {
        'current_accuracy': current_accuracy,
        'topic_accuracies': topic_accuracies,
        'weak_topics': weak_topics,
        'improvement_trends': improvement_trends,
        'performance_gaps': performance_gaps
    }
    
    return insights_of_student

def generating_recommendations(current_analysis_of_student, historical_analysis_of_student):
    recommendations = []
    
    # Focusing on the weak topics
    for topic in current_analysis_of_student['topics']:
        if current_analysis_of_student['topics'][topic] == 0:
            recommendations.append(f"Focus on these weak topics: {topic}.")
    
    # Suggesting difficulty levels based on performance of the student 
    difficulty_levels = ['easy', 'medium', 'hard']
    for difficulty in difficulty_levels:
        recommendations.append(f"Try focusing on {difficulty} difficulty questions to improve accuracy.")
    
    # Suggesting question types based on accuracy
    question_types = ['MCQ', 'Assertion-Reasoning', 'Match the following']
    for q_type in question_types:
        recommendations.append(f"Practice more {q_type} questions to gain confidence.")
    
    return recommendations

def generating_student_persona(current_analysis_of_student, historical_analysis_of_student):
    total_quizzes = len(historical_analysis_of_student)
    correct_answers = sum([historical_analysis_of_student[q]['correct_answers'] for q in historical_analysis_of_student])
    
    accuracy = (correct_answers / (total_quizzes * 1.0)) * 100  # Assuming each quiz has 1 correct answer.
    
    if accuracy >= 90:
        persona = 'High Achiever'
    elif accuracy >= 70:
        persona = 'Steady Learner'
    elif accuracy >= 50:
        persona = 'Average Performer'
    else:
        persona = 'Needs Improvement'
    
    strengths = [key for key, value in current_analysis_of_student['topics'].items() if value > 0]
    weaknesses = [key for key, value in current_analysis_of_student['topics'].items() if value == 0]

    return {
        'type': persona,
        'strengths': strengths,
        'weaknesses': weaknesses
    }
