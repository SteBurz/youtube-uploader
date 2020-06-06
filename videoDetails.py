import os

class Video:
    description = "test description"
    category = "22"
    keywords = "test"
    privacyStatus = "private"

    def getFileName():
        for file in os.listdir("D:\\Videos\\Youtube\\Upload"):
            return file
            break
