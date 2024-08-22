export CUDA_VISIBLE_DEVICES=6,7
export PYTHONPATH=$PYTHONPATH:/home/tyh/git/LLaMA-Factory/src

python -c 'from llamafactory.cli import main; main()' train ./config/qwen_lora_sft_ds3.yaml
python -c 'from llamafactory.cli import main; main()' export ./config/qwen_lora_sft_merge.yaml
