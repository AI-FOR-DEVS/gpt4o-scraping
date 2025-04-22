# LinkedIn Profile Analyzer

This project uses Selenium and OpenAI's GPT-4 Vision API to analyze LinkedIn profiles. It takes a screenshot of a LinkedIn profile and uses GPT-4 Vision to extract key information about the candidate.

## Prerequisites

- Python 3.x
- Chrome browser installed
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Install Chrome WebDriver:
   - For macOS: `brew install chromedriver`
   - For other operating systems, download the appropriate version from [ChromeDriver website](https://sites.google.com/chromium.org/driver/)

4. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Update the LinkedIn profile URL in `app.py` to the profile you want to analyze:
```python
driver.get("https://www.linkedin.com/in/your-target-profile/")
```

2. Run the script:
```bash
python app.py
```

The script will:
1. Take a screenshot of the LinkedIn profile
2. Convert the screenshot to base64
3. Send it to GPT-4 Vision API for analysis
4. Print the analysis results in JSON format

## Output

The script outputs a JSON response containing key information about the candidate, analyzed from their LinkedIn profile.

## Notes

- Make sure you have proper permissions to access the LinkedIn profile you're analyzing
- Be mindful of LinkedIn's terms of service and rate limits
- The script requires an active internet connection 