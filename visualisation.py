import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots (Seaborn's default white grid)
sns.set(style="whitegrid")

def plot_topic_accuracy(current_analysis, historical_analysis):
    """
    Plot topic-wise accuracy of the current quiz submission.
    :param current_analysis: Current quiz analysis data (accuracies by topic)
    :param historical_analysis: Historical quiz analysis data (for future comparison if needed)
    """
    # Extract topics and accuracy data
    topics = list(current_analysis['topics'].keys())
    accuracies = [current_analysis['topics'][topic] / current_analysis['total_questions'] * 100 for topic in topics]
    
    # Create a bar plot for topic-wise accuracy
    plt.figure(figsize=(12, 6))
    sns.barplot(x=topics, y=accuracies, palette='viridis')
    
    # Title and labels with proper fonts
    plt.title('Topic-wise Accuracy', fontsize=16, fontweight='bold')
    plt.xlabel('Topics', fontsize=14)
    plt.ylabel('Accuracy (%)', fontsize=14)
    plt.xticks(rotation=45, ha="right")  # Rotate topic names for readability
    plt.ylim(0, 100)  # Accuracy range from 0 to 100%
    
    # Show grid lines for easier visual comparison
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()  # Ensure no labels get cut off
    plt.show()

def plot_performance_over_time(historical_analysis):
    """
    Plot performance over time (accuracy per quiz).
    :param historical_analysis: Historical quiz performance data
    """
    # Extract quizzes and accuracy data over time
    quizzes = list(historical_analysis.keys())
    accuracies = [
        historical_analysis[q]['correct_answers'] / historical_analysis[q]['total_questions'] * 100
        for q in quizzes
    ]
    
    # If there is no data, print message and exit
    if not accuracies:
        print("No historical data available to plot.")
        return

    # Create a line plot for performance over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=quizzes, y=accuracies, marker='o', color='b', linewidth=2, markersize=8)
    
    # Title and labels with proper fonts
    plt.title('Performance Over Time', fontsize=16, fontweight='bold')
    plt.xlabel('Quizzes', fontsize=14)
    plt.ylabel('Accuracy (%)', fontsize=14)
    plt.xticks(rotation=45, ha="right")  # Rotate quiz names for readability
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Show plot with tight layout
    plt.tight_layout()
    plt.show()

def plot_accuracy_distribution(current_analysis, historical_analysis):
    """
    Plot the distribution of accuracies for current and historical quizzes.
    :param current_analysis: Current quiz analysis data
    :param historical_analysis: Historical quiz analysis data
    """
    # Calculate current quiz accuracy
    current_accuracy = current_analysis['correct_answers'] / current_analysis['total_questions'] * 100
    
    # Extract historical accuracies
    historical_accuracies = [
        historical_analysis[q]['correct_answers'] / historical_analysis[q]['total_questions'] * 100
        for q in historical_analysis
    ]
    
    # If there's no historical data, show a message and exit
    if not historical_accuracies:
        print("No historical data available for accuracy distribution.")
        return
    
    # Create a histogram and KDE (Kernel Density Estimate) plot for accuracy distribution
    plt.figure(figsize=(12, 6))
    sns.histplot(historical_accuracies, kde=True, color='orange', label='Historical Performance', bins=10, alpha=0.6)
    sns.histplot([current_accuracy], kde=True, color='blue', label='Current Performance', bins=10, alpha=1)
    
    # Title and labels with proper fonts
    plt.title('Accuracy Distribution: Current vs Historical', fontsize=16, fontweight='bold')
    plt.xlabel('Accuracy (%)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend(title="Performance", loc='upper right')
    
    # Show plot with tight layout
    plt.tight_layout()
    plt.show()

