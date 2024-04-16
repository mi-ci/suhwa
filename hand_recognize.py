import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 이미지 파일의 경우을 사용하세요.:
IMAGE_FILES = ["americano1.jpg"]
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    # 이미지를 읽어 들이고, 보기 편하게 이미지를 좌우 반전합니다.
    image = cv2.flip(cv2.imread(file), 1)
    # 작업 전에 BGR 이미지를 RGB로 변환합니다.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # 손으로 프린트하고 이미지에 손 랜드마크를 그립니다.
    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
      )
      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    cv2.imwrite(
    './annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))

