def define_student_persona(historical_analysis):
    """
    Defines a student persona based on historical performance.
    """
    persona = {
        'type': '',
        'strengths': [],
        'weaknesses': []
    }

    # Determine persona type based on overall accuracy
    total_questions = sum(stats['total_questions'] for stats in historical_analysis.values())
    total_correct = sum(stats['correct_answers'] for stats in historical_analysis.values())
    accuracy = (total_correct / total_questions) * 100 if total_questions > 0 else 0

    if accuracy > 80:
        persona['type'] = 'High Achiever'
    elif accuracy > 60:
        persona['type'] = 'Steady Learner'
    else:
        persona['type'] = 'Needs Improvement'

    # Identify strengths and weaknesses
    for topic, stats in historical_analysis.items():
        topic_accuracy = (stats['correct_answers'] / stats['total_questions']) * 100 if stats['total_questions'] > 0 else 0
        if topic_accuracy > 80:
            persona['strengths'].append(topic)
        elif topic_accuracy < 50:
            persona['weaknesses'].append(topic)

    return persona
