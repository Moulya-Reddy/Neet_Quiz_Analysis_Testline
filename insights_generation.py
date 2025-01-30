def generate_insights(current_analysis, historical_analysis):
    current_accuracy = (current_analysis['correct_answers'] / current_analysis['total_questions']) * 100 if current_analysis['total_questions'] > 0 else 0
    topic_accuracies = {topic: (current_analysis['topics'][topic] / current_analysis['total_questions']) * 100 for topic in current_analysis['topics']}
    
    weak_topics = [topic for topic, accuracy in topic_accuracies.items() if accuracy < 50]
    improvement_trends = []  # Could be expanded with time-based improvements
    performance_gaps = [f"Focus on improving {topic}." for topic in weak_topics]
    
    insights = {
        'current_accuracy': current_accuracy,
        'topic_accuracies': topic_accuracies,
        'weak_topics': weak_topics,
        'improvement_trends': improvement_trends,
        'performance_gaps': performance_gaps
    }
    
    return insights

def generate_recommendations(current_analysis, historical_analysis):
    recommendations = []
    
    # Focus on weak topics
    for topic in current_analysis['topics']:
        if current_analysis['topics'][topic] == 0:
            recommendations.append(f"Focus on these weak topics: {topic}.")
    
    # Suggest difficulty levels based on performance
    difficulty_levels = ['easy', 'medium', 'hard']
    for difficulty in difficulty_levels:
        recommendations.append(f"Try focusing on {difficulty} difficulty questions to improve accuracy.")
    
    # Suggest question types based on accuracy
    question_types = ['MCQ', 'Assertion-Reasoning', 'Match the following']
    for q_type in question_types:
        recommendations.append(f"Practice more {q_type} questions to gain confidence.")
    
    return recommendations

def generate_student_persona(current_analysis, historical_analysis):
    total_quizzes = len(historical_analysis)
    correct_answers = sum([historical_analysis[q]['correct_answers'] for q in historical_analysis])
    
    accuracy = (correct_answers / (total_quizzes * 1.0)) * 100  # Assuming each quiz has 1 correct answer.
    
    if accuracy >= 90:
        persona = 'High Achiever'
    elif accuracy >= 70:
        persona = 'Steady Learner'
    elif accuracy >= 50:
        persona = 'Average Performer'
    else:
        persona = 'Needs Improvement'
    
    strengths = [key for key, value in current_analysis['topics'].items() if value > 0]
    weaknesses = [key for key, value in current_analysis['topics'].items() if value == 0]

    return {
        'type': persona,
        'strengths': strengths,
        'weaknesses': weaknesses
    }
