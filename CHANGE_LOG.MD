
# 更新日志

![FuXLogger](https://media.tenor.com/A11YI0qGHRoAAAAi/fu-xuan-honkai-star-rail.gif)

## v0.2.3 (2024-9-28 16:56)

- ***添加 {workdir} 变量到 LogFormatter, 用于获取当前工作目录***

## v0.2.2 (2024-9-28)

- ***logger.exception()方法改进, 添加了is_fatal参数, 用于用户确认此异常是否为致命错误, 并将其写入日志***

## v0.2.1 (2024-9-26)

- ***修复了一些bug***

## v0.2.0 (2024-9-25)

- ***实现异步记录日志功能,示例代码如下***

```python
from FuXLogger import LogManager , LogLevel , StreamHandler , LogFormatter
import asyncio

async def main():
    my_log_fmt = LogFormatter("{time} | {levelName:<7} | {module}:{function} | {file}:{line:02} | {message}")
    logger = LogManager.getLogger("main", my_log_fmt, False, True)

    console_handler = StreamHandler("console", LogLevel.TRACE, my_log_fmt,colorize=True, enableXMLRender=True)

    logger.addHandler(console_handler)

    logger.trace("trace message")
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.fatal("fatal message")
    await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
```

## v0.1.0 (2024-9-24)

- 实现基本功能
