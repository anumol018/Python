from google.colab import drive
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from google.colab import files
import shutil

# Mount your Google Drive
drive.mount('/content/drive')
print("Google Drive is mounted!")

uploaded=files.upload()
for filename in uploaded.keys():
  shutil.move(filename,'/content/drive/mydrive/' + filename)

# Open an image file
image_path = "/content/drive/MyDrive/download.jpg"  # Provide the full path to the image file
img = mpimg.imread(image_path)

# Display the image
plt.imshow(img)
plt.axis('off')  # Optional: Hide axes for better view
plt.show()

print(f"Downloading the file: {image_path}")
files.download(image_path)
