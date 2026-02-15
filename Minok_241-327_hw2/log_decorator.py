# log_decorator.py
import functools
import datetime
from pathlib import Path

def function_logger(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            log_path = Path(log_file_path)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            
            start_time = datetime.datetime.now()
            start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            
            try:
                result = func(*args, **kwargs)
                return_value = result if result is not None else '-'
            except Exception as e:
                result = None
                return_value = f'ERROR: {str(e)}'
                raise e
            finally:
                end_time = datetime.datetime.now()
                end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
                

                execution_time = end_time - start_time
                
                #запись лога
                log_entries = [
                    func.__name__,
                    start_time_str,
                    f"args: {args}" if args else "args: ()",
                    f"kwargs: {kwargs}" if kwargs else "kwargs: {}",
                    f"return: {return_value}",
                    end_time_str,
                    str(execution_time),
                    "-" * 50  # разделитель
                ]
                

                with open(log_path, 'a', encoding='utf-8') as f:
                    f.write('\n'.join(log_entries) + '\n')
            
            return result
        return wrapper
    return decorator


if __name__ == '__main__':
    @function_logger('test.log')
    def greeting_format(name):
        return f'Hello, {name}!'
    
    greeting_format('John')