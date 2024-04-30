<h1 align="center"><img src="https://raw.githubusercontent.com/ABSphreak/ABSphreak/master/gifs/Hi.gif" width="30px"> 프로젝트 헬로수화</h1>
<p align="center">
  <a href="https://github.com/Ratheshan03/readme-typing-svg"><img src="https://readme-typing-svg.herokuapp.com?lines=유나;은영;규림;태창;우진;우성;&center=true&width=700&height=70"></a>
  <br>
  <img src="https://i.imgur.com/CiyBZtG.jpeg">
  <img src="https://i.imgur.com/qapqp5E.jpeg">
  <img src="https://i.imgur.com/40ywq5L.jpeg">
  <img src="https://i.imgur.com/txjDGop.jpeg">
</p>

<br/>

<h2 align="center">
  헬로수화란?
</h2>
수화를 처음 공부하는 청각장애인들의 학습 능률을 높이고
<br>
수화에 관심이 많은 일반인들도 쉽고 재미있게 수화학습을 할 수 있도록 만들어진 교육용 웹 어플리케이션 입니다.
<br>
<br>
헬로수화는 라즈베리파이 카메라를 활용해서 퀴즈도 풀 수 있으며 최대 2명까지 참여할 수 있습니다.
<br>
<br>
<a href="https://20af-1-233-65-186.ngrok-free.app">헬로수화</a>에서 체험 해보실 수 있습니다.


<h2 align="center">
  계기
</h2>

<table align="center" border="0">
  <tr>
    <td>
      <ul>
        <li>
          수화 배우는 것을 재밌게!
        </li>
        <li>
          놀이하듯이 쉽게!
        </li>
        <li>
          청각장애인과 일반인 간의 소통 제고!
        </li>
      </ul>
    </td>
    <td align="center" width="400px">
      <img align="center" src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExanl2NGh4YWo4bXY2bjk5djBzOHcwdmVvN2E0Z3B4em9zenV0d2h6YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CoTHTNblovkG8wHXf4/giphy.gif"/>
    </td>
  </tr>
</table>

<br>






<h2 align="center">
  인트로
</h2>

<p align="center">
  <img src="https://i.imgur.com/eP37J2N.png" width="100%"/>
  <sub>
    홈페이지의 메인 화면 모습이다. 수화를 접할 수 있는 다양한 메뉴들이 있다.
  </sub>
</p>
  
<table align="center" border="0">
  <tr>
    <td width="1000px">
      <b><code>Quiz Start</code></b> 퀴즈 화면으로 넘어간다.
      <br>
      <b><code>How to play</code></b> 설명 화면으로 넘어간다.
      <br>
      <b><code>Dictionary</code></b> 단어장 화면으로 넘어간다.
      <br>
      <b><code>Exit</code></b> 앱을 종료한다.
    </td>
  </tr>
</table>
  
<br>

<h2 align="center">
  퀴즈
</h2>

<p align="center">
  <img src="https://i.imgur.com/qv6Uu72.png" width="1000px"/>
  <sub>
    2명의 사용자가 퀴즈대결을 하고 있는 화면이다
  </sub>
</p>
  
<table align="center" border="0">
  <tr>
    <td width="100%">
      <b><code>Player</code></b> 플레이어명을 표시해준다.
      <br>
      <b><code>Score</code></b> 플레이어의 점수를 표시해준다.
      <br>
      <b><code>Camera</code></b> 플레이어의 라즈베리 카메라 화면을 표시해준다.
    </td>
  </tr>
</table>
  
<br>


<h2 align="center">
  사전
</h2>

<p align="center">
  <img src="https://i.imgur.com/tPNdXDH.png" width="100%"/>
  <sub>
    현재 헬로수화에서 저장하고 있는 단어 Glossary다. 귀여운 보노보노는 덤이다.
  </sub>
</p>




<h2 align="center">
  모델링
</h2>

