#This code is just a test for showcasing the principle, sound doesnt actually play.
from abc import ABC, abstractmethod

class AudioPlayerInt(ABC):
    @abstractmethod
    def play_audio(self, file_name: str):
        pass

    @abstractmethod
    def stop(self):
        pass

class VideoPlayerInt(ABC):
    @abstractmethod
    def play_video(self, file_name: str):
        pass

    @abstractmethod
    def stop(self):
        pass

class AudioPlayer(AudioPlayerInt):
    def play_audio(self, file_name: str):
        print(f"Playing audio file: {file_name}")
    def stop(self):
        print("Stopping audio player")

class VideoPlayer(VideoPlayerInt):
    def play_video(self, file_name: str):
        print(f"Playing video file: {file_name}")
    def stop(self):
        print("Stopping video player")

ap = AudioPlayer()
ap.play_audio("audio.mp4")
ap.stop()

vp = VideoPlayer()
vp.play_video("video.mp3")
vp.stop()

