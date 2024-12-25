import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
from PIL import Image
import numpy as np

# Load the pipeline
pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

# Define the prompt
prompt = "Darth Vader is surfing on waves"

# Generate video frames
video_frames = pipe(prompt, num_inference_steps=40, height=320, width=576, num_frames=24).frames

# Ensure proper shape (remove batch dimension if needed)
video_frames = np.squeeze(video_frames, axis=0)

# Check if the frames have valid channel dimensions
if video_frames.shape[-1] not in [1, 3, 4]:
    raise ValueError("Frames must have 1, 3, or 4 channels.")

# Export to video
video_path = export_to_video(video_frames)
print("Video exported to:", video_path)