<table align="center" border="0">
  </tr>
  <tr>
    <td width="1000px">
      <p align="center">
        <img src="https://i.imgur.com/ZMrYb0h.png"/>
        <br>
        <sub>
          Click <a href="https://github.com/mi-ci/suhwa/blob/main/modeling/train.ipynb">여기</a> 를 눌러 전체코드를 확인하세요.
        </sub>
      </p>
    </td>
  </tr>
</table>
<table align="center" border="0">
  <tr>
    우리는 총 10개의 수화에 대해 각자 데이터셋을 만들었다. 
    우리의 데이터는 mediapipe가 제공해주는 21개 손마디를 2개씩 조합하여 마디의 위치, 각도, 레이블이 담긴 numpy array이다.
    이 데이터셋을 또 시간에 따라 겹치게 30장씩 합쳐서 새로운 데이터셋을 만들었다.
    이후 각자의 데이터셋을 하나의 array로 합쳤다.
    <br>
<br><br>
아래는 우리의 수화 인식 모델 학습에 사용된 층이고 채택 이유이다:
<ul>
  <li>
    <b><code>LSTM</code></b> 수화는 제스쳐로 이루어져있으므로 제스쳐를 인식하기 위해 우리는 데이터셋은 여러개의 Sequence로 만들었다(각 Sequence는 30프레임). 첫번째 LSTM층에 128유닛을 주어 우리의 데이터셋을 input을 받는다. 두번째 LSTM층은 64유닛을 주어 보다 input을 받은 값을 보다 정밀하게 학습한다. 
  </li>
      <li>
        <code>BatchNormalization</code> 첫번째 LSTM input layer에서 받은 수화 시퀀스들을 정규화 해줌으로써 텐서플로우가 학습을 더 빠르고 효율적으로 할 수 있게 해주었다.
      </li>
      <li>
        <code>Dense</code> relu 함수를 써서 데이터가 선형으로 가는 것을 방지 하였고 Dense로 LSTM에서 받은 수화 시퀀스들을 분류하기 시작한다. 마지막 Dense층은 softmax 함수를 사용해 각각 수화의 확률값을 분류해주었다.
      </li>
      <li>
        <code>Dropuot</code> 여러 사람이 녹화한 수화 데이터셋은 제스쳐들이 가지각색이므로 오버핏은 과대적합으로 이어질 수 있다. 방지하기 위해 50%를 드롭아웃 해주었다.
      </li>

</ul>
    </td>
</table>

<br>
<h2 align="center">
  예측
</h2>

<table align="center" border="0">
  <tr>
    <td width="350px">
      <p align="center">
        <img src="https://user-images.githubusercontent.com/69165598/150469699-d8a94ab4-7d70-49c3-8736-a9018996f39a.png"/>
        <br>
        <sub>
          Click <a href="https://github.com/tanjeffreyz02/auto-maple/blob/f13d87c98e9344e0a4fa5c6f85ffb7e66860afc0/routines/dcup2.csv">here</a> to view the entire routine.
        </sub>
      </p>
    </td>
    <td>
A routine is a user-created CSV file that tells Auto Maple where to move and what commands to use at each location. A custom compiler within Auto Maple parses through the selected routine and converts it into a list of <code>Component</code> objects that can then be executed by the program. An error message is printed for every line that contains invalid parameters, and those lines are ignored during the conversion. 
<br><br>
Below is a summary of the most commonly used routine components:
<ul>
  <li>
    <b><code>Point</code></b> stores the commands directly below it and will execute them in that order once the character is within <code>move_tolerance</code> of the specified location. There are also a couple optional keyword arguments:
    <ul>
      <li>
        <code>adjust</code> fine-tunes the character's position to be within <code>adjust_tolerance</code> of the target location before executing any commands.
      </li>
      <li>
        <code>frequency</code> tells the Point how often to execute. If set to N, this Point will execute once every N iterations.
      </li>
      <li>
        <code>skip</code> tells the Point whether to run on the first iteration or not. If set to True and frequency is N, this Point will execute on the N-1th iteration.
      </li>
    </ul>
  </li>
  <li>
    <b><code>Label</code></b> acts as a reference point that can help organize the routine into sections as well as create loops.
  </li>
  <li>
    <b><code>Jump</code></b> jumps to the given label from anywhere in the routine.
  </li>
  <li>
    <b><code>Setting</code></b> updates the specified setting to the given value. It can be placed anywhere in the routine, so different parts of the same routine can have different settings. All editable settings can be found at the bottom of <a href="https://github.com/tanjeffreyz02/auto-maple/blob/v2/settings.py">settings.py</a>.
  </li>
