import json
from collections import defaultdict


def analyze_performance(current_data, historical_data):
    # Initialize current analysis results
    current_analysis = {
        'total_questions': len(current_data['questions']),
        'correct_answers': sum(
            1 for i, q in enumerate(current_data['questions']) if q['correct_option'] == current_data['response_map'].get(str(q['id']), "")
        ),
        'topics': defaultdict(int),
        'difficulty_levels': defaultdict(int)
    }
    
    # Populate topic and difficulty level analysis
    for q in current_data['questions']:
        current_analysis['topics'][q['topic']] += 1
        current_analysis['difficulty_levels']['unknown'] += 1  # Assuming unknown for simplicity
    
    # Initialize historical analysis results
    historical_analysis = {}
    for quiz_id, quiz_data in historical_data.items():
        historical_analysis[quiz_id] = {
            'total_questions': len(quiz_data['questions']),
            'correct_answers': sum(
                1 for q in quiz_data['questions'] if q['correct_option'] == quiz_data['response_map'].get(str(q['id']), "")
            )
        }
    
    return current_analysis, historical_analysis

