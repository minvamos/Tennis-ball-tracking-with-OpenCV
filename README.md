
# Tennis Ball Tracking Program
![](https://i.imgur.com/FYIKNow.png)
## Overview

This project aims to detect and track the trajectory of tennis balls in match videos. Utilizing OpenCV, the program processes the video to highlight and follow the tennis ball, providing a visual representation of its path. This solution addresses the challenge of manually analyzing tennis ball movements in large court videos where the ball is often too small to track with the naked eye.

## Features

- **HSV Filtering**: Uses HSV color space for more accurate detection under natural lighting conditions.
- **Gaussian Blur**: Reduces noise for better detection accuracy.
- **Morphology Operations**: Enhances the tennis ball's visibility in the filtered video.
- **Background Subtraction**: Differentiates the ball from the background for clearer tracking.
- **Predictive Tracking**: Continues tracking even when the ball is momentarily lost by predicting its position based on previous frames.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tennis-ball-tracking.git
   cd tennis-ball-tracking
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Prepare your video files**:
   Place your video files in the `videos` directory.

## Usage

1. **Run the tracking script**:
   ``` bash
   python track_tennis_ball.py --video videos/your_video.mp4
   ```

## Example

You can find a demo video of the program in action [here](https://youtu.be/0SoFbFIlUkY).

## Results and Analysis

The program was tested on various court surfaces with the following accuracy:
- **Red Clay Court**: 70.1%
- **Blue Clay Court**: 68.3%
- **Grass Court**: 73.6%

The tracking accuracy was measured by comparing the frames where the ball was correctly tracked against the total number of frames.

### Limitations
- **False Positives**: The program may mistakenly track objects of similar color to the tennis ball.
- **High-Speed Ball Movements**: Fast movements may cause the ball to blur, making detection challenging.

## Future Work

To improve accuracy and robustness, future versions could implement deep learning-based object detection and tracking techniques. Additionally, integrating advanced filtering methods to differentiate the tennis ball from similarly colored objects can further enhance performance.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [Hawk-Eye System](https://en.wikipedia.org/wiki/Hawk-Eye)
- [NVIDIA NvDCF](https://developer.nvidia.com/nvdec)

## References

1. 양요셉, 안성민, 김성현, 최동일. "테니스 로봇을 위한 공 추적 및 궤적 예측 시스템." 대한기계학회 2022년 학술대회.
2. [ESPN Wimbledon](https://www.espn.com/sports/tennis/wimbledon08/news/story?id=3452293)
3. [Deep Learning Study Blog](https://deep-learning-study.tistory.com/274)
4. [OpenCV Ball Tracking](https://076923.github.io/exercise/C-opencv-ball_tracking/)
5. [Hawk-Eye Wikipedia](https://en.wikipedia.org/wiki/Hawk-Eye)
6. [Coding Tree Blog](https://durian9s-coding-tree.tistory.com/195)
