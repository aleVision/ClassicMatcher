# Feature Detection and Object Matching Web App

This web application allows users to upload two images and perform feature detection and matching using traditional computer vision methods like SIFT, ORB, and Harris Corner Detection. The app visualizes the keypoints and matches features between the images interactively.

## 🚀 **Live Web App**
You can access the live web app here:  
[Image Feature Detection Web App]([https://your-deployed-app-link.com)(https://featurematching.streamlit.app/)

## 📦 **Project Features**
- **SIFT (Scale-Invariant Feature Transform)**: Detects keypoints that are invariant to scaling, rotation, and changes in illumination. Great for object recognition.
- **ORB (Oriented FAST and Rotated BRIEF)**: A faster, free alternative to SIFT. Suitable for applications that require speed.
- **Harris Corner Detection**: Detects corners in images where two edges meet.

### Key Features:
1. **Keypoint Detection**: Visualize keypoints detected in both images.
2. **Feature Matching**: Matches features between the two images and displays the matches side by side.
3. **Interactive Interface**: Choose from different feature detection methods and upload your own images.
4. **Download**: Save the matched image with visualized keypoints.

## 🔧 **How It Works**

1. **Upload Two Images**:
   - You can upload any two images to the web app.
   
2. **Select Feature Detection Method**:
   - Choose one of the following methods:
     - **SIFT**: Best for detailed, complex feature matching.
     - **ORB**: Faster but less accurate than SIFT.
     - **Harris Corner Detection**: Finds corners in the image.
   
3. **Feature Matching**:
   - If SIFT or ORB is selected, the app will find the keypoints and match features between the two images.
   
4. **Download the Results**:
   - You can download the image that visualizes the matched keypoints.

## 🛠️ **Tech Stack**
- **OpenCV**: For feature detection, keypoint matching, and image processing.
- **Streamlit**: To build the interactive web application.
- **NumPy**: For handling arrays and image data.
- **Pillow**: For image file handling.

## 🚀 **Getting Started**
### Prerequisites
Make sure you have the following installed:
- Python 3.7+
- OpenCV
- Streamlit
- NumPy
- Pillow

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/FeatureDetectionApp.git
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and go to:
    ```bash
    http://localhost:8501
    ```

## 📖 **References**

- [OpenCV SIFT Documentation](https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html)
- [OpenCV ORB Documentation](https://docs.opencv.org/4.x/db/d95/classcv_1_1ORB.html)
- [OpenCV Harris Corner Detection](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html)

---

Feel free to contribute or fork the project to add more feature detection methods or improve the interface!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
