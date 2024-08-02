import numpy as np
from PIL import Image, ImageDraw
import csv
import random as ran


# Ile próbek ma wygenerować
probes=10

# Tablica do zapisania współrzędnych środka
centerPoint = np.zeros((probes, 2))


#Generate spiral shapes with random position of center.
def generate_spiral_image(size=100, max_intensity=100, number=0):
    # Create an empty image with white background
    img = Image.new('L', (size, size), color=0)
    draw = ImageDraw.Draw(img)
    
    
    # Begining of the spiral. (Center point)
    # Center of the image
    ranX = ran.randrange(0, 100)
    ranY = ran.randrange(0, 100)
    center = (ranX, ranY)  #(size // 2, size // 2)
    centerPoint[number, 0] = ranX
    centerPoint[number, 1] = ranY

    # Spiral parameters
    a = 1
    b = 1
    num_points = 1000

    for i in range(num_points):
        angle = 0.1 * i
        x = int(center[0] + (a + b * angle) * np.cos(angle))
        y = int(center[1] + (a + b * angle) * np.sin(angle))

        if 0 <= x < size and 0 <= y < size:
            draw.point((x, y), fill=max_intensity)


    return img


# Image size
size = 100

#Series of spiral images saves as picture and csv's.


# Wielkość 200 bo dwia obrazki zapisuje
save_array = np.empty( (100, (probes*100) ) )
deltaStart=0
deltaEnd=100

for i in range(probes):

    # Generate spiral image
    spiral_image = generate_spiral_image(size, 100, i)

    # Save the image
    spiral_image.save('probes/spiral'+str(i)+'.png')

    # Create Ccsv file with center saved
    csv_file_path = 'probes/spiralCenter.csv'
    with open(csv_file_path, mode='w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerows(centerPoint)



    # Create a CSV file with pixel values
    csv_file_path = 'probes/spiralTest.csv'
    with open(csv_file_path, mode='w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file, delimiter=',')

        # Convert image to numpy array
        pixel_data = np.array(spiral_image)

        # Normalize pixel values from 0 to 100
        normalized_pixel_data = (pixel_data / 255) * 100

        csv_file.seek(0, 1)

        # Write into array as rows
        #for row in normalized_pixel_data:
        #    csv_writer.writerow(row.astype(int))
        wiersz=0
        for row in normalized_pixel_data:
            save_array[wiersz, deltaStart : deltaEnd ] = row
            wiersz+=1

        deltaStart += size
        deltaEnd += size
        for i in range(100):
            csv_writer.writerow(save_array[i].astype(int))

            #csv_writer.writerow(row.astype(int))

#print(save_array.shape)
#print(save_array)


# Write pixel values to CSV file
#for i in range(100):
#    csv_writer.writerow(row.astype(int))




