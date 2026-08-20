from src.agents.id_agent import id_agent


state = {
    "id_image_path": "data/ids/test_img.jpg",
}


result = id_agent(state)


print("\nErrors:")
print(result.get("errors", []))


print("\nIdentity data:")
print(result.get("identity_data"))