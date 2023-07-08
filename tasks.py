from celery import shared_task


@shared_task(ignore_result=False)
def count_words(*args, **kwargs) -> int:
    print(kwargs)
    return 10
