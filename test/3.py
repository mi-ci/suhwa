import cv2
import mediapipe as mp
import numpy as np
import os

camera = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

action = "ice"
seq_length = 30
data = []

while True :
  캠연결여부, 이미지 = camera.read()
  result = hands.process(이미지)
  if result.multi_hand_landmarks is not None:
    for res in result.multi_hand_landmarks:
      mp_drawing.draw_landmarks(이미지, res, mp_hands.HAND_CONNECTIONS)

  # cv2.putText(이미지, "AAAA", (100,100), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,0), 2)
  cv2.imshow('my webcam', 이미지)
  

  if cv2.waitKey(1) == ord('c') :
    if result.multi_hand_landmarks is not None:
      for res in result.multi_hand_landmarks:
        joint = np.zeros((21, 4))
        for j, lm in enumerate(res.landmark):
            joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

        v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19], :3] # Parent joint
        v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], :3] # Child jointqqqqqq
        v = v2 - v1 # [20, 3]
        v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]
        print(v.shape)
        angle = np.arccos(np.einsum('nt,nt->n',
            v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
            v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

        angle = np.degrees(angle) # Convert radian to degree

        angle_label = np.array([angle], dtype=np.float32)
        angle_label = np.append(angle_label, 1)
        d = np.concatenate([joint.flatten(), angle_label])
        data.append(d)
     
  
  if cv2.waitKey(1) == ord('q') :
    break

  
data = np.array(data)
print(action, data.shape)
np.save(os.path.join('dataset', f'raw_{action}'), data)
# Create sequence data
full_seq_data = []
for seq in range(len(data) - seq_length):
  full_seq_data.append(data[seq:seq + seq_length])

full_seq_data = np.array(full_seq_data)
print(action, full_seq_data.shape)
np.save(os.path.join('dataset', f'seq_{action}'), full_seq_data)