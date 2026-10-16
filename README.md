# MS Dhoni ODI Performance Analysis

## Project Overview

This project analyzes MS Dhoni's One Day International (ODI) cricket performance using Python and data analysis libraries. It explores his batting statistics, performance against different opposition teams, and yearly scoring trends through data visualization.

## Objectives

- Analyze overall batting performance.
- Calculate career statistics such as runs, batting average, and strike rate.
- Identify centuries, half-centuries, fours, and sixes.
- Compare batting averages against major opposition teams.
- Visualize matches played and runs scored by year.

## Technologies Used

- **Python** — Data analysis and programming
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Seaborn** — Data visualization library
- **Excel** — Dataset storage (`.xlsx` format)

## Project Files

| File | Description |
|---|---|
| `project.py` | Python script for data processing, statistical analysis, and visualization |
| `dataset.xlsx` | Dataset containing ODI match and batting performance information |

## Features

1. **Career Statistics:** Calculates total runs, innings, not-outs, batting average, and strike rate.
2. **Highest Score:** Identifies the highest individual score in the dataset.
3. **Batting Milestones:** Counts centuries and half-centuries.
4. **Boundary Analysis:** Calculates total fours and sixes.
5. **Opposition Analysis:** Examines matches, runs, and batting averages against different teams.
6. **Yearly Performance:** Visualizes matches played and runs scored across years.

## Installation and Setup

### Prerequisites

Install Python 3 and the required libraries.

### Install Dependencies

Open a terminal and run:

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### Run the Project

1. Clone or download this repository.
2. Keep `project.py` and `dataset.xlsx` in the same folder.
3. Open a terminal in that folder.
4. Update the dataset path in `project.py` to use the local file:

```python
data = pd.read_excel("dataset.xlsx")
```

5. Execute the script:

```bash
python project.py
```

The script prints statistical results and displays graphs for performance analysis.

## Visualizations

The project generates charts for:

- Number of matches against different opposition teams
- Runs scored against different opposition teams
- Batting averages against major teams
- Matches played by year
- Runs scored by year

## Learning Outcomes

This project demonstrates practical skills in Python programming, data cleaning, statistical analysis, data manipulation, and graphical representation of sports data.

## Future Enhancements

- Develop an interactive dashboard using Streamlit.
- Add filters for opposition teams and years.
- Include additional batting performance metrics.
- Improve visualizations with interactive charts.

## Author

**Manjunatha K V**

GitHub: [@Iammanju14](https://github.com/Iammanju14)

---

*This project is intended for educational and data analysis purposes.*
