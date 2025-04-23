# Four known reference points on surface in camera view
pts_camera = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], dtype=np.float32)
# Corresponding points in projector (canvas) space
pts_projector = np.array([[u1, v1], [u2, v2], [u3, v3], [u4, v4]], dtype=np.float32)

# Calculate homography
H, _ = cv2.findHomography(pts_camera, pts_projector)

# Convert detected (x, y) from camera to projector space
point_camera = np.array([[x, y]], dtype='float32')
point_projector = cv2.perspectiveTransform(np.array([point_camera]), H)