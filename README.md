This project was made to control a computer's mouse with only hand gestures.

# Current state

- Very unstable and shaky, hard to control
- Need to make the gestures more smooth and elegant with fingers instead of entire hand, instead of kinect sensor
- Scaling math ratios are off
- Handle extra complexity when there are multiple monitors

# Setup

1. Install Anaconda or Miniconda
2. Setup main environment

```
conda env create -f environment.yml
conda activate gestures
```

# Add libraries

```
conda install -n gestures [package_name]
conda env export --name gestures > environment.yml
```

# Remove conda environment

```
conda env remove --name gestures
```

# Permissions to allow
- video recording
- allow in settings to have accessibility to mouse control
