import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("loggers_info.txt")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def masked_card_num(num: str) -> str:
    """функция принимает номер карты и возвращает замаскированный номер
    @rtype: object
    """
    logger.info(f"start masked_card_num {num}")
    number = 4
    result = num[:number] + " " + num[number : number + 2] + "** ****" + " " + num[number + 8 :]
    logger.info(f"mask {result}")
    return result


def masked_account_num(num: str) -> str:
    """функция принимает номер счёта и возвращает замаскированный номер"""
    logger.info(f"start masked_account_num {num}")
    result = "**" + num[-4:]
    logger.info(f"mask {result}")
    return result
