from selenium import webdriver
from openai import OpenAI
import base64

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://ai-for-devs.com")

# Take a screenshot and save it as 'screenshot.png'
driver.save_screenshot("screenshot.png")

# Quit the WebDriver session
driver.quit()

client = OpenAI()

def encode_image(image_path):
  with open(image_path, "rb") as image_file: 
    return base64.b64encode(image_file.read()).decode('utf-8') 

base64_image = encode_image('screenshot.png')

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": """
            You are a UX expert.
            You will be given a screenshot of a webpage.
            You will then provide a list of observations and recommendations to enhance conversion rates on the webpage.

            Respond in the JSON format.
          """
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Here are some observations and recommendations to enhance conversion rates on this webpage:\n\n### **1. Hero Section:**\n\n#### **Observations:**\n- **Call to Action (CTA):** The \"Unlock Access To All Courses\" button is prominently placed but could benefit from clearer value proposition text.\n- **Headline:** \"Get In-Demand AI Expertise to boost earnings and stay ahead\" is a clear headline, but it could be more compelling.\n\n#### **Recommendations:**\n- **Optimize CTA Text:** Modify the button text to include a benefit, e.g., “Start Learning Now”, \"Get Instant Access\", or “Unlock AI Mastery Now”.\n- **Subheadline:** Add a persuasive subheadline beneath the main headline to supplement the benefits, e.g., “Learn from Industry Experts, Risk-Free for 7 Days!”\n- **Visual Hierarchy:** Ensure that the headline and subheadline use different font sizes or styles to establish a clear visual hierarchy.\n\n### **2. Cookie Consent Banner:**\n\n#### **Observations:**\n- The banner takes up significant space and can divert attention from the main content.\n\n#### **Recommendations:**\n- **Optimize Content:** Make the content more concise if possible.\n- **Better Placement:** Consider minimizing this banner to a smaller, less intrusive notification that"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)