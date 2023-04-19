import cv2  # 导入opencv库

if __name__ == '__main__':
    video = cv2.VideoCapture(0)  # 选择摄像头0、1... 或 选择视频路径
    while True:
        ret, img = video.read()
        # 获取摄像头或视频的一帧，ret判断获取是否成功，成功则为True；img为获取的图像
        if ret:
            cv2.imshow("img", img)  # 显示图像（显示名称，显示对象）
            cv2.waitKey(0)  # 等待时间
            cv2.destroyAllWindows()
        else:
            print("摄像头未打开。")
            pass    # 图像获取失败，可能未接入摄像头
            
