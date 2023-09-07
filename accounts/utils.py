from django.contrib import messages


def notification_system(request, message, notification_type="success"):
    script = f"iziToast.{notification_type}({{message: '{message}'}});"
    messages.info(request, script)
