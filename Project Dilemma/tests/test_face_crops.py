import cv2
from insightface.app import FaceAnalysis


app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"],
)

app.prepare(
    ctx_id=0,
    det_size=(640, 640),
)


images = {
    "id": "data/ids/test_img.jpg",
    "video_1": "data/frames/frame_0000.jpg",
    "video_2": "data/frames/frame_0080.jpg",
}


for name, path in images.items():

    image = cv2.imread(path)

    faces = app.get(image)

    print(
        f"{name}: {len(faces)} face(s)"
    )

    for i, face in enumerate(faces):

        x1, y1, x2, y2 = map(
            int,
            face.bbox,
        )

        crop = image[
            max(0, y1):y2,
            max(0, x1):x2,
        ]

        output = (
            f"data/frames/"
            f"debug_{name}_{i}.jpg"
        )

        cv2.imwrite(
            output,
            crop,
        )

        print(
            f"  face {i}: "
            f"{face.bbox} → {output}"
        )