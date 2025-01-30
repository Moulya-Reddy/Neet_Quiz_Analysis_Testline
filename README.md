#Student Quiz Performance Analysis

This project analyzes a student’s performance in quizzes taken on the **Testline.in** platform. It evaluates the student’s accuracy, identifies strengths and weaknesses, and provides actionable recommendations for improvement. The project uses quiz data extracted from the Testline.in website and processes it using Python scripts.

**Project Overview**

The project consists of four Python scripts that work together to analyze and visualize the student’s quiz performance:

1. `data_analysis.py`: Loads and processes the quiz data to calculate accuracy, topic-wise performance, and difficulty-level performance.
2. `insights_generation.py`: Generates insights based on the analyzed data, such as weak topics and improvement trends.
3. `visualisation.py`: Creates visual representations (e.g., graphs and charts) of the student’s performance.
4. `main.py`: The main script that runs the analysis, generates insights, and displays the results.

**How to Use**

Step 1: Extract Quiz Data
1. Visit the "Testline.in" website using Google Chrome.
2. Open the "Developer Tools" by pressing `Command + Option + I` (on Mac) or `Ctrl + Shift + I` (on Windows).
3. Go to the "Network" tab and select "Fetch/XHR".
4. Take a quiz on the platform.
5. Copy the quiz response from the Developer Tools and save it into two JSON files:
   - `current_data.json`: Contains the latest quiz details and the student’s responses.
   - `historical_data.json`: Contains the student’s performance data from past quizzes.

Step 2: Run the Scripts
1. Clone or download this repository to your local machine.
2. Install the required Python libraries by running:
3. Run the `main.py` script:
   (python3 main.py)

Step 3: View Results
The script will display the following:
  - Current Quiz Analysis: Accuracy, topic-wise performance, and difficulty-level performance.
  - Historical Quiz Analysis: Trends in the student’s performance over time.
  - Insights: Weak topics, improvement trends, and performance gaps.
  - Recommendations: Actionable steps to improve performance.
  - Student Persona: A classification of the student’s performance (e.g., High Achiever, Steady Learner).
- Graphs and charts will be generated to visualize the student’s performance.

**File Descriptions**

1. `data_analysis.py`
Purpose: Processes the quiz data.
Functions:
  - `analysing_performance()`: Calculates accuracy, topic-wise performance, and difficulty-level performance.

2. `insights_generation.py`
Purpose: Generates insights based on the analyzed data.
Functions:
  - `generating_insights()`: Identifies weak topics, improvement trends, and performance gaps.
  - `generating_recommendations()`: Gives recommendation to the student where to improve.
  - `generating_student_persona()`: Highlights the student's strengths and weaknesses.

3. `visualisation.py`
Purpose: Creates visual representations of the student’s performance.
Functions:
  - `plotting_topic_accuracy()`: Generates a bar chart showing the student’s accuracy in different topics.
  - `plotting_performance_over_time()`: Generates a line graph showing the student’s performance trends over time.
  - `plotting_accuracy_distribution()`: Generates a graph to show the accuracy of the student's performace.

4. `main.py`
Purpose: The main script that runs the analysis and displays the results.
Functions:
  - Calls functions from `data_analysis.py`, `insights_generation.py`, and `visualisation.py` to analyze the data, generate insights, and create visualizations.

**Requirements**

- Python 3.x
- Libraries:
  - `json`
  - `collections`
  - `matplotlib`
  - `seaborn`

Install the required libraries using:
