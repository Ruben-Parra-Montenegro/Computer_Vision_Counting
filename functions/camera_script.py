import cv2

# Works both when run from main.py and when running this file directly
try:
    from functions.gray_scale import gray_scale_frame
    from functions.binary_thresholding import binary_threshold
    from functions.morph_close_open import morph_operation
    from functions.counting import count_objects
except ImportError:
    from gray_scale import gray_scale_frame
    from binary_thresholding import binary_threshold
    from morph_close_open import morph_operation
    from counting import count_objects


def run_camera():

    # Initialize webcam
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    # Set camera resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        # Capture frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        gray_frame = gray_scale_frame(frame)
        
        binary_frame = binary_threshold(gray_frame)

        morph_frame = morph_operation(binary_frame)

        count = count_objects(morph_frame)

        grayscale_3channel = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

        binary_3channel = cv2.cvtColor(binary_frame, cv2.COLOR_GRAY2BGR)

        morph_3channel = cv2.cvtColor(morph_frame, cv2.COLOR_GRAY2BGR)

    
        top_row = cv2.hconcat([frame, grayscale_3channel])
        bottom_row = cv2.hconcat([binary_3channel, morph_3channel])
        combined_feed = cv2.vconcat([top_row, bottom_row])

        # Live count in the top-left corner
        cv2.putText(combined_feed, f"Count: {count}", (10, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display processed frame
        cv2.imshow("Live Camera", combined_feed)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release camera and close windows
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    run_camera()
