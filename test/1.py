import cv2
import mediapipe as mp
import numpy as np
import os

# hand 카테고리를 가지고 옴
mp_hands = mp.solutions.hands
# 마디마다 그려줌
mp_drawing= mp.solutions.drawing_utils 
hands = mp_hands.Hands( # Hand가
    max_num_hands=2,
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
a=0
seq_length=30
data=[]
action="ice"
label_code=1

if cap.isOpened():
    
    while True:
        ret, img = cap.read()
        # 
        img=cv2.putText(img, "blind_language", (0,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 1, cv2.LINE_AA)
        img=cv2.flip(img,1)
        result = hands.process(img)
        result.multi_hand_landmarks 
        if result.multi_hand_landmarks is not None:
            for res in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img,res,mp_hands.HAND_CONNECTIONS)

        cv2.imshow("IMG", img)
        key = cv2.waitKey(1)
        if key == ord("c"):
            if result.multi_hand_landmarks is not None:
                for res in result.multi_hand_landmarks:
                    joint = np.zeros((21, 4))
                    for j, lm in enumerate(res.landmark):
                        joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

                v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19], :3] 
                v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], :3] 
                v = v2 - v1 
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]
                print("찰칵")
                angle = np.arccos(np.einsum('nt,nt->n',
                    v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                    v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:]))

                angle = np.degrees(angle)

                angle_label = np.array([angle], dtype=np.float32)
                angle_label = np.append(angle_label, label_code)
                d = np.concatenate([joint.flatten(), angle_label])
                data.append(d)
        
                
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
data = np.array(data)
print(action, data.shape)
np.save(os.path.join('dataset', f'raw_{action}'), data)

full_seq_data = []
for seq in range(len(data) - seq_length):
    full_seq_data.append(data[seq:seq + seq_length])

full_seq_data = np.array(full_seq_data)
print(action, full_seq_data.shape)
np.save(os.path.join('dataset', f'seq_{action}'), full_seq_data)



