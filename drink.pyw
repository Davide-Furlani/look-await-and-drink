from notifypy import Notify

notification = Notify()
notification.application_name = "Ci penso io a te"
notification.title = "BEVI!!"
notification.message = "Beviiiiiiiiiiiiiiiiii"
notification.icon = "brindis-with-wine-glasses.png"
notification.audio = "drip.wav"
notification.send()