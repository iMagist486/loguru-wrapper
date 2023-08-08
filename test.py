from utils.logger import MyLogger

logger = MyLogger()

# %%
logger.trace('级别名称：trace，严重值：5')
logger.debug('级别名称：debug，严重值：10')
logger.info('级别名称：info，严重值：20')
logger.success('级别名称：success，严重值：25')
logger.warning('级别名称：warning，严重值：30')
logger.error('级别名称：error，严重值：40')
logger.critical('级别名称：critical，严重值：50')


# %%
@logger.log_decorator("函数异常")
def test_zero_division_error(a, b):
    return a / b


test_zero_division_error(1, 0)
