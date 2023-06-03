import logging

def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(str(e))
                elif mode == "file":
                    logging.basicConfig(filename='error.log', level=logging.ERROR)
                    logging.error(str(e))
        return wrapper
    return decorator

