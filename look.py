from notifypy import Notify

notification = Notify()
notification.application_name = "Ci penso io a te"
notification.title = "EHI!!"
notification.message = "Distogli lo suardo"
notification.icon = "eyeglasses.png"
notification.audio = "drip.wav"
notification.send()