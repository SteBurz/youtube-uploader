import os
from googleapiclient.http import MediaFileUpload

class Video:
    description = "test description"
    category = "22"
    keywords = "test"
    privacyStatus = "private"

    def getFileName(self, type):
        for file in os.listdir("D:\\Videos\\Youtube\\Upload"):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break

    def insertThumbnail(self, youtube, videoId):
        thumnailPath = "D:\\Videos\\Youtube\\Upload\%s" % (self.getFileName("thumbnail"))

        request = youtube.thumbnails().set(
            videoId=videoId,
            media_body=MediaFileUpload(thumnailPath)
        )
        response = request.execute()
        print(response)
