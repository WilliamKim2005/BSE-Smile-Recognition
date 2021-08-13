# Smile Recognition with Machine Learning
By: William Kim

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| William Kim | Hunter College High School | Business/Engineering | Incoming Junior
  
# Final Milestone
For my final milestone, after I finished the tedious process of classifying the 400 faces, I then used a image to test if my model was working. 
![image](https://user-images.githubusercontent.com/87985881/129373767-84fdb63d-b2dd-4005-9c2f-5d93deffe291.png)

# Second Milestone
My second milestone was finding a database from Sklearn called the "Olivetti faces dataset". From there made a user interface so I could classify the 400 images in the dataset as either smiling or not smiling. 
```python 
trainer = Trainer() 
def display_face(face):
    clear_output()
    plt.imshow(face, cmap='gray')
    plt.axis('off')

def update_smile(b):
    trainer.record_result(smile=True)
    trainer.increment_face()
    display_face(trainer.imgs[trainer.index])

def update_no_smile(b):
    trainer.record_result(smile=False)
    trainer.increment_face()
    display_face(trainer.imgs[trainer.index])
button_smile = Button(description='smile')
button_no_smile = Button(description='sad face')
out=widgets.Output()

def display_face(face):
    clear_output()
    plt.imshow(face, cmap='gray')
    plt.axis('off')

def update_smile(b):
    trainer.record_result(smile=True)
    trainer.increment_face()
    display_face(trainer.imgs[trainer.index])

def update_no_smile(b):
    trainer.record_result(smile=False)
    trainer.increment_face()
    display_face(trainer.imgs[trainer.index])

button_no_smile.on_click(update_no_smile)
button_smile.on_click(update_smile)

display(button_smile)
display(button_no_smile)
display_face(trainer.imgs[trainer.index])
buttons = widgets.HBox([button_smile, button_no_smile])
widgets.VBox([buttons,out])'''
# First Milestone
![image](https://cdn.discordapp.com/attachments/870297608189542430/875026705851486208/image0.jpg)
My first milestone was setting up my Rasberry Pi. I was able to connect the power supply, monitor, and camera to my Pi. I was also able to install the OS onto my Pi using a micro sd card and a chip reader. Also, I found a data set I can use for my machine learning program. 

