import logging
from datetime import datetime
#
# def log_details():
#     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#
#     logging.basicConfig(
#         filename=f"AutoTest_Execution{now}.log",
#         level=logging.INFO,
#         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S %p',
#         filemode='a'
#     )
#     return logging.getLogger("AutoTest")
#
#
#
# logger = log_details()
#
# logger.info("Logging Successful")
#
#


logging.basicConfig(
    filename="test.log",
    level=logging.INFO
)

logging.info("Hello World")