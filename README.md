# TensionFlow-hacksync25

Got it! Since you're using **Gemini** instead of OpenAI, I'll update the README accordingly. Here’s your updated README:  

---

# **Tale.AI - Interactive Story Generator**  

## **Overview**  
Tale.AI is an AI-powered storytelling companion designed for writers. It generates interactive stories based on user inputs such as genre, writing style, intent, and length. Users can also regenerate, continue, conclude stories, and even listen to them.  

## **Dependencies**  
Ensure you have the following dependencies installed:  

### **Backend Requirements (Python)**
- Python (>=3.8)  
- Flask (`pip install flask`)  
- Google Generative AI SDK for Gemini (`pip install google-generativeai`)  
- Flask-CORS (`pip install flask-cors`)  

### **Frontend Requirements (HTML, CSS, JavaScript)**
- A modern web browser (Chrome, Firefox, Edge, etc.)  

## **Setup and Execution**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/TaleAI.git
cd TaleAI
```

### **2. Set Up the Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

> If `requirements.txt` does not exist, manually install the dependencies:  
```bash
pip install flask flask-cors google-generativeai
```

### **4. Configure Gemini API Key**  
- Sign up for Google AI Studio: [https://aistudio.google.com/](https://aistudio.google.com/)  
- Get your **Gemini API Key** and export it:  
```bash
export GEMINI_API_KEY="your_api_key_here"  # On Windows: set GEMINI_API_KEY="your_api_key_here"
```

### **5. Run the Flask Server**  
```bash
python app.py
```

### **6. Access the Web Interface**  
- Open your browser and go to:  
  ```
  http://127.0.0.1:5000/
  ```

## **API Endpoints**  
| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| `/generate`      | POST   | Generates a new story based on user input |
| `/continue_story` | POST   | Continues an existing story |
| `/suggest_title` | POST   | Suggests a title for the generated story |
| `/conclude_story` | POST   | Provides a conclusion for the story |
| `/listen`        | POST   | Converts the story to audio |

## **Contributing**  
Feel free to fork the project and submit a pull request.  

## **License**  
This project is under the **MIT License**.  

---

This README now accurately reflects the use of **Gemini** for text generation. Let me know if you need any further tweaks! 🚀
