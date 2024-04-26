import cv2 
import mediapipe as mp
import numpy as np
import os
import time

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

video = cv2.VideoCapture(0)

seq_length = 30
data = []
action = "reject"
a=9
#학습시킬 action 
#[bathroom, scissors, rainbow, ginseng, mountain, girl, sometimes, nineteen, remote, reject]

created_time = int(time.time())



while True: 
  ret, frame = video.read()
  frame = cv2.flip(frame , 1)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  result = hands.process(frame)
  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
  result.multi_hand_landmarks


  if result.multi_hand_landmarks is not None:
    for res in result.multi_hand_landmarks:
      mp_drawing.draw_landmarks(frame, res, mp_hands.HAND_CONNECTIONS)
      joint = np.zeros((21, 4))
      for j, lm in enumerate(res.landmark):
          joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

      v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19], :3] 
      v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], :3] 
      v = v2 - v1 
      v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]
      if cv2.waitKey(1) == ord('c') :
        print("찰칵")
        angle = np.arccos(np.einsum('nt,nt->n',
            v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
            v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:]))

        angle = np.degrees(angle) 

        angle_label = np.array([angle], dtype=np.float32)
        angle_label = np.append(angle_label, a)
        d = np.concatenate([joint.flatten(), angle_label])
        data.append(d)

  cv2.putText(frame, action, (50, 50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 0))

  cv2.imshow('Video', frame)

  if cv2.waitKey(1) == ord('q'):
    break

data = np.array(data)
print(action, data.shape)
np.save(os.path.join('dataset', f'raw_{action}_{created_time}'), data)

full_seq_data = []
for seq in range(len(data) - seq_length):
  full_seq_data.append(data[seq:seq + seq_length])

full_seq_data = np.array(full_seq_data)
print(action, full_seq_data.shape)
np.save(os.path.join('dataset', f'seq_{action}_{created_time}'), full_seq_data)
