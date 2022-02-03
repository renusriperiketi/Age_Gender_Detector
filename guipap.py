{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "c3d6ccbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "bf16e3b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import filedialog"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "d37c370e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "9b058aad",
   "metadata": {},
   "outputs": [],
   "source": [
    "from PIL import Image,ImageTk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "32d548ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "9f55620d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "8a1de8b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Loading the Model\n",
    "from keras.models import load_model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "c526d02a",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=load_model('Age_Sex_Detection.hS')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "2be52536",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initialising the GUI\n",
    "top=tk.Tk()\n",
    "top.geometry('800x600')\n",
    "top.title('Age & Gender Detector')\n",
    "top.configure(background='#CDCDCD')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "98312a99",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initialising the Labels (1 for age and 1 for Gender)\n",
    "label1=Label(top,background='#CDCDCD',font=('arial',15,\"bold\"))\n",
    "label2=Label(top,background='#CDCDCD',font=('arial',15,'bold'))\n",
    "sign_image=Label(top)\n",
    "\n",
    "#Defining Detect function which detects the age and gender of the person in image using the model\n",
    "def Detect(file_path):\n",
    "    global label_packed\n",
    "    image=Image.open(file_path)\n",
    "    image=image.resize((48,48))\n",
    "    image=numpy.expand_dims(image,axis=0)\n",
    "    image=np.array(image)\n",
    "    image=np.delete(image,0,1)\n",
    "    image=np.resize(image,(48,48,3))\n",
    "    print (image.shape)\n",
    "    sex_f=[\"Male\",\"Female\"]\n",
    "    image=np.array([image])/255\n",
    "    pred=model.predict(image)\n",
    "    age=int(np.round(pred[1][0]))\n",
    "    sex=int(np.round(pred[0][0]))\n",
    "    print(\"Predicted Age is \"+ str(age))\n",
    "    print(\"Predicted Gender is \"+sex_f[sex])\n",
    "    label1.configure(foreground=\"#011638\",text=age)\n",
    "    label2.configure(foreground=\"#011638\",text=sex_f[sex])\n",
    "\n",
    "#Defining Show_detect button function\n",
    "def show_Detect_button(file_path):\n",
    "    Detect_b=Button(top,text=\"Detect Image\",command=lambda: Detect(file_path),padx=10,pady=5)\n",
    "    Detect_b.configure(background=\"#364156\",foreground='white',font=('arial',10,'bold'))\n",
    "    Detect_b.place(relx=0.79,rely=0.46)\n",
    "    \n",
    "#Defining Upload Image Function\n",
    "def upload_image():\n",
    "    try:\n",
    "        file_path=filedialog.askopenfilename()\n",
    "        uploaded=Image.open(file_path)\n",
    "        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))\n",
    "        im=ImageTk.PhotoImage(uploaded)\n",
    "        \n",
    "        sign_image.configure(image=im)\n",
    "        sign_image.image=im\n",
    "        label1.configure(text='')\n",
    "        label2.configure(text='')\n",
    "        show_Detect_button(file_path)\n",
    "    except:\n",
    "        pass\n",
    "    \n",
    "upload=Button(top,text=\"Upload an Image\",command=upload_image,padx=10,pady=5)\n",
    "upload.configure(background='#364156',foreground='white',font=('arial',10,'bold'))\n",
    "upload.pack(side='bottom',pady=50)\n",
    "sign_image.pack(side='bottom',expand=True)\n",
    "\n",
    "label1.pack(side='bottom',expand=True)\n",
    "label2.pack(side=\"bottom\",expand=True)\n",
    "heading=Label(top,text=\"Age and Gender Detector\",pady=20,font=('arial',20,\"bold\"))\n",
    "heading.configure(background='#CDCDCD',foreground=\"#364156\")\n",
    "heading.pack()\n",
    "top.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "566c4fab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
