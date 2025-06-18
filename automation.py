import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Message to send
MESSAGE = """
📢 GOQii Health Plan Offer! 💪

Get fit and stay healthy with GOQii Smart Health Plans!
🔥 Limited Time Offer – Get up to 60% OFF on GOQii subscription plans!

✅ Personalized Health Coaching
✅ Doctor Consultation
✅ Fitness Tracking
✅ FREE Health Check-ups
✅ Health Insurance

📞 Call us at: 9004212677

Stay healthy, stay GOQii! ❤️
"""

# Load numbers from Excel
df = pd.read_excel(r"C:\Users\userc\OneDrive\Desktop\client auto mesagges\contacts.xlsx")
numbers = df['Phone'].astype(str).tolist()

# Setup Chrome
options = Options()
options.add_argument("--user-data-dir=C:/Users/userc/OneDrive/Desktop/client auto mesagges/ChromeProfile")
options.add_argument("--profile-directory=Default")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)  # keep browser open

# Set path to your downloaded ChromeDriver
CHROMEDRIVER_PATH = r"C:\Users\userc\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(CHROMEDRIVER_PATH)

# Launch browser
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")
print("🚀 Waiting for WhatsApp Web to load...")

# Wait for manual login
input("✅ After logging into WhatsApp Web, press ENTER to continue...")

# Send messages
for number in numbers:
    print(f"📨 Sending to: {number}")
    url = f"https://web.whatsapp.com/send?phone={number}&text={MESSAGE}"
    driver.get(url)
    time.sleep(10)
    try:
        send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
        send_button.click()
        print(f"✅ Message sent to {number}")
    except Exception as e:
        print(f"❌ Could not send to {number}: {e}")
    time.sleep(5)

print("✅ All messages attempted.")
