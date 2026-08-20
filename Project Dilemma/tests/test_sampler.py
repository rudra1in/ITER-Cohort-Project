from src.video.sampler import sample_frames


video_path = "data/videos/verification_video.mp4"

frame_paths = sample_frames(
    video_path,
    target_fps=10,
)

print("Number of sampled frames:", len(frame_paths))

if frame_paths:
    print("First frame:", frame_paths[0])