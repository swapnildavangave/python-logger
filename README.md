# python-logger
Custom python based logging module which allows multiple instances.


Installation:

    ```
    pip install https://github.com/swapnildavangave/python-logger.git
    ```
or

    ```
    git clone https://github.com/swapnildavangave/python-logger.git
    cd python-logger
    python3 setup.py install
    ```

Definition:

    class Logger:
        ...

    def __init__(keys: list, path: str)
        ...

        path : path of the target log file default is /pwd/default.log

        keys : ['process', 'module',...]
        
        inbuild keys:
            'process': process id
            'module': current file name
            'function': current function name
            'asctime': timestamp
            'line': current line number

    def info(data: str, extra: dict={}):
        ...

        data = "Info message"

        extra = {'key':'value'}
    
    def warning(data: str, extra: dict={}):
        ...

        data = "Info message"

        extra = {'key':'value'}
    
    def error(data: str, extra: dict={}):
        ...

        data = "Info message"

        extra = {'key':'value'}


Example:

    ```import python_logger

        logger = python_logger.Logger(keys=['module','function'], path='my_logs.log',)
        logger.info('Info log message', extra={'myid':'12'})
        logger.warning('Warning log message', extra={'myid':'12'})
        logger.error('Warning log message', extra={'myid':'12'})
    ```



