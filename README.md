# Streamlit Web App

This repository contains the code for my portfolio website, which is hosted on [https://portfolio-manu.streamlit.app/](https://portfolio-manu.streamlit.app/). The website is created using Streamlit, a Python library for building interactive web applications.

## Contents

- `assets/`: Folder containing images and resume files used in the website.
- `pages/`: Folder containing different pages used in the multipage deployment.
- `styles/`: Folder containing CSS stylesheets for the website.
- `.gitignore`: File specifying which files and directories to ignore in version control.
- `.streamlit/`: Folder containing `config.toml` file for Streamlit configuration.
- `Portfolio.py`: The main Python script containing the code for the Streamlit web application.
- `constants.py`: Python file containing textual information used in the application.
- `dummy.py`: Unused Python file.

## About Streamlit

Streamlit is an open-source Python library that makes it easy to create interactive web applications for data science and machine learning projects. With Streamlit, you can quickly turn your Python scripts into interactive dashboards, without needing to write HTML, CSS, or JavaScript code.

For more information about Streamlit, check out the official documentation.

## Sub-projects (Pages)

### Planning Financial Freedom

This page helps users visualize the power of compounding in investments. It features an interactive calculator where you can input your initial investment, expected rate of return, and the number of years to project the growth of your portfolio.

### SPX Market Monitor

This page allows you to track the closing prices of individual S&P 500 companies. You can select a company and a date range to view its historical stock performance.

### Compare S&P Stocks

This page enables a comparative analysis of multiple S&P 500 stocks. You can select several companies to plot their closing prices on the same graph, making it easier to identify trends and relative performance.

### YoutubePremium

A tool to download YouTube videos as either MP3 (audio) or MP4 (video) files. Simply paste the YouTube link, and the app will handle the conversion and download.

### Connect

A page with a simple contact form to get in touch with me.