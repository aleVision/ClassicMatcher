import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Helper function to detect and compute keypoints and descriptors
def detect_features(image, method):
    if method == 'SIFT':
        detector = cv2.SIFT_create()
    elif method == 'ORB':
        detector = cv2.ORB_create()
    elif method == 'Harris':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        harris_corners = cv2.cornerHarris(gray, 2, 3, 0.04)
        image[harris_corners > 0.01 * harris_corners.max()] = [255, 0, 0]
        return image, None, None
    keypoints, descriptors = detector.detectAndCompute(image, None)
    return image, keypoints, descriptors

# Helper function to match features between two sets of keypoints
def match_features(des1, des2, method):
    if method == 'SIFT' or method == 'ORB':
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True) if method == 'SIFT' else cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        return matches
    return None

# Sidebar for user inputs
st.sidebar.title("Feature Detection and Matching Options")

# Information icons and brief explanation for each method
st.sidebar.markdown("### Feature Detection Methods ℹ️")
with st.sidebar.expander("Learn more about each method"):
    st.markdown("""
    - **SIFT**: Scale-Invariant Feature Transform. Detects keypoints that are invariant to scaling, rotation, and illumination.  
      [Learn more](https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html)
      
    - **ORB**: Oriented FAST and Rotated BRIEF. A free alternative to SIFT, it's faster but less accurate.  
      [Learn more](https://docs.opencv.org/4.x/db/d95/classcv_1_1ORB.html)
      
    - **Harris Corner Detection**: Detects corners in an image. Useful for identifying corners where two edges meet.  
      [Learn more](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html)
    """)

# Upload two images
uploaded_file1 = st.sidebar.file_uploader("Upload First Image", type=["jpg", "png", "jpeg"])
uploaded_file2 = st.sidebar.file_uploader("Upload Second Image", type=["jpg", "png", "jpeg"])

# Select feature detection method
method = st.sidebar.selectbox("Choose Feature Detection Method", ["SIFT", "ORB", "Harris"])

if uploaded_file1 is not None and uploaded_file2 is not None:
    # Load both images
    image1 = np.array(Image.open(uploaded_file1))
    image2 = np.array(Image.open(uploaded_file2))

    # Detect keypoints and descriptors
    st.sidebar.subheader("Detecting Features...")

    img1_with_keypoints, kp1, des1 = detect_features(image1, method)
    img2_with_keypoints, kp2, des2 = detect_features(image2, method)

    st.subheader(f"Detected Features using {method}")
    st.image(img1_with_keypoints, caption="Image 1 with Keypoints", use_column_width=True)
    st.image(img2_with_keypoints, caption="Image 2 with Keypoints", use_column_width=True)

    if method != 'Harris':
        # Match features between the two images
        matches = match_features(des1, des2, method)
        matched_image = cv2.drawMatches(image1, kp1, image2, kp2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        st.subheader(f"Matched Features using {method}")
        st.image(matched_image, caption="Matched Features", use_column_width=True)

    # Save button to download the matched image
    st.sidebar.subheader("Download Matched Image")
    if st.sidebar.button("Save Image"):
        cv2.imwrite("matched_image.png", matched_image)
        st.sidebar.write("Matched image saved as 'matched_image.png'.")
