import cv2
from torch.utils.data.dataset import Dataset
from torchvision import transforms
label_dic = {"cat": 0, "dog": 1}



class MyCustomDataset(Dataset):
    def __init__(self, path): # __init__ : csv읽기,변환 할당, 데이터 필터링 등 초기 논리가 발생하는 곳
        # data path
        self.all_data_path = "./image/*.jpg"
        self.transforms = transforms

    def __getitem__(self, index): # __getitem__ : 데이터와 레이블을 반환
        image_path = self.all_data_path[index]
        # " image01.png, image02.png, image03.png ..."
        label_temp = image_path.split("/")
        label_temp = label_temp[2]
        label_temp = label_temp.replace(".jpg", "")
        label = label_dic[label_temp]
        # cat -> 0
        # [. , image, cat.jpg]

        # image read
        image = cv2.imread(image_path)

        if self.transforms is not None:
            image = self.transforms(image)

        return filename, bbox
        # return image, label

    def __len__(self): # __len__ : 보유한 샘플 수를 반환
        return len(self.all_data_path)

temp = MyCustomDataset("./dataset")

for i in temp:
    print(i)
    # image01 xywh