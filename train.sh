#!/bin/bash
#
#SBATCH --job-name=OCR_DET_1              # Job name
#SBATCH --output=my_gpu_job_output.log    # Output file
#SBATCH --error=my_gpu_job_error.log      # Error log file
#SBATCH --nodes=1                         # Request 1 node
#SBATCH --ntasks=1                        # Total number of tasks
#SBATCH --gres=gpu:1                      # Request 1 GPU
#SBATCH --time=4:00:00                   # Maximum job run time
#SBATCH --export=NONE                     # Do not export current environment variables

# Ensure environment variables are not exported
unset SLURM_EXPORT_ENV

# Load necessary modules
module load python/3.12
module load cuda/12.6                     # Load CUDA and cuDNN module
module load cudnn/8.9

# 安装requirements.txt中的依赖
pip install --no-index --find-links=offline\ dependencies/ paddlepaddle-gpu
pip install --no-index --find-links=offline\ dependencies/ requirements
pip install --no-index --find-links=offline\ dependencies/ visualdl

# Run your application
srun python tools/train.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_cml.yml

# 启动 VisualDL 服务
visualdl --logdir ./log --port 8040