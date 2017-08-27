# Deeplearning

Mục tiêu chung: Anh/ chị có thể hiểu và nắm được cách xây dựng một model neural network cho một bài toán cụ thể.

## Sử dụng Jupyter Notebook

Chúng ta vẫn sử dụng công cụ này như giới thiệu ở bài thực hành [trước](https://github.com/kienvu58/face_detection)

## Keras

Keras là công cụ trợ giúp các anh/chị với deep learning. Tìm hiểu thêm về Keras có thể xem tại [đây](https://keras.io).

## CNN

Trong phần này, anh/chị được thực hành các bước cơ bản trong một bài toán phân loại có sử dụng convolutional neural network. Mục tiêu của phần này là anh/ chị có thể hiểu được cách xây dựng một model CNN đơn giản có chức năng phân loại các ảnh. 
- Trong **CNN Cifar.ipynb** anh/ chị tự xây dựng một mạng ConvNet cho bài toán classification với bộ dataset CIFAR10.
- Trong **CNN_trainedmodel.ipynb** 1 ví dụ cho anh/ chị có thể áp dụng trực tiếp kết quả training có sẵn vào mục đích classification của mình. 
- **Visualize convolution.ipynb** giúp anh/ chị thấy được kết quả của một ảnh sau khi đi qua một lớp trong mạng ConvNet.
- **CNN_Catech** là phần tự thực hành, anh/ chị áp dụng cách làm tương tự để có một model classification cho bộ dataset [Catech](http://www.vision.caltech.edu/Image_Datasets/Caltech101/)

## RNN

Trong phần này, anh/ chị sẽ được tiếp cận một vài bài toán được giải quyết bằng phương pháp của RNN.
- Trong **RNN_text_generation** anh/ chị sẽ tìm hiểu bài toán generation text sử dụng một mạng RNN đơn giản. 
- Trong **RNN simple** anh/ chị sẽ tìm hiểu bài toán setiment classification.

## Autoencoder

Tương tự với CNN, trong phần này các anh/ chị sẽ được tìm hiểu cách xây dựng một model cho mục đích autoencoder bằng Convolution neural network trong mục **autoencoder_Convolution_version.ipynb** và mạng full connected trong mục **autoencoder_simple_version.ipynb**

# Task 
Đóng vai trò quan trọng trong deep learning là việc lựa chọn hàm loss cũng như sử dụng hàm optimizer . Trong RNN, việc chọn các parameter này lại cực kỳ nhạy cảm. Thay đổi parameter như batch_size, epochs,... là một task chung cho từng phần mục CNN, RNN , Autoencoder.
