file = input("File name: ").strip().lower()

extension = file.split(".")[-1] if "." in file else ""

app = ["zip", "pdf"]
image = ["gif", "png", "jpeg"]

if extension in image:
    print(f"image/{extension}")
elif extension == "jpg":
    print(f"image/jpeg")
elif extension in app:
    print(f"application/{extension}")
elif extension == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
