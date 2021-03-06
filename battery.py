from discord_webhook import DiscordWebhook
import psutil as psu
import time

# your discord webhook url goes here
WEBHOOK_URL = "https://discord.com/api/webhooks/793655410749997077/UWaKE9FyLnu8zqW1GOwR7uzHgQGp_Ycm-diAaZvLuPNo0zK1ysmULNwRehNPv2Sd0Xmb"


if __name__ == "__main__":
    start = time.time()
    print("Battery Monitor Started")
    while True:
        battery = psu.sensors_battery()
        battery_percent = int(str(battery.percent))
        if battery_percent == 100 and battery.power_plugged:
            end = time.time()
            DiscordWebhook(url=WEBHOOK_URL, content="Battery Full, Please unplug\nTime Taken = {} minutes".format(
                int(end - start)/60)).execute()
            quit()
        time.sleep(60)
