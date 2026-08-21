from src.agents.vision_agent import vision_agent


state = {
    "frame_paths": [
        "data/frames/frame_0000.jpg",
        "data/frames/frame_0010.jpg",
        "data/frames/frame_0020.jpg",
    ]
}


result = vision_agent(state)

print("\nErrors:")
print(result.get("errors", []))

print("\nVideo identity data:")
print(result.get("video_identity_data"))