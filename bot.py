import webbrowser
import pyautogui
import pandas as pd
import time
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

def setup_logging():
    """Configures the logging system with file rotation."""
    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_handler = RotatingFileHandler(
        "logs/automation.log", 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3,
        encoding='utf-8'
    )
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)
    
    logger = logging.getLogger("ProductBot")
    logger.setLevel(logging.INFO)
    logger.addHandler(log_handler)
    logger.addHandler(logging.StreamHandler())
    return logger

logger = setup_logging()

def fill_field(value):
    """Presses TAB and writes the provided value."""
    pyautogui.press("tab")
    pyautogui.write(str(value))
    
def perform_login(login, password):
    """Executes the login routine on the form."""
    try:
        logger.info("Attempting to login...")
        pyautogui.press("tab")
        pyautogui.write(login)
        pyautogui.press("tab")
        pyautogui.write(password)
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(3)
        logger.info("Login processed.")
    except Exception as e:
        logger.error(f"Technical failure during login: {e}")
        raise

def main():
    """Main function to orchestrate the automation."""
    try:
        load_dotenv()
        
        user_session = os.getlogin()
        browser_name = os.getenv("BROWSER")
        form_url = os.getenv("URL_FORM")
        credentials_user = os.getenv("LOGIN")
        credentials_pass = os.getenv("PASSWORD")
        csv_filename = os.getenv("CSV_FILENAME")
        
        pyautogui.PAUSE = 0.5
        
        logger.info(f"Session started by: {user_session}")

        logger.info(f"Opening browser: {browser_name}")
        browser = webbrowser.get(browser_name)
        browser.open(form_url)
        time.sleep(3)

        perform_login(credentials_user, credentials_pass)

        logger.info(f"Reading {csv_filename} database")
        if not os.path.exists(csv_filename):
            raise FileNotFoundError(f"The file {csv_filename} was not found!")
            
        df = pd.read_csv(csv_filename)
        logger.info(f"{len(df)} products loaded.")

        for index, row in df.iterrows():
            product_id = row["codigo"]
            try:
                logger.info(f"Processing item {index + 1}/{len(df)}: {product_id}")

                # Initial positioning
                pyautogui.click(x=890, y=288)
                pyautogui.write(str(product_id))

                # Fill sequential fields
                fill_field(row["marca"])
                fill_field(row["tipo"])
                fill_field(row["categoria"])
                fill_field(row["preco_unitario"])
                fill_field(row["custo"])

                # Handle observations
                pyautogui.press("tab")
                observation = row["obs"]
                if not pd.isna(observation):
                    pyautogui.write(str(observation))

                # Submit form
                pyautogui.press("tab")
                pyautogui.press("enter")
                
                # Success confirmation log
                logger.info(f"✅ Item {product_id} registered successfully.")
                
                time.sleep(1)
                pyautogui.scroll(5000)
                
            except pyautogui.FailSafeException:
                logger.critical("🛑 Fail-safe triggered! Stopping bot immediately.")
                raise 

            except Exception as e:
                logger.warning(f"⚠️ Error processing row {index} (ID: {product_id}): {e}")

        logger.info("Automation finished successfully!")

    except Exception as e:
        logger.critical(f"Automation stopped due to critical error: {e}")
    finally:
        logger.info("Closing bot.")

if __name__ == "__main__":
    main()
    