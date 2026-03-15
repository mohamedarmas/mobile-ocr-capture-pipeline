import time
import logging

def retry_operation(func, retries=3, delay=2):

    for attempt in range(retries):
        try:
            return func()

        except Exception as e:
            logging.warning(f"Attempt {attempt+1} failed: {e}")

            if attempt == retries - 1:
                raise

            time.sleep(delay * (attempt + 1))