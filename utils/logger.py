import os
from functools import wraps
from time import perf_counter
from loguru import logger


class MyLogger:
    def __init__(self, log_dir='./logs', rotation="1 day", retention='7 days', level="DEBUG"):
        self.log_dir = log_dir
        self.rotation = rotation
        self.retention = retention
        self.level = level
        self.logger = self.configure_logger()

    def configure_logger(self):
        # 创建日志目录
        os.makedirs(self.log_dir, exist_ok=True)
        logger.add(
            sink=f"{self.log_dir}/{{time:YYYY-MM-DD}}.log",
            rotation=self.rotation,
            retention=self.retention,
            level=self.level,
            encoding="utf-8",
            enqueue=True,
            backtrace=True
        )
        return logger

    def __getattr__(self, level: str):
        return getattr(self.logger, level)

    def log_decorator(self, msg="函数异常"):

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                self.logger.info(f'-----------分割线-----------')
                self.logger.info(f'调用 {func.__name__} args: {args}; kwargs:{kwargs}')
                start = perf_counter()  # 开始时间
                try:
                    result = func(*args, **kwargs)
                    end = perf_counter()  # 结束时间
                    duration = end - start
                    self.logger.info(f"{func.__name__} 返回结果：{result}, 耗时：{duration:4f}s")
                    return result
                except Exception as e:
                    self.logger.exception(f"{func.__name__}: {msg}")
                    self.logger.info(f"-----------分割线-----------")
                    # raise e

            return wrapper

        return decorator
