# DoughnutChartAPI 🍩

DoughnutChartAPI is a FastAPI-based backend service that generates customizable doughnut charts from user-provided data, performs basic sales analytics, and generates AI-powered business insights using Google's Gemini model.

## Live API

Interactive Swagger Documentation:

[https://doughnut-chart-api.onrender.com/docs#/default/visual_visualise_data_post](https://doughnut-chart-api.onrender.com/docs#/default/visual_visualise_data_post)

---

## Sample Generated Chart

Charts are automatically uploaded to Cloudinary and returned as publicly accessible URLs.

Example:

[https://res.cloudinary.com/dzb2yohjx/image/upload/v1780994278/x7vzxyw2dicthfo80am8.png](https://res.cloudinary.com/dzb2yohjx/image/upload/v1780994278/x7vzxyw2dicthfo80am8.png)

---

## The Story Behind DoughnutChartAPI

While solving a data visualization challenge on StrataScratch, I encountered a requirement to create a doughnut chart.

During implementation, I realized that Matplotlib does not provide a direct method for generating doughnut charts. A doughnut chart is typically created by:

1. Generating a pie chart.
2. Overlaying a white circular patch at the center.
3. Creating the visual effect of a doughnut.

This led to the idea of building DoughnutChartAPI — a reusable backend service that simplifies doughnut chart creation while also providing analytics and AI-generated insights from the supplied data.

The goal was to transform a commonly repeated visualization technique into an easy-to-use API.

---

## Features

* Generate Doughnut Charts from JSON input.
* Automatic Cloudinary Uploads.
* Sales Data Analytics.
* AI-Powered Business Summaries using Gemini.
* REST API built with FastAPI.
* Interactive Swagger Documentation.
* UUID-based chart naming to prevent file collisions.
* Environment-based configuration management.

---

## Tech Stack

### Backend

* FastAPI
* Pydantic
* Python

### Data Processing

* Pandas

### Visualization

* Matplotlib
* Matplotlib Patches

### AI Integration

* Google Gemini

### Cloud Storage

* Cloudinary

### Deployment

* Render

---

## API Workflow

Client Request

↓

Validate Input

↓

Generate Doughnut Chart

↓

Perform Analytics

↓

Upload Chart To Cloudinary

↓

Generate AI Summary

↓

Return Response

---

## Example Request

```json
{
  "label": [
    "Python",
    "JavaScript",
    "Java",
    "C++"
  ],
  "values": [
    45,
    30,
    15,
    10
  ],
  "color": {
    "Python": "blue",
    "JavaScript": "yellow",
    "Java": "red",
    "C++": "green"
  },
  "figsize": [
    8,
    8
  ],
  "title": "Programming Languages"
}
```

## Example Response

```json
{
  "status": "success",
  "chart_url": "https://res.cloudinary.com/...",
  "total": 100,
  "highest_category": "Python",
  "lowest_category": "C++",
  "average_value": 25,
  "summary": "Python dominates the dataset while C++ has the smallest share..."
}
```

---

## Analytics Generated

The API automatically calculates:

* Total Value
* Highest Category
* Lowest Category
* Average Value
* AI-Generated Business Summary

---

## Project Structure

```text
doughnutChartAPI
│
├── main.py
├── config.py
├── requirements.txt
│
├── serv
│   ├── visualization.py
│   ├── ai_service.py
│   └── data_processing.py
│
└── outputs
```

---
## Learning Outcomes

This project provided hands-on experience with:

* FastAPI Development
* REST API Design
* Pydantic Data Validation
* Data Visualization with Matplotlib
* Cloudinary Integration
* Environment Variable Management
* AI API Integration
* Error Handling
* Cloud Deployment using Render
* Backend Project Structuring

---

## Author

Made with <3 by WeenAIthDev, In collab with Jesus as a practical backend engineering project combining data visualization, cloud services, and AI-powered analytics.