</ul>
    </td>
  </tr>
</table>

<br>








<h2 align="center">
  Runes
</h2>

<p align="center">
  <img src="https://user-images.githubusercontent.com/69165598/123479558-f61fad00-d5b5-11eb-914c-8f002a96dd62.gif" width="100%"/>
</p>

<table align="center" border="0">
  <tr>
    <td width="100%">
Auto Maple has the ability to automatically solve "runes", or in-game arrow key puzzles. It first uses OpenCV's color filtration and <b>Canny edge detection</b> algorithms to isolate the arrow keys and reduce as much background noise as possible. Then, it runs multiple inferences on the preprocessed frames using a custom-trained <b>TensorFlow</b> model until two inferences agree. Because of this preprocessing, Auto Maple is extremely accurate at solving runes in all kinds of (often colorful and chaotic) environments.
    </td>
  </tr>
</table>


<br>









<h2 align="center">
  Video Demonstration
</h2>

<p align="center">
  <a href="https://www.youtube.com/watch?v=qs8Nw55edhg"><b>Click below to watch the full video</b></a>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=qs8Nw55edhg">
    <img src="https://user-images.githubusercontent.com/69165598/123308656-c5b61100-d4d8-11eb-99ac-c465665474b5.gif" width="600px"/>
  </a>
</p>

<br>



<h2 align="center">
  Setup
</h2>

<ol>
  <li>
    Download and install <a href="https://www.python.org/downloads/">Python3</a>.
  </li>
  <li>
    Download and install the latest version of <a href="https://developer.nvidia.com/cuda-downloads">CUDA Toolkit</a>.
  </li>
  <li>
    Download and install <a href="https://git-scm.com/download/win">Git</a>.
  </li>
  <li>
    Download and unzip the latest <a href="https://github.com/tanjeffreyz02/auto-maple/releases">Auto Maple release</a>.
  </li>
  <li>
    Download the <a href="https://drive.google.com/drive/folders/1SPdTNF4KZczoWyWTgfyTBRvLvy7WSGpu?usp=sharing">TensorFlow model</a> and unzip the "models" folder into Auto Maple's "assets" directory.
  </li>
  <li>
    Inside Auto Maple's main directory, open a command prompt and run:
    <pre><code>python -m pip install -r requirements.txt</code></pre>
  </li>
  <li>
    Lastly, create a desktop shortcut by running:
    <pre><code>python setup.py</code></pre>
    This shortcut uses absolute paths, so feel free to move it wherever you want. However, if you move Auto Maple's main directory, you will need to run <code>python setup.py</code> again to generate a new shortcut. To keep the command prompt open after Auto Maple closes, run the above command with the <code>--stay</code> flag.
  </li>
</ol>



<!-- About Section -->
 # About Us
 
<p>
 <img align="right" width="350" src="/assets/programmer.gif" alt="Coding gif" />
  
 ✌️ &emsp;  &nbsp;MBC아카데미에서 만났습니다 <br/><br/>
 ❤️ &emsp; 인공지능을 사랑하는 5인입니다<br/><br/>
 📧 &emsp; 언제든 연락주세요: <br>
 💬 &emsp; 무엇이든 물어보세요 [here](https://github.com/mi-ci/suhwa/issues)

</p>

<br/>
<br/>

## 언어

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<br/>
<br/>

## 라이브러리

![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Static Badge](https://img.shields.io/badge/-mediapipe-blue)
<br/>
<br/>
## 프레임워크

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
<br/>
<br/>

## ETC

![Static Badge](https://img.shields.io/badge/-Rpi4-red)


