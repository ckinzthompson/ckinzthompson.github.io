---
layout: posts
author: Colin Kinz-Thompson
title: Contrastive Unpaired Translation of a single CryoEM image > Negative Stain image
date: 2020-09-27
---

# Idea
Use machine learning to turn Cryo EM images in negative stain TEM images, and back and forth.

## Methods
Use a machine learning approach called contrastive unpaired translation [link here](https://github.com/taesungp/contrastive-unpaired-translation). This allows you to do single image to single image translation! Very cool! Here's the paper on [arXiv](https://arxiv.org/pdf/2007.15651.pdf).

I used the GPUs on to run this [Google Collab](https://colab.research.google.com/)

Make sure you have the gpu on in the notebook.
(Edit >> notebook settings)


## Results
I think it's pretty obvious that I needed to train more (stopped after first of 16 epochs (~50 mins)). This doesn't quite look like a negative stain image it's clearly going in the right direction! More training data (instead of a random image I pulled from the internet), and more training epochs should help!

![png](https://ckinzthompson.github.io/img/em/CUT_cryoem_12_0.png)


## Conclusions
This is an insane idea without any scientific merit. To put it into perspective, imagine turning a single-molecule fluorescence image into a cryo-EM image...
It's cool though!


## Appendix

Just for fun, let's try to turn an EM image into a David Goodsell style image.

Use this [cell section](https://cdn.thinglink.me/api/image/698929919408734209/1240/10/scaletowidth)

pull targets (1024x1024) from this image:
[Goodsell target](https://cdn.rcsb.org/pdb101/motm/tiff/247-Myelinassociated_Glycoprotein-Myelin.tif)

![png](https://ckinzthompson.github.io/img/em/CUT_goodsell.png)
It's starting to work. I'm not totally sure why it's all blue, but more training might help. Finally, more images in the training will probably help the style transfer.


## The Jupyter Notebook

Check to make sure you have GPU access
```python
!nvidia-smi
```
    Sun Sep 27 19:11:45 2020       
    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 450.66       Driver Version: 418.67       CUDA Version: 10.1     |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |                               |                      |               MIG M. |
    |===============================+======================+======================|
    |   0  Tesla T4            Off  | 00000000:00:04.0 Off |                    0 |
    | N/A   41C    P8    10W /  70W |      0MiB / 15079MiB |      0%      Default |
    |                               |                      |                 ERR! |
    +-------------------------------+----------------------+----------------------+

    +-----------------------------------------------------------------------------+
    | Processes:                                                                  |
    |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
    |        ID   ID                                                   Usage      |
    |=============================================================================|
    |  No running processes found                                                 |
    +-----------------------------------------------------------------------------+


Download the CUT git repo
```python
!git clone https://github.com/taesungp/contrastive-unpaired-translation.git
```

    Cloning into 'contrastive-unpaired-translation'...
    remote: Enumerating objects: 235, done.[K
    remote: Counting objects: 100% (235/235), done.[K
    remote: Compressing objects: 100% (172/172), done.[K
    remote: Total 235 (delta 115), reused 172 (delta 58), pack-reused 0[K
    Receiving objects: 100% (235/235), 17.89 MiB | 31.59 MiB/s, done.
    Resolving deltas: 100% (115/115), done.

Move into the folder
```python
import os
print(os.getcwd())
os.chdir('contrastive-unpaired-translation')
```

Install all the requirements
```python
!pip install -r requirements.txt
```

    Requirement already satisfied: torch>=1.4.0 in /usr/local/lib/python3.6/dist-packages (from -r requirements.txt (line 1)) (1.6.0+cu101)
    Requirement already satisfied: torchvision>=0.5.0 in /usr/local/lib/python3.6/dist-packages (from -r requirements.txt (line 2)) (0.7.0+cu101)
    Collecting dominate>=2.4.0
      Downloading https://files.pythonhosted.org/packages/c0/03/1ba70425be63f2aab42fbc98894fe5d90cdadd41f79bdc778b3e404cfd8f/dominate-2.5.2-py2.py3-none-any.whl
    Collecting visdom>=0.1.8.8
    [?25l  Downloading https://files.pythonhosted.org/packages/c9/75/e078f5a2e1df7e0d3044749089fc2823e62d029cc027ed8ae5d71fafcbdc/visdom-0.1.8.9.tar.gz (676kB)
    [K     |████████████████████████████████| 686kB 9.5MB/s
    [?25hRequirement already satisfied: packaging in /usr/local/lib/python3.6/dist-packages (from -r requirements.txt (line 5)) (20.4)
    Collecting GPUtil>=1.4.0
      Downloading https://files.pythonhosted.org/packages/ed/0e/5c61eedde9f6c87713e89d794f01e378cfd9565847d4576fa627d758c554/GPUtil-1.4.0.tar.gz
    Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from torch>=1.4.0->-r requirements.txt (line 1)) (1.18.5)
    Requirement already satisfied: future in /usr/local/lib/python3.6/dist-packages (from torch>=1.4.0->-r requirements.txt (line 1)) (0.16.0)
    Requirement already satisfied: pillow>=4.1.1 in /usr/local/lib/python3.6/dist-packages (from torchvision>=0.5.0->-r requirements.txt (line 2)) (7.0.0)
    Requirement already satisfied: scipy in /usr/local/lib/python3.6/dist-packages (from visdom>=0.1.8.8->-r requirements.txt (line 4)) (1.4.1)
    Requirement already satisfied: requests in /usr/local/lib/python3.6/dist-packages (from visdom>=0.1.8.8->-r requirements.txt (line 4)) (2.23.0)
    Requirement already satisfied: tornado in /usr/local/lib/python3.6/dist-packages (from visdom>=0.1.8.8->-r requirements.txt (line 4)) (5.1.1)
    Requirement already satisfied: pyzmq in /usr/local/lib/python3.6/dist-packages (from visdom>=0.1.8.8->-r requirements.txt (line 4)) (19.0.2)
    Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from visdom>=0.1.8.8->-r requirements.txt (line 4)) (1.15.0)
    Collecting jsonpatch
      Downloading https://files.pythonhosted.org/packages/4f/d0/34b0f59ac08de9c1e07876cfecd80aec650600177b4bd445124c755499a7/jsonpatch-1.26-py2.py3-none-any.whl
    Collecting torchfile
      Downloading https://files.pythonhosted.org/packages/91/af/5b305f86f2d218091af657ddb53f984ecbd9518ca9fe8ef4103a007252c9/torchfile-0.1.0.tar.gz
    Collecting websocket-client
    [?25l  Downloading https://files.pythonhosted.org/packages/4c/5f/f61b420143ed1c8dc69f9eaec5ff1ac36109d52c80de49d66e0c36c3dfdf/websocket_client-0.57.0-py2.py3-none-any.whl (200kB)
    [K     |████████████████████████████████| 204kB 19.3MB/s
    [?25hRequirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.6/dist-packages (from packaging->-r requirements.txt (line 5)) (2.4.7)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.6/dist-packages (from requests->visdom>=0.1.8.8->-r requirements.txt (line 4)) (2020.6.20)
    Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.6/dist-packages (from requests->visdom>=0.1.8.8->-r requirements.txt (line 4)) (3.0.4)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.6/dist-packages (from requests->visdom>=0.1.8.8->-r requirements.txt (line 4)) (1.24.3)
    Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/dist-packages (from requests->visdom>=0.1.8.8->-r requirements.txt (line 4)) (2.10)
    Collecting jsonpointer>=1.9
      Downloading https://files.pythonhosted.org/packages/18/b0/a80d29577c08eea401659254dfaed87f1af45272899e1812d7e01b679bc5/jsonpointer-2.0-py2.py3-none-any.whl
    Building wheels for collected packages: visdom, GPUtil, torchfile
      Building wheel for visdom (setup.py) ... [?25l[?25hdone
      Created wheel for visdom: filename=visdom-0.1.8.9-cp36-none-any.whl size=655251 sha256=c3d7207080e1a4c8bc4df5b7bedc7fd1e9f703d56b17986f38e40450ffee6628
      Stored in directory: /root/.cache/pip/wheels/70/19/a7/6d589ed967f4dfefd33bc166d081257bd4ed0cb618dccfd62a
      Building wheel for GPUtil (setup.py) ... [?25l[?25hdone
      Created wheel for GPUtil: filename=GPUtil-1.4.0-cp36-none-any.whl size=7411 sha256=338c1378a7230ea2a4c0d1b37232d361f58df862b9aa60db2e7c9c7ed8edda8c
      Stored in directory: /root/.cache/pip/wheels/3d/77/07/80562de4bb0786e5ea186911a2c831fdd0018bda69beab71fd
      Building wheel for torchfile (setup.py) ... [?25l[?25hdone
      Created wheel for torchfile: filename=torchfile-0.1.0-cp36-none-any.whl size=5711 sha256=c8b031dcd0d775a042d547d4444a09e353704dd2ea1333c792bdca09acbd63ef
      Stored in directory: /root/.cache/pip/wheels/b1/c3/d6/9a1cc8f3a99a0fc1124cae20153f36af59a6e683daca0a0814
    Successfully built visdom GPUtil torchfile
    Installing collected packages: dominate, jsonpointer, jsonpatch, torchfile, websocket-client, visdom, GPUtil
    Successfully installed GPUtil-1.4.0 dominate-2.5.2 jsonpatch-1.26 jsonpointer-2.0 torchfile-0.1.0 visdom-0.1.8.9 websocket-client-0.57.0


Download the data
```python
!ls ./datasets/cryoem
!mkdir ./datasets/cryoem/trainA
!mkdir ./datasets/cryoem/trainB

import urllib.request
urllib.request.urlretrieve("https://ckinzthompson.github.io/img/em/em.jpg", "./datasets/cryoem/trainA/em.jpg")
urllib.request.urlretrieve("https://ckinzthompson.github.io/img/em/stain.jpg", "./datasets/cryoem/trainB/stain.jpg")
```

    ('./datasets/cryoem/trainA/em.jpg', <http.client.HTTPMessage object at 0x7f4392f50048>)
    ('./datasets/cryoem/trainB/stain.jpg', <http.client.HTTPMessage object at 0x7f4392f50048>)


Run the training
```python
!python train.py --model sincut --name cryoem --dataroot ./datasets/cryoem
```

    ----------------- Options ---------------
                     CUT_mode: CUT                           
                   batch_size: 16                            
                        beta1: 0.0                           
                        beta2: 0.99                          
              checkpoints_dir: ./checkpoints                 
               continue_train: False                         
                    crop_size: 64                            
                     dataroot: ./datasets/cryoem             	[default: placeholder]
                 dataset_mode: singleimage                   
                    direction: AtoB                          
                  display_env: main                          
                 display_freq: 400                           
                   display_id: None                          
                display_ncols: 4                             
                 display_port: 8097                          
               display_server: http://localhost              
              display_winsize: 256                           
                   easy_label: experiment_name               
                        epoch: latest                        
                  epoch_count: 1                             
              evaluation_freq: 5000                          
            flip_equivariance: False                         
                     gan_mode: nonsaturating                 
                      gpu_ids: 0                             
                    init_gain: 0.02                          
                    init_type: xavier                        
                     input_nc: 3                             
                      isTrain: True                          	[default: None]
                   lambda_GAN: 1.0                           
                   lambda_NCE: 4.0                           
                    lambda_R1: 1.0                           
              lambda_identity: 1.0                           
                    load_size: 1024                          
                           lr: 0.002                         
               lr_decay_iters: 50                            
                    lr_policy: linear                        
             max_dataset_size: inf                           
                        model: sincut                        	[default: cut]
                     n_epochs: 8                             
               n_epochs_decay: 8                             
                   n_layers_D: 3                             
                         name: cryoem                        	[default: experiment_name]
                        nce_T: 0.07                          
                      nce_idt: True                          
    nce_includes_all_negatives_from_minibatch: True                          
                   nce_layers: 0,2,4                         
                          ndf: 8                             
                         netD: stylegan2                     
                         netF: mlp_sample                    
                      netF_nc: 256                           
                         netG: stylegan2                     
                          ngf: 10                            
                 no_antialias: False                         
              no_antialias_up: False                         
                   no_dropout: True                          
                      no_flip: False                         
                      no_html: False                         
                        normD: instance                      
                        normG: instance                      
                  num_patches: 1                             
                  num_threads: 4                             
                    output_nc: 3                             
                        phase: train                         
                    pool_size: 0                             
                   preprocess: zoom_and_patch                
              pretrained_name: None                          
                   print_freq: 100                           
             random_scale_max: 3.0                           
                 save_by_iter: False                         
              save_epoch_freq: 1                             
             save_latest_freq: 20000                         
               serial_batches: False                         
    stylegan2_G_num_downsampling: 1                             
                       suffix:                               
             update_html_freq: 1000                          
                      verbose: False                         
    ----------------- End -------------------
    Image sizes (1024, 1024) and (1024, 1024)
    dataset [SingleImageDataset] was created
    model [SinCUTModel] was created
    The number of training images = 100000
    Setting up a new session...
    create web directory ./checkpoints/cryoem/web...
    [W TensorIterator.cpp:918] Warning: Mixed memory format inputs detected while calling the operator. The operator will output contiguous tensor even if some of the inputs are in channels_last format. (function operator())
    [W TensorIterator.cpp:924] Warning: Mixed memory format inputs detected while calling the operator. The operator will output channels_last tensor even if some of the inputs are not in channels_last format. (function operator())
    ---------- Networks initialized -------------
    [Network G] Total number of parameters : 3.068 M
    [Network F] Total number of parameters : 0.281 M
    [Network D] Total number of parameters : 5.885 M
    -----------------------------------------------
    (epoch: 1, iters: 400, time: 0.093, data: 1.451) G_GAN: 1.132 D_real: 0.489 D_fake: 0.336 G: 12.148 NCE: 10.780 NCE_Y: 10.923 D_R1: 0.028 idt: 0.164
    (epoch: 1, iters: 800, time: 0.085, data: 0.002) G_GAN: 0.863 D_real: 1.163 D_fake: 0.212 G: 11.428 NCE: 11.329 NCE_Y: 9.252 D_R1: 0.014 idt: 0.275

    ...
    ...
    ...

    (epoch: 1, iters: 100000, time: 0.031, data: 0.002) G_GAN: 1.263 D_real: 0.348 D_fake: 0.851 G: 4.615 NCE: 3.781 NCE_Y: 2.801 D_R1: 0.033 idt: 0.061
    saving the latest model (epoch 1, total_iters 100000)
    cryoem
    saving the model at the end of epoch 1, iters 100000
    End of epoch 1 / 16 	 Time Taken: 3092 sec
    learning rate = 0.0020000
    (epoch: 2, iters: 400, time: 0.031, data: 1.208) G_GAN: 1.243 D_real: 0.496 D_fake: 0.575 G: 4.266 NCE: 3.445 NCE_Y: 2.513 D_R1: 0.035 idt: 0.045
    (epoch: 2, iters: 800, time: 0.031, data: 0.001) G_GAN: 1.564 D_real: 0.439 D_fake: 0.636 G: 4.901 NCE: 3.774 NCE_Y: 2.796 D_R1: 0.034 idt: 0.052
    (epoch: 2, iters: 1200, time: 0.031, data: 0.002) G_GAN: 1.213 D_real: 0.490 D_fake: 0.684 G: 4.882 NCE: 3.822 NCE_Y: 3.437 D_R1: 0.042 idt: 0.039
    Traceback (most recent call last):
      File "train.py", line 49, in <module>
        torch.cuda.synchronize()
      File "/usr/local/lib/python3.6/dist-packages/torch/cuda/__init__.py", line 398, in synchronize
        return torch._C._cuda_synchronize()
    KeyboardInterrupt


Translate the image using the model from the latest checkput
```python
!python test.py --model sincut --name cryoem --dataroot ./datasets/cryoem
```

    ----------------- Options ---------------
                     CUT_mode: CUT                           
                   batch_size: 1                             
                        beta1: 0.0                           
                        beta2: 0.99                          
              checkpoints_dir: ./checkpoints                 
                    crop_size: 64                            
                     dataroot: ./datasets/cryoem             	[default: placeholder]
                 dataset_mode: singleimage                   
                    direction: AtoB                          
              display_winsize: 256                           
                   easy_label: experiment_name               
                        epoch: latest                        
                         eval: False                         
            flip_equivariance: False                         
                     gan_mode: nonsaturating                 
                      gpu_ids: 0                             
                    init_gain: 0.02                          
                    init_type: xavier                        
                     input_nc: 3                             
                      isTrain: False                         	[default: None]
                   lambda_GAN: 1.0                           
                   lambda_NCE: 4.0                           
                    lambda_R1: 1.0                           
              lambda_identity: 1.0                           
                    load_size: 1024                          
                           lr: 0.002                         
             max_dataset_size: inf                           
                        model: sincut                        	[default: cut]
                   n_layers_D: 3                             
                         name: cryoem                        	[default: experiment_name]
                        nce_T: 0.07                          
                      nce_idt: True                          
    nce_includes_all_negatives_from_minibatch: True                          
                   nce_layers: 0,2,4                         
                          ndf: 8                             
                         netD: stylegan2                     
                         netF: mlp_sample                    
                      netF_nc: 256                           
                         netG: stylegan2                     
                          ngf: 10                            
                 no_antialias: False                         
              no_antialias_up: False                         
                   no_dropout: True                          
                      no_flip: False                         
                        normD: instance                      
                        normG: instance                      
                  num_patches: 1                             
                     num_test: 1                             
                  num_threads: 4                             
                    output_nc: 3                             
                        phase: test                          
                    pool_size: 0                             
                   preprocess: none                          
             random_scale_max: 3.0                           
                  results_dir: ./results/                    
               serial_batches: False                         
    stylegan2_G_num_downsampling: 1                             
                       suffix:                               
                      verbose: False                         
    ----------------- End -------------------
    Image sizes (1024, 1024) and (1024, 1024)
    dataset [SingleImageDataset] was created
    Image sizes (1024, 1024) and (1024, 1024)
    dataset [SingleImageDataset] was created
    model [SinCUTModel] was created
    creating web directory ./results/cryoem/test_latest
    loading the model from ./checkpoints/cryoem/latest_net_G.pth
    ---------- Networks initialized -------------
    [Network G] Total number of parameters : 3.068 M
    -----------------------------------------------
    processing (0000)-th image... ['./datasets/cryoem/trainA/em.jpg']


Plot the final picture
```python
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,3,figsize=(12,18),dpi=100)
img1 = plt.imread('./results/cryoem/test_latest/images/fake_B/em.png')
img2 = plt.imread('./results/cryoem/test_latest/images/real_A/em.png')
img3 = plt.imread('./results/cryoem/test_latest/images/real_B/em.png')
ax[0].set_title('Original (CryoEM)')
ax[1].set_title('Translation (cryo->stain)')
ax[2].set_title('Style (Negative Stain)')
ax[1].imshow(img1)
ax[0].imshow(img2)
ax[2].imshow(img3)
plt.savefig('cryoem_test_img.png')

```
