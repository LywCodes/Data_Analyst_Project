# Bike Rental Dashboard 

## Setup Environment - Shell/Terminal
```
mkdir project_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```

## 1. File Structures
```
.
├── dashboard
│   ├── dashboard.py
│   └── day.csv
├── data
│   ├── Readme.txt
│   ├── day.csv
|   └── hour.csv
├── screenshots
|   ├── Screenshots (91).png
|   ├── Screenshots (92).png
|   ├── Screenshots (93).png
|   └── Screenshots (94).png
├── README.md
├── notebook.ipynb
└── requirements.txt
```

## 2. Project work cycle
1. Data Wrangling: 
 - Gathering data
 - Assessing data
 - Cleaning data
2. Exploratory Data Analysis:
 - Defined business questions for data exploration
 - Create Data exploration
3. Data Visualization:
 - Create Data Visualization that answer business questions
4. Dashboard:
 - Set up the DataFrame which will be used
 - Make filter components on the dashboard
 - Complete the dashboard with various data visualizations

**Note: Numbers 1 to 3 are in the dicoding-collection-exercise and number 4 is in dashboard.**

## 3. Getting Started
### `notebook.ipynb`
1. Download this project.
2. Open your favorite IDE like Jupyter Notebook or Google Colaboratory (but in here I will use Google Colab).
3. Create a New Notebook.
4. Upload and select the file with .ipynb extension.
5. Connect to hosted runtime.
6. Lastly, run the code cells.

### `dashboard/dashboard.py`
1. Download this project.
2. Install the Streamlit in your terminal or command prompt using `pip install streamlit`. Install another libraries like pandas, numpy,  matplotlib, and seaborn.
3. don't move the csv file because it acts a data source. keep it in one folder as dashboard.py
4. Open your VSCode and run the file by clicking the terminal and write it `streamlit run dashboard.py`.

## 4. Screenshots
![Alt text](https://raw.githubusercontent.com/LywCodes/Data_Analyst_Project/main/documentation/dashboard.gif)


![image](https://github.com/LywCodes/Data_Analyst_Project/blob/main/documentation/image_2.png?raw=true)

![image](https://github.com/LywCodes/Data_Analyst_Project/blob/main/documentation/image_1.png?raw=true)

![image](https://github.com/LywCodes/Data_Analyst_Project/blob/main/documentation/image_2.png?raw=true)

![image](https://github.com/LywCodes/Data_Analyst_Project/blob/main/documentation/image_3.png?raw=true)
