from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import traceback

def scrape_events():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print("Error initializing Chrome WebDriver:", e)
        traceback.print_exc()
        return []

    try:
        driver.get("https://www.timeout.com/sydney")

        print("Page title:", driver.title)
        print("Page URL:", driver.current_url)
        print("Page source snippet:", driver.page_source[:500])

        try:
            # Wait up to 30 seconds for event cards to be present
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article, div[data-testid='event-card']"))
            )
        except:
            print("Timeout waiting for event cards")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.select("article, div[data-testid='event-card']")
        print(f"Found {len(cards)} event cards")

        events = []

        for card in cards:
            try:
                title_tag = card.select_one("h3, .card-title")
                title = title_tag.get_text(strip=True) if title_tag else "Title not found"
                link_tag = card.find("a")
                link = link_tag["href"] if link_tag and "href" in link_tag.attrs else ""
                date_tag = card.select_one(".date, .card-date")
                date = date_tag.get_text(strip=True) if date_tag else "Date not found"
                image_tag = card.find("img")
                image_url = image_tag["src"] if image_tag and "src" in image_tag.attrs else ""
                events.append({
                    "title": title,
                    "link": link,
                    "date": date,
                    "image": image_url
                })
            except Exception as e:
                print(f"Error parsing card: {e}")
                traceback.print_exc()
                continue

        return events
    finally:
        driver.quit()
