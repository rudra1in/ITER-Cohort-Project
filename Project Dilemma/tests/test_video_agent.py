from src.agents.video_agent import video_agent


video_path = "data/videos/verification_video.mp4"

state = {
    "video_path": video_path,
}

result = video_agent(state)

print("Errors:", result.get("errors", []))

frame_paths = result.get("frame_paths", [])

print("Number of frames:", len(frame_paths))

if frame_paths:
    print("First frame:", frame_paths[0])