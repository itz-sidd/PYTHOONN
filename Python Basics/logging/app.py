import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger('ArithmeticApp')

def add(a,b):
    result=a+b
    logger.debug(f"Adding{a}+{b}={result}")
    return result

def subs(a,b):
    result=a-b
    logger.debug(f"Substraction{a}-{b}={result}")
    return result

def mul(a,b):
    result=a*b
    logger.debug(f"Multiply{a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Division{a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    

add(10,5)
subs(10,5)
mul(10,5)
divide(10,5)