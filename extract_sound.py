import os
import subprocess
import torchaudio

def extract_audio_with_torchaudio(input_folder, output_folder):
    """
    Extract audio from all MP4 videos in a folder, save as WAV files, and process with torchaudio.

    Args:
        input_folder (str): Folder containing the MP4 video files.
        output_folder (str): Folder to save the extracted WAV audio files.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mp4"):
            video_path = os.path.join(input_folder, file_name)
            output_audio_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.wav")

            try:
                # Use ffmpeg to extract audio
                subprocess.run(
                    ["ffmpeg", "-i", video_path, "-vn", "-acodec", "pcm_s16le", output_audio_path],
                    check=True
                )
                print(f"Audio extracted and saved to: {output_audio_path}")

                # Load and process the audio using torchaudio
                audio, sr = torchaudio.load(output_audio_path)
                print(f"Loaded audio with sample rate {sr} and shape {audio.shape}")

            except subprocess.CalledProcessError as e:
                print(f"Error with ffmpeg on file {file_name}: {e}")
            except Exception as e:
                print(f"An error occurred with file {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "/mnt/d/datasets/AudioSet_Drums/AudioSet_Dataset/train/video"  # Folder chứa video
    output_folder = "/mnt/d/datasets/AudioSet_Drums/AudioSet_Dataset/train/audio"  # Folder lưu file WAV

    extract_audio_with_torchaudio(input_folder, output_folder)
