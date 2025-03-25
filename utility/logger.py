import logging


def setup_logger():
    logger = logging.getLogger(name="pytest_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("../logs/test_log.log")
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

