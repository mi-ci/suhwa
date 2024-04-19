import os
import numpy as np

def stack_frames_from_directory_and_save_npy(directory_path, output_file):
    frame_stack = []

    # 디렉토리 내의 모든 파일에 대해 반복합니다.
    for filename in os.listdir(directory_path):
        if filename.endswith(".npy"):  # npy 파일만 처리합니다.
            filepath = os.path.join(directory_path, filename)
            frames = np.load(filepath)
            frame_stack.extend(frames)

    # 모든 프레임을 하나의 배열로 쌓습니다.
    stacked_frames = np.stack(frame_stack, axis=0)

    # 스택된 프레임을 하나의 npy 파일로 저장합니다.
    np.save(output_file, stacked_frames)

    print("프레임 스택을 저장한 npy 파일:", output_file)

# 로드할 파일이 있는 디렉토리 경로를 지정합니다.
directory_path = "./dataset/seq_hot_1713326239"  # 디렉토리 경로 수정

# 출력할 npy 파일의 경로와 이름을 지정합니다.
output_file = "seq_hot_1713326239.npy"  # 저장할 npy 파일명

# 디렉토리에서 모든 npy 파일을 로드하여 스택하고 하나의 npy 파일로 저장합니다.
stack_frames_from_directory_and_save_npy(directory_path, output_file)
