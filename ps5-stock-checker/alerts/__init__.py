from alerts.alert import Alert

async def send_alert(provider=None, link=None):
    alert = Alert(provider=provider, link=link)
    await alert.alert()
