import pydicom
import numpy as np
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_modality_lut, apply_voi_lut

window_center = -600
window_width = 1600

# DICOM 파일 읽어들이는 함수 -> pydicom.read_file(), pydicom.dcmread()
slice = pydicom.read_file("./ID_0000_AGE_0060_CONTRAST_1_CT.dcm")
print(slice)

s = int(slice.RescaleSlope)
b = int(slice.RescaleIntercept)
image = s * slice.pixel_array + b

#신경세포까지 자세히 보임
plt.subplot(1,3,1)
plt.title("DICOM - > Array")
plt. imshow(image, cmap='gray')

#신경세포같은 부분이 덜 보이고 전체적으로 진하게 보임
slice.WindowCenter = window_center
slice.WindowWidth = window_width
image = apply_modality_lut(image, slice)
image2 = apply_voi_lut(image, slice)
plt.subplot(1,3,2)
plt.title("apply_voi_cut")
plt.imshow(image2, cmap='gray')

#normalization : 조금 더 깔끔하게 보여짐
image3 = np.clip(image, window_center-(window_width/2),
                 window_center+(window_width/2))

plt.subplot(1, 3, 3)
plt.title("normlization")
plt.imshow(image3, cmap='gray')
plt.show()