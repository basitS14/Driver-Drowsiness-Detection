import os
import random
import shutil

data_path = "Drowsy/train_data/"
drowsy_img = os.path.join( data_path, 'drowsy')
notdrowsy_img = os.path.join( data_path, 'notdrowsy')

# os.mkdir("Drowsy/test_data")
test_folder = os.path.join("Drowsy\\" , "test_data")

image_extension = ['.jpg' , 'jpeg' , '.png']

drowsy_img_list = [file for file in os.listdir(drowsy_img)]
notdrowsy_img_list = [file for file in os.listdir(notdrowsy_img)]


print("drowsy:" , len(drowsy_img_list) , 'notdrowsy:' ,len(notdrowsy_img_list))

random.seed(42)

random.shuffle(drowsy_img_list)
random.shuffle(notdrowsy_img_list)


test_size = int((len(drowsy_img_list) + len(notdrowsy_img_list))*0.2) // 2
print(test_size)
# os.makedirs(os.path.join(test_folder , "drowsy"))
# os.makedirs(os.path.join(test_folder , "notdrowsy"))

for i in range(test_size):
    shutil.move(os.path.join(drowsy_img , drowsy_img_list[i]) ,
                os.path.join('Drowsy/test_data/drowsy' , drowsy_img_list[i]) )

    shutil.move(os.path.join(notdrowsy_img , notdrowsy_img_list[i]) ,
                    os.path.join('Drowsy/test_data/notdrowsy' , notdrowsy_img_list[i]) )




