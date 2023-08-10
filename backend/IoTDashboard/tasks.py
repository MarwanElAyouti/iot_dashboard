from IoTDashboard.celery import celery_app


@celery_app.task(name="test_task")
def test_task() -> None:
    print("This is an async test task..")
